import logging
import logging.handlers
import time
from multiprocessing import Process, Queue, cpu_count

from collector.dns_context import DNSContext
from collector.model.local_windows import LocalComputerData, instanciate
from collector.utils import ADContext
from collector.windows.ad.computer import Computer
from collector.windows.dcerpc.collect import dcerpc_collect
from collector.windows.psrp_collect import collect

main_logger = logging.getLogger(__name__)


class WindowsComputerProcessor(Process):
    def __init__(self, context: ADContext, queue: Queue, worker_id: int, **kwargs):
        super().__init__(**kwargs)
        if context.logger_manager is not None:
            self.debug_level = context.logger_manager.level
            self.logger_formatter = context.logger_manager.formatter
            self.log_queue = context.logger_manager.get_queue()
        else:
            raise Exception("Logger not initialized")
        self.logger = None
        self.out_dir = context.output_directory
        self.input_queue = queue
        self.auth = context.host_auth_method
        self.user_profile = context.user_profile
        self.worker_id = worker_id
        self.collect_method = context.host_collect_method

    def __do_export(self, target: Computer, results: dict) -> bool:
        # Privacy mode enabled
        if target.exporter.privacy:
            local_data: LocalComputerData | None = None

            try:
                start_time = time.perf_counter()
                local_data = instanciate(LocalComputerData, results)
                elapsed = time.perf_counter() - start_time
                self.logger.debug(f"Instanciation completed in {elapsed:.3f} seconds")
            except Exception as e:
                self.logger.debug(f"Cannot instantiate LocalComputerData: {e}")
                self.logger.debug("Privacy process will not be applied")

            # Apply anonymisation if possible
            if target.anonymiser and local_data:
                start_time = time.perf_counter()
                target.anonymiser.local_data = local_data
                anon_data = target.anonymiser.process()
                elapsed = time.perf_counter() - start_time
                self.logger.debug(f"Anonymisation completed in {elapsed:.3f} seconds")

                # Export anonymised data
                target.exporter.export(anon_data, "all.json")
                for name, value in anon_data.__dict__.items():
                    target.exporter.export(value, f"{name}.json")

                # Export mapping of anonymised SIDs
                target.exporter.export(target.anonymiser.mapping, "mapping_sids.json")

                return True

        # Standard export (no privacy)
        if isinstance(results, dict):
            target.exporter.export(results, "all.json")
            for collectable, data in results.items():
                target.exporter.export(data, f"{collectable}.json")
            return True

        return False

    def process_computers(self, logger: logging.Logger, target: Computer) -> bool:
        data: dict | None = None

        if self.collect_method == "psrp":
            data = collect(logger, target, "negotiate", False)
        else:
            data = dcerpc_collect(logger, target)

        if not data:
            return False

        success = self.__do_export(target, data)

        return success

    def run(self):
        # Init Logger
        qh = logging.handlers.QueueHandler(self.log_queue)
        self.logger = logging.getLogger(f"{__name__}.worker_{self.worker_id}")
        self.logger.addHandler(qh)
        self.logger.setLevel(self.debug_level)
        self.logger.debug(f"Process {self.worker_id} Started")
        target: Computer
        for target in iter(self.input_queue.get, "STOP"):
            log_path = target.exporter.out_dir + target.hostname + ".log.txt"
            log_file = logging.FileHandler(log_path)
            log_file.setFormatter(self.logger_formatter)
            self.logger.addHandler(log_file)
            self.logger.debug(f"Starting host collection on {target.hostname}")

            with DNSContext({target.hostname.lower(): target.ip_addr}, self.logger):
                success = self.process_computers(self.logger, target)

            self.logger.debug(f"Collection on {target.hostname} finished: {'Success' if success else 'Failed'}")
            self.logger.removeHandler(log_file)

        self.logger.debug(f"Process {self.worker_id} Finished")


def collect_remote_host(targets: list[Computer], context: ADContext):
    main_logger.debug(f"Start of {len(targets)} host collections")
    queue: Queue = Queue()
    workers: list[Process] = []

    n_workers = context.workers if 0 < context.workers <= cpu_count() else cpu_count()
    if n_workers > len(targets):
        n_workers = len(targets)
    main_logger.info(f"Host collection will use {n_workers} workers")

    for computer in targets:
        queue.put(computer)

    for _ in range(n_workers):
        queue.put("STOP")

    for i in range(0, n_workers):
        p = WindowsComputerProcessor(context, queue, i)
        p.start()
        workers.append(p)

    for proc in workers:
        proc.join()
        main_logger.debug(f"Process {proc.name} exit with code {proc.exitcode}")

    queue.close()
    queue.join_thread()
    main_logger.debug("End of host collection")
