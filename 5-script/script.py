import logging
import time
logging.basicConfig(level=logging.INFO, filename='/var/log/sample.log')
while True:
    logging.info("Hello world!")
    time.sleep(5)
