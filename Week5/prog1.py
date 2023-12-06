import logging

logging.basicConfig(level=logging.DEBUG)

#Create a logger for a specific module
logger = logging.getLogger('my-module')

# Create file handler
file_handler = logging.FileHandler('Week5/my-module.log')

console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Debug Message")
logger.warning("Warning Message")
logger.info("Info message")
logger.error("Error Message")
logger.critical("Critical Message")
