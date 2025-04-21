# Bank Account Project

A mini project using Python's Object-Oriented Programming (OOP) to simulate basic bank operations like deposit, withdraw, and balance check.

# Features

- Create a bank account with account holder's name and balance
- Deposit money into the account
- Withdraw money from the account
- View current balance
- Simple command-line interaction

# Concepts Used

- Python Classes and Objects
- Constructors (__init__)
- Methods
- Conditional Statements
- Simple user input/output

# Sample Usage

```python
account = BankAccount("Naresh", 1000)
account.deposit(500)        # Output: Deposited ₹500. New balance: ₹1500
account.withdraw(200)       # Output: Withdrawn ₹200. New balance: ₹1300
account.display_balance()   # Output: Current Balance: ₹1300
