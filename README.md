# BankAccount

Creating a bank account in Python using OOP. The goal is to create two classes:

### Account class

The account class represents a bank account. It is constructed without any
arguments.

#### Example: create a new account instance
```python
my_account = Account()
```

| Property              | Description
| -----------           | ---
| `transactions`        | A list of Transaction instances
| `get_balance()`       | A method which returns the account balance
| `deposit(amount)`     | A method which creates a deposit transaction
| `withdraw(amount)`    | A method which creates a withdrawal transaction


#### Example: making transactions
Here's an example of how the end product usage could look:
```python
>>> account = Account()
>>> account.deposit(200)
>>> account.get_balance()
200.0
>>> account.withdraw(10)
>>> account.get_balance()
190.0
```

### Transaction class

A transaction class represents a monetary transaction event. It has two
properties: an amount, and a timestamp.

| Property                      | Description
| ------------                  | --
| `amount: float, int, Decimal` | The amount entered in the constructor
| `timestamp: datetime`         | The date & time which the transaction occurred.


A `Transaction` class must be instantiated with an amount argument, and has an
optional `timestamp` which defaults to `None`. If the timestamp is not
provided, it is automatically set to the current date & time.

```python
>>> from banking import Transaction
>>> transaction = Transaction(100.0)
>>> transaction.timestamp
datetime.datetime(2018, 12, 31, 8, 3, 1)
>>> transaction.amount
100.0

>>> import datetime as dt
>>> transaction = Transaction(10, dt.datetime(2002, 1, 10))
>>> transaction.timestamp
datetime.datetime(2002, 1, 10, 0, 0, 0)
```
