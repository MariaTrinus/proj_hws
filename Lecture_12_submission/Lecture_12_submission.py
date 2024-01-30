""" Лекція 12. Decorator """

import time

print(f"\n=======================| Task 1 |=======================")


#   Write a decorator that ensures a function is only called by users with a specific role.
#   Each function should have a user_type with a string type in kwargs.
#
#   Example:
#   @is_admin
#   def show_customer_receipt(user_type: str):
#     # Some very dangerous operation
#
#   show_customer_receipt(user_type='user')
#   > ValueError: Permission denied
#
#   show_customer_receipt(user_type='admin')
#   > function pass as it should be

def is_admin(func):
    def wrapper(**kwargs):
        user_type = kwargs.get('user_type')
        if user_type == 'admin':
            return func(**kwargs)
        else:
            raise ValueError(" Permission denied")

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print(f" Some very dangerous operations was done) have a nice day) ")


def main_1():
    try:
        show_customer_receipt(user_type='user')
    except ValueError as e:
        print(e)

    try:
        show_customer_receipt(user_type='admin')
    except ValueError as e:
        print(e)


main_1()

print(f"\n=======================| Task 2 |=======================")


#   Write a decorator
#       that wraps a function in a try-except block
#       and prints an error if any type of error has happened.

#   Example:
#   @catch_errors
#   def some_function_with_risky_operation(data):
#     print(data['key'])
#
#   some_function_with_risky_operation({'foo': 'bar'})
#   > Found 1 error during execution of your function: KeyError no such key as foo
#
#   some_function_with_risky_operation({'key': 'bar'})
#   > bar

def catch_errors(func):
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as e:

            print(
                f" Found 1 error during execution of your function: {type(e).__name__} no such key as '{list(args[0].keys())[0]}'")

    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(f" {data['key']}")


def main_2():
    some_function_with_risky_operation({'foo': 'bar'})
    some_function_with_risky_operation({'key': 'bar'})


main_2()

print(f"\n=======================| Task 3 |=======================")


#   Create a decorator that will check types.
#       It should take a function with arguments and validate inputs with annotations.
#       It should work for all possible functions.
#       Don`t forget to check the return type as well
#
#   Example:
#   @check_types
#   def add(a: int, b: int) -> int:
#     return a + b
#
#   add(1, 2)
#   > 3
#
#   add("1", "2")
#   > TypeError: Argument a must be int, not str

def check_types(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        # Перевірка типів вхідних аргументів
        for i, arg in enumerate(args):
            if annotations and list(annotations.values())[i] != type(arg):
                raise TypeError(
                    f" Argument {arg} must be {list(annotations.values())[i].__name__}, not {type(arg).__name__}")

        # Виклик функції
        result = func(*args, **kwargs)

        # Перевірка типу поверненого значення
        if 'return' in annotations and annotations['return'] != type(result):
            raise TypeError(
                f" The returned value must be {annotations['return'].__name__}, not {type(result).__name__}")

        return result

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


def main_3():
    try:
        print(f" {add(1, 2)}")
    except TypeError as e:
        print(e)

    try:
        print(f" {add("1", "2")}")
    except TypeError as e:
        print(e)


main_3()
print(f"\n=======================| Task 4 |=======================")


#   Create a function
#       that caches the result of a function,
#       so that if it is called with the same argument multiple times,
#       it returns the cached result first instead of re-executing the function.

def caches_the_results(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f" This result is in cash!)\t\t\t", end="")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


@caches_the_results
def subtract(a, b):
    print("\n Performing the subtraction function")
    return a - b


def main_4():
    print(f" {subtract(5, 3) = }")
    print(f" {subtract(5, 3) = }")

    print(f" {subtract(8, 4) = }")
    print(f" {subtract(8, 4) = }")

    print(f" {subtract(5, 3) = }")


main_4()

print(f"\n=======================| Task 5 |=======================")


#   Write a decorator
#       that adds a rate-limiter to a function,
#       so that it can only be called a certain amount of times per minute


# I use "import time" for this task


def rate_limiter(max_calls, period):
    def decorator(func):
        calls = []

        def wrapper(*args, **kwargs):
            current_time = time.time()
            calls[:] = [call for call in calls if current_time - call < period]

            if len(calls) < max_calls:
                calls.append(current_time)
                return func(*args, **kwargs)
            else:
                raise Exception(f" The function can only be called {max_calls} times per minute! ")

        return wrapper

    return decorator


@rate_limiter(max_calls=2, period=60)
def some_function():
    print(f" Calling a function")


def main_5():
    try:
        some_function()
        some_function()
        some_function()
    except Exception as e:
        print(e)


main_5()
