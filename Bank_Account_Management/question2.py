# Bank Account Management Question

# Create a console application that simulates a simple bank account system. 
# The app should allow users to create accounts, deposit and withdraw money, 
# and view their account balance. Implement basic error handling, 
# such as preventing negative balances.

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return(f"Deposited Amount: {amount} . Current balance is {self.balance}.")
        else:
            return("You can't deposite an amount in below zero!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew amount: {amount}. Current balance is : {self.balance}.")
            else:
                print("Insufficient amount balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def get_balance(self):
        print(f"Your account balance is {self.balance}.")

def main():
    accounts = {}

    while True:
        print("\nWelcome to the bank. \nWhat would you like to do?")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter your name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                balance = float(input("Enter initial deposit amount: "))
                if balance < 0:
                    print("Invalid deposit amount. Please enter a positive number.")
                else:
                    accounts[name] = BankAccount(name, balance)
                    print(f"Account created for {name} with a balance of {balance}.")

        elif choice == "2":
            name = input("Enter your name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("Account does not exist.")

        elif choice == "3":
            name = input("Enter your name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("Account does not exist.")

        elif choice == "4":
            name = input("Enter your name: ")
            if name in accounts:
                accounts[name].get_balance()
            else:
                print("Account does not exist.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
