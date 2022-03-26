# As per usual, we need to import the logging module.
import logging

# But, we also want to import our specail custom logger.
import misc.custom_logger as _

from misc.submodule import add_records

log = logging.getLogger()  # All files should run this
log.setLevel(logging.DEBUG)  # only a main file should run this


def records():
    """add some different log records"""
    log.debug("debug message from main")
    log.info("info message from main")
    log.warning("warning message from main")
    log.error("error message from main")
    log.critical("critical message from main")


def main():
    # alternatively, setLoggerLevel can be done here.
    log.info("starting app...")
    records()
    add_records()
    log.info("app finished!")

if __name__ == "__main__":
    # alternatively, setLoggerLevel can be done here.
    main()
