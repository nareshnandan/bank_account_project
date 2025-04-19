class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")
        print(f"Updated balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"Updated Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def checkbalance(self):
        print(f"Current Balance: ₹{self.balance}")


user_name = input("Enter your name: ")
account = BankAccount(user_name)

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount) 
    elif choice == '2':
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Thank you for using our service!")
        break
    else:
        print("Invalid choice. Please select between 1 and 4.")
