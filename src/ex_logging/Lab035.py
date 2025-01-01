import logging

logging.basicConfig(filename="file1.log",
                    format="%(asctime)s%(message)s",
                    filemode="w")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

x = 3
y = 0

logging.info(f"The values of x and y are {x} and {y}")
try:
    result = x/y
    logging.info(f"x/y is successfull with result {x/y}")
except ZeroDivisionError as err:
    logging.error("ZeroDivisionError:", exc_info=True)

logging.debug("Harmless debug message")
logging.info("Just an information")
logging.warning("It's a warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down")
