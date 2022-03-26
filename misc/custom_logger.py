# This is where the magic happens...
import logging  # like a submodule
import pathlib

log = logging.getLogger()  # okay... very normal

"""
But then, we want to do all the centralized setup from here. 
The logger object has the same name so it will report "upwards".
We are going to customize the logger handlers here and make sure
the format is as we want it. 

These changes will propogate back to the top-level logger.
And all this code will be run because we import it from the top module.
"""

# Formatting
log_format = logging.Formatter(
    '%(asctime)s | %(levelname)-8s | %(filename)s | %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z')

# custom logfile location
logs_folder = pathlib.Path(__file__).parents[1] / "logs"
logs_folder.mkdir(exist_ok=True)
log_file =  logs_folder / "main.log"

# File handler
log_file_handler = logging.FileHandler(log_file)
log_file_handler.setFormatter(log_format)
log_file_handler.setLevel(logging.DEBUG)

# Console handler
log_console_handler = logging.StreamHandler()
log_console_handler.setFormatter(log_format)
log_console_handler.setLevel(logging.ERROR)

# add handlers to logger
log.addHandler(log_file_handler)
log.addHandler(log_console_handler)

# Finally, check to see this popping up in the console output. 
log.critical("log setup complete!")
