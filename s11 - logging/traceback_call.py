import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

try:
    result = 10 / 0
    logging.info(f"calculation done {result}", exc_info=True)

except Exception as e:
    logging.error("Calculation error", exc_info=True)