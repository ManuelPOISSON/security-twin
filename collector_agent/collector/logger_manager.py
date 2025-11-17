import logging
from logging.handlers import QueueListener
from multiprocessing import Queue
from pathlib import Path


class LoggerManager:
    def __init__(self, out_dir: str, level=logging.INFO, log_file=None):
        self.log_queue: Queue = Queue()
        self.out_dir = out_dir
        self.level = level
        self.log_file = log_file
        self.listener = None
        self.formatter = logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s")

    def start(self):
        handlers = []
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        stream_handler.setLevel(self.level)
        handlers.append(stream_handler)

        path = Path(self.out_dir) / "main_log.txt"
        main_file_handler = logging.FileHandler(path)
        main_file_handler.setFormatter(self.formatter)
        handlers.append(main_file_handler)

        if self.log_file:
            file_handler = logging.FileHandler(self.log_file)
            file_handler.setFormatter(self.formatter)
            handlers.append(file_handler)

        self.listener = QueueListener(self.log_queue, *handlers)
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()
        for handler in self.listener.handlers:
            handler.flush()
            handler.close()

    def get_queue(self):
        return self.log_queue
