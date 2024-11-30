import logging

# 1. Basic Logging
print("1. Basic Logging")
logging.basicConfig(level=logging.INFO)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# 2. Logging to a File
print("\n2. Logging to a File")
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG)
logging.debug("This debug message is saved to the file")
logging.info("This info message is saved to the file")

# 3. Formatting Log Messages
print("\n3. Formatting Log Messages")
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.debug("This message has a custom format")

# 4. Creating a Logger Object
print("\n4. Creating a Logger Object")
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.ERROR)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Use the logger
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")