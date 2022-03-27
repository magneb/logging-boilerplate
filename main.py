# As per usual, we need to import the logging module.
import logging
import os

# But, we also want to import our specail custom logger.
from misc.custom_logger import setup_log

from misc.submodule import add_records
from misc.mp_module import process_data
import multiprocessing

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
    setup_log()
    log.critical(f"starting app... {os.getpid()}")
    pool = multiprocessing.Pool()
    pool.apply_async(process_data)
    pool.apply_async(process_data)
    pool.apply_async(process_data)
    records()
    add_records()
    log.debug("closing pool...")
    pool.close()
    pool.join()
    log.debug("pool closed!")
    log.info("app finished!")

if __name__ == "__main__":
    # alternatively, setLoggerLevel can be done here.
    main()
