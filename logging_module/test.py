import logging

logging.basicConfig(
    level=logging.INFO,
)

def user_login(username, user_id):
    
    logging.info("User %s with ID %d logged in successfully" , username, user_id)
    
user_login("Sourabh" , 101)