import logging
import time
# add filemode="w" to overwrite

def log():
    logging.basicConfig(filename='sample.log',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

    # "application" code
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warn message")
    logging.error("error message")
    logging.critical("critical message")

while True:
    time.sleep(1) #sleep for 1 second
    log()
