import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("automation")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("automation.log", maxBytes=2000, backupCount=5)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

for i in range(1000):
    logger.info(f"Testing log capacity {i}")

print("Operation Done")