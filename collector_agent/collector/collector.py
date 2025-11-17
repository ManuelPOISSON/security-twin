import argparse
import logging
import logging.handlers
import sys
import time
from getpass import getpass

from collector.linux.collect import linux_collect
from collector.logger_manager import LoggerManager
from collector.utils import ADContext, BaseContext, LinuxContext, WindowsContext
from collector.windows.ad.active_directory import active_directory_collect
from collector.windows.local_collector import local_windows_context

logger = logging.getLogger("collector")


def parse_cli() -> dict:
    global_parser = argparse.ArgumentParser(add_help=False)
    global_parser.add_argument("-v", "--verbose", action="store_true")
    global_parser.add_argument("--debug", action="store_true")
    global_parser.add_argument("--output-directory", default="", required=False)
    global_parser.add_argument("--log-file", required=False)

    parser = argparse.ArgumentParser(prog="CollectorAgent", description="Collect Data from IS", parents=[global_parser])

    subparsers = parser.add_subparsers(dest="mode", required=True)

    ad_parser = subparsers.add_parser("ad")
    ad_parser.add_argument("-i", "--dc-ip", required=True)
    ad_parser.add_argument("-d", "--domain", required=True)
    ad_parser.add_argument("-u", "--username", required=True)
    ad_parser.add_argument("-p", "--password", required=False)
    ad_parser.add_argument(
        "--ldap-auth-method",
        default="ntlm",
        choices=["simple", "ntlm", "kerberos", "digest-md5", "spnego"],
        required=False,
    )
    ad_parser.add_argument(
        "--host-auth-method", default="negotiate", choices=["ntlm", "negotiate", "kerberos"], required=False
    )
    ad_parser.add_argument("--no-host-collection", dest="host_collection", action="store_false", required=False)
    ad_parser.add_argument("--user-profile", action="store_true", required=False)
    ad_parser.add_argument("--filter-hosts", type=str, nargs="+", required=False)
    ad_parser.add_argument("--workers", type=int, default=0, required=False)
    ad_parser.add_argument("--laps", action="store_true", required=False)
    ad_parser.add_argument("--host-collect-method", default="psrp", choices=["psrp", "rpc"], required=False)
    ad_parser.add_argument("--privacy", action="store_true", required=False)
    ad_parser.add_argument("--laps-user", default="Administrator", required=False)

    windows = subparsers.add_parser("windows")
    windows.add_argument("--output_directory", required=False)

    linux = subparsers.add_parser("linux")
    linux.add_argument("--hostname", required=True)
    linux.add_argument("-p", "--port", type=int, default=22)
    linux.add_argument("-u", "--username", required=True)
    linux.add_argument("--password")
    linux.add_argument("--key-path")
    linux.add_argument("--passphrase")

    args = vars(parser.parse_args())
    mode = args.pop("mode")
    return {"mode": mode, "args": args}


def init_context_from_args(cli: dict) -> BaseContext | None:
    context: BaseContext
    try:
        if cli["mode"] == "ad":
            context = ADContext(**cli["args"])
        elif cli["mode"] == "windows":
            context = WindowsContext(**cli["args"])
        elif cli["mode"] == "linux":
            context = LinuxContext(**cli["args"])
        else:
            raise Exception()
    except Exception as e:
        print(f"Error when unpacking args : {e} ")
        print("Failed to initialize the main context, exit...")
        return None
    if context.debug:
        level = logging.DEBUG
    elif context.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING

    context.logger_manager = LoggerManager(context.output_directory, level, log_file=context.log_file)
    context.logger_manager.start()
    logger.setLevel(context.logger_manager.level)

    logger.handlers.clear()
    logger.addHandler(logging.handlers.QueueHandler(context.logger_manager.get_queue()))
    logger.info("Main Logger Initialized")
    return context


def main():
    args = parse_cli()

    context = init_context_from_args(args)

    if context is None:
        return -1

    begin = time.perf_counter()

    cli = parse_cli()
    context = init_context_from_args(cli)

    if isinstance(context, ADContext):
        if context.password is None:
            context.password = getpass(f"Enter the password for the user {context.username}:")

        active_directory_collect(context)
    elif isinstance(context, WindowsContext):
        if sys.platform == "win32":
            local_windows_context(context)
        else:
            logger.error("Local windows mode enabled, but the current platform is not Windows (win32).")
    elif isinstance(context, LinuxContext):
        linux_collect(context)
    else:
        return -1

    end = time.perf_counter()
    logger.info(f"Total Execution time : {end - begin} s")
    context.logger_manager.stop()
    return 0


if __name__ == "__main__":
    main()
