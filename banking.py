"""
Created banking.py -- Write the application code here

This function will take a number and will ouput as a list of prime numbers.

"""
# pylint: disable=missing-docstring

from datetime import datetime  # using datetime module


class Transaction:
    """created a class called Transaction"""

    def __init__(self, timestamp=None, amount=float):
        self.amount = amount
        self.timestamp = timestamp
        if timestamp is None:
            self.timestamp = datetime.today().strftime('%Y-%m-%d')

    def __repr__(self):
        return f'Transaction(timestamp={self.timestamp} and amount is ${self.amount})'

    def __str__(self):
        return f'Transaction is {self.timestamp}: ${self.amount}'


class InsufficientAmount(Exception):
    pass


class Account:
    """created a class called Account"""

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_list = []

    def deposit(self, amount: float):
        """a method which creates a deposit transaction into bank account"""
        self.balance += amount
        self.transaction_list.append(amount)
        return self.balance

    def withdraw(self, amount: float):
        """a method which creates withdrawal transaction from bank account"""
        if self.balance < amount:
            raise InsufficientAmount
        self.balance -= amount
        self.transaction_list.append(amount)
        return self.balance

    def get_balance(self):
        """a method to return the account balance"""
        print("Account Balance: ", self.balance)


# # to test class Transaction:
# t = Transaction("2022-07-04", 20.00)
# print(t.__repr__())
# print(t.__str__())


# to test class Account:

# b = Account("hana", 5000)
# b.deposit(500)
# b.withdraw(300)
# b.get_balance()
