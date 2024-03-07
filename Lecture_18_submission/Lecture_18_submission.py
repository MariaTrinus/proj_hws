""" Лекція 18. Testing """
import unittest

print(f"\n=======================| Task 0 |=======================")


#   From lesson 14 for testing:

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        self._balance += self._balance * self.interest


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        self.accounts = [acc for acc in self.accounts if acc.get_account_number() != account_number]

    def pay_dividend(self, dividend):
        for account in self.accounts:
            account.deposit(dividend)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.get_balance() < 0:
                print(f" Letter sent to account {account.get_account_number()}: You are in overdraft!")


bank = Bank()

savings_acc = SavingsAccount(0, 'SA001', 0.03)
savings_acc.deposit(1000)
savings_acc_with_interest = SavingsAccount(1000, 'SA002', 0.05)
current_acc = CurrentAccount(0, 'CA001', 500)

bank.open_account(savings_acc)
bank.open_account(savings_acc_with_interest)
bank.open_account(current_acc)

bank.update()

print(f"{'Account number'.ljust(15)} {'Balance':<15}")
for account in bank.accounts:
    print(f"{account.get_account_number().ljust(15)} {account.get_balance():<15.2f}")

bank.pay_dividend(50)

print(f"\n{'Account number'.ljust(15)} {'Balance':<15}")
for account in bank.accounts:
    print(f"{account.get_account_number().ljust(15)} {account.get_balance():<15.2f}")

print(f"\n=======================| Task 1 |=======================")

#   Write a test for the Bank class that we wrote in 14 lesson.
#       You should write a test for the open_account method.
#       Ensure that the account is opened and has balance.

print(f"\n=======================| Task 2 |=======================")


#   Test update method.
#       It should check that code added interest
#       and sent a message (print function was called).


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        initial_balance = 1000
        savings_acc = SavingsAccount(initial_balance, 'SA001', 0.03)
        self.bank.open_account(savings_acc)
        self.assertIn(savings_acc, self.bank.accounts)
        self.assertEqual(savings_acc.get_balance(), initial_balance)
        print("Test for opening account passed.")

    def test_update(self):
        initial_balance = 1000
        interest_rate = 0.03
        savings_acc = SavingsAccount(initial_balance, 'SA001', interest_rate)
        self.bank.open_account(savings_acc)

        self.bank.update()

        # Check if interest was added
        expected_balance_with_interest = initial_balance * (1 + interest_rate)
        self.assertEqual(savings_acc.get_balance(), expected_balance_with_interest)

        # Check if message was sent for savings account
        with self.assertLogs() as cm:
            self.bank.update()
            self.assertIn(f" Letter sent to account {savings_acc.get_account_number()}: You are in overdraft!",
                          cm.output)
        print("Test for update passed.")


if __name__ == "__main__":
    unittest.main()
