class BankAccount:
    
    def __init__(self , balance):
        self.__balance = balance
        
    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited Successfully")
        else:
            print("Invalid Amount")
            
    def get_balance(self):
        print("Balance" , self.__balance)
        

account = BankAccount(5000)

# account.__balance(100)
# print(account.balance) === Attribute Error comes --> 'BankAccount' object has no attribute '__balance'
account.deposit(100)
account.get_balance()
                          