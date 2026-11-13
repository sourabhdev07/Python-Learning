import logging

logger = logging.getLogger("registration")

logger.setLevel(logging.INFO)

handler = logging.FileHandler("registration.log")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)


def register_user(username):

    logger.info("Registration started for %s", username)

    if username:
        logger.info("User %s registered successfully", username)
    else:
        logger.warning("Registration failed: username missing")


register_user("Sourabh")
register_user("")