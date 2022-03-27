import logging
import time
import os
from misc.custom_logger import file_handler
import pathlib

log = logging.getLogger("multiprocessor")  # not the root logger

def process_data():
    pid = os.getpid()
    logs_folder = pathlib.Path(__file__).parents[1] / "logs"
    log_file= logs_folder / f"mp_{pid}.log"

    log.addHandler(file_handler(log_file))

    log.info(f"processing data... {os.getpid()}")
    time.sleep(1)
    log.critical(f"data processing working with pid {os.getpid()}")
    time.sleep(1)
    log.info("data processed!")