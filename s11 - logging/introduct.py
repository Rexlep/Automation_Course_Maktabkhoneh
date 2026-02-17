import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Program started")
logging.warning("connection lost")
logging.error("error ouccoured")
logging.critical("Critical system damage")
