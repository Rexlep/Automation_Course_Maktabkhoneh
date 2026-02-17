import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s - %(asctime)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

urls = ["site1.com", "site2.com", "unknown-site.com", "site3.com"]

for url in urls:
    try:
        print(f"in process {url}")
        if "unknown" in url:
            raise ConnectionError("site is not available")

        logging.info(f"successful process {url}")

    except ConnectionError as e:
        logging.error(f"Network error {url}: {e}")
        continue