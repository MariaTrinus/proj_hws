""" Лекція 14. OOP. Inheritance """

print(f"\n=======================| Task 1 |=======================")


#   Create a class Product with properties name, price, and quantity.
#   Create a child class Book
#       that inherits from Product
#       and adds a property author
#       and a method called read
#           that prints information about the book.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price} UAH")
        print(f"Quantity: {self.quantity}")


book1 = Book("The Kobzar", 1000, 100, "Taras Shevchenko")
book1.read()

print(f"\n=======================| Task 2 |=======================")


#   Create a class Restaurant with properties
#       name
#       cuisine
#       menu
#   The menu property should be a dictionary
#       with keys being the dish name
#       and values being the price.
#   Create a child class FastFood that inherits from Restaurant
#       and adds a property drive_thru
#           (a boolean indicating whether the restaurant has a drive-thru or not)
#       and a method called order,
#           which takes in the dish name and quantity
#           and returns the total cost of the order.
#       The method should also update the menu dictionary to subtract the ordered quantity from the available quantity.
#       If the dish is not available or if the requested quantity is greater than the available quantity,
#           the method should return a message indicating that the order cannot be fulfilled.
#   Example of usage:

#   class Restaurant:
#     # your code here
#     pass
#
#   class FastFood(Restaurant):
#     # your code here
#     pass
#
#   menu =  {
#     'burger': {'price': 5, 'quantity': 10},
#     'pizza': {'price': 10, 'quantity': 20},
#     'drink': {'price': 1, 'quantity': 15}
# }
#
#   mc = FastFood('McDonalds', 'Fast Food', menu, True)
#
#   print(mc.order('burger', 5)) # 25
#   print(mc.order('burger', 15)) # Requested quantity not available
#   print(mc.order('soup', 5)) # Dish not available


class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu and self.menu[dish_name]['quantity'] >= quantity:
            total_cost = self.menu[dish_name]['price'] * quantity
            self.menu[dish_name]['quantity'] -= quantity
            return total_cost
        elif dish_name not in self.menu:
            return "Dish not available"
        else:
            return "Requested quantity not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

# 25
print(f"{mc.order('burger', 5) = }")
# Requested quantity not available
print(f"{mc.order('burger', 15) = }")
# Dish not available
print(f"{mc.order('soup', 5) = }")

print(f"\n=======================| Task 3 |=======================")


#       A Bank
#   1.  Using the Account class as a base class,
#           write two derived classes called SavingsAccount and CurrentAccount.
#       A SavingsAccount object, in addition to the attributes of an Account object,
#           should have an interest attribute
#           and a method which adds interest to the account.
#       A CurrentAccount object, in addition to the attributes of an Account object,
#           should have an overdraft limit attribute.
#   2.  Now create a Bank class, an object of which contains
#           an array of Account objects.
#       Accounts in the array could be instances of
#           the Account class,
#           the SavingsAccount class,
#           or the CurrentAccount class.
#       Create some test accounts (some of each type).
#   3.  Write an update method in the Bank class.
#       It iterates through each account, updating it in the following ways:
#           Savings accounts get interest added (via the method you already wrote);
#           CurrentAccounts get a letter sent if they are in overdraft.
#           (use print to 'send' the letter).
#   4.  The Bank class requires methods
#           for opening and closing accounts,
#           and for paying a dividend into each account.


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
