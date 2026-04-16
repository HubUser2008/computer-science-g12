class BankingSystem:
    # Constructor to initialize account details
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance+= amount
        self.display_account_details()

    # Method to withdraw money
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient Funds")
        else:
            self.balance-= amount
            self.display_account_details()

    # Method to display the account details
    def display_account_details(self):
        print(f"{self.account_holder} has {self.balance} remaining funds")

    # Method to transfer money between accounts
    def transfer(self, amount, recipient_account):
        pass
if __name__ == "__main__":

    Ethan = BankingSystem("Ethan Baillie", 140000)
    Ethan.deposit(45)
    Ethan.withdraw(350)

    Adrian = BankingSystem("Adrian Pierre Louis", 500)

