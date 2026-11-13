import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

def place_order(user, order_id, amount):

    logging.info("User %s started placing order", user)

    if amount > 0:
        logging.info(
            "Order %d placed successfully. Amount: Rs.%s",
            order_id,
            amount
        )
    else:
        logging.error("Invalid order amount for user %s", user)


place_order("Sourabh", 501, 2500)
place_order("Rahul", 502, -100)