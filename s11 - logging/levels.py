import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s - %(asctime)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("Error")
logging.critical("This is critical message")
