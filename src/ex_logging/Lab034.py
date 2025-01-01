import logging

logging.basicConfig(filename="file.txt",
                              format="%(asctime)s%(message)s",
                              filemode = "w")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Harmless debug message")
logger.info("Just an information")
logger.warning("It's a warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")