# logging.basicConfig() is used to configure the logging system.

import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.debug("Debug message")
# logging.info("Application started")
# logging.warning("Low disk space")
# logging.error("Something went wrong")
# logging.critical("System failure")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s | Line:%(lineno)d | %(message)s | %(name)s | %(funcName)s | %(module)s"
)

def login():
    logging.info("User login successful")

login()



# logging.warning("First message")

# logging.basicConfig(level=logging.DEBUG ,  force=True)

# logging.debug("Second message")