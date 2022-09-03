# pylint: disable=missing-docstring
"""
The test module for Account
It is a total of 8 test cases
"""
import pytest

from banking import Account, InsufficientAmount


# test case for iniital balance of zero
def test_default_zero_balance():
    """"if balance in account is 0"""
    account = Account(0)
    assert account.balance == 0


def test_name():
    """"if account name is called Jill"""
    account = Account(name="Jill")
    assert account.name == "Jill"

# test cases deposit method:


def test_deposit_one_thousand():
    """if deposit is 1000 """
    account = Account(0)
    assert account.deposit(1000) == 1000


def test_deposit_three_thousand():
    """if deposit is 3000 """
    account = Account(0)
    assert account.deposit(3000) == 3000


def test_deposit_ten_fifty():
    """if deposit is 10.50 """
    account = Account(10.50)
    assert account.deposit(10.50) == 10.50

# test cases withdraw method:


def test_withdraw_ten():
    """Account name Jill withdraws 20 from account """
    account = Account(name="Jill", balance=1000)
    account.withdraw(20)
    assert account.balance == 980


def test_withdraw_fourty():
    """Account name Jill withdraw 40 from account """
    account = Account(name="Jill", balance=980)
    account.withdraw(40)
    assert account.balance == 940


def test_withdraw_insuffient_amount():
    """Account name Jill withdraw 100 from account """
    account = Account(0)
    with pytest.raises(InsufficientAmount):
        account.withdraw(100)
