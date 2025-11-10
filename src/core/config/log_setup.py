import logging


def setup_logging(debug: bool = False):
    """
    Configure application-wide logging.

    Sets the global logging level and format for the application.
    The log level is set to DEBUG if `debug` is True; otherwise, INFO.
    Additionally, suppresses verbose logs from the "httpx" library
    by raising its log level to WARNING.

    Args:
        debug (bool): Whether to enable debug-level logging. Defaults to False.

    Returns:
        None
    """
    log_level = logging.DEBUG if debug else logging.INFO

    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s] #%(levelname)-1s | [%(processName)s] | %(name)s: %(message)s",
        datefmt="%m %d %Y %H:%M:%S",
    )

    logging.getLogger("httpx").setLevel(logging.WARNING)
