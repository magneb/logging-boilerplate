# All we need to worry about in submodules is to import the logging library
# and add a logger *with the same name* as the top-level logger.

import logging

log = logging.getLogger()  # notice no name given == "root"

def add_records():
    """add some different log records"""
    log.debug("debug message from submodule")
    log.info("info message from submodule")
    log.warning("warning message from submodule")
    log.error("error message from submodule")
    log.critical("critical message from submodule")
