import logging

logging.basicConfig(
    filename="application.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s "
)

logging.debug("Debugging application")
logging.info("Application started")
logging.warning("Low memory")
logging.error("Database connection failed")
logging.critical("System failure")