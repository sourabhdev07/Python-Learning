import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    filemode='a',
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculate_price(price, quantity):

    try:
        total = price / quantity
        logging.info("Calculation successful")
        return total

    except ZeroDivisionError:
        logging.exception("Quantity cannot be zero")
        # logging.error("Quantity cannot be zero", exc_info=True)

calculate_price(1000, 0)