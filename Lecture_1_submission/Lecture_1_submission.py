""" Лекція 1. Вступ до змінних та вбудованих функцій Python"""

print(f"\n=======================| Task 1.1 |=======================")
#       Write a program that
#     gets two int variables
#     and swaps their values.
#     Do it in 3 different ways.


# Actually, there is much more ways to swap values, so I group them in 2 types:
# 1) work with id (1st and 2nd ways)
# 2) work with values (3rd way)


print(" Before: ")
# a = int(input(" Enter 1-st variable: "))
# b = int(input(" Enter 1-st variable: "))
a = 3
b = 5
print(f" {a=} \t\t {b=} \n {id(a)=} \n {id(b)=}\n")

# 1st way: use 3rd variable to keep the result:
print(" After 1st: ")
c = a
a = b
b = c
print(f" {a=} \t\t {b=} \n {id(a)=} \n {id(b)=}\n")

# 2nd way: use tuples (use it always, let me know if it`s not OK):
print(" After 2nd: ")
a, b = b, a
print(f" {a=} \t\t {b=} \n {id(a)=} \n {id(b)=}\n")

# 3rd way: use math (at previous ways we work with id. Now let`s work with meanings):
print(" After 3rd: ")
a = b + a  # now a = b + a, b = b
b = a - b  # now a = b + a, b = a - b = b + a - b = a
a = a - b  # now a = b + a - a = b, b = a

print(f" {a=} \t\t {b=} \n {id(a)=} \n {id(b)=}\n")

print(f"\n=======================| Task 1.2 |=======================")
#       Write a program that gets 2 numbers from the user.
#     Print to the console their difference.
#     Use the built-in Input function for that
#
#     Enter the first digit: 5
#     Enter the second digit: 3
#     The difference is: 2


number_1 = int(input(" Enter the first digit: \t"))
number_2 = int(input(" Enter the second digit: \t"))

print(f" The difference is: \t\t{number_1 - number_2}")

print(f"\n=======================| Task 1.3 |=======================")
#       Write a program that gets 2 numbers from the user.
#     Print to the console maximum of these two variable.
#     Use a built-in function for that.
#
#     Enter the first digit: 75
#     Enter the second digit: 34
#     The maximum is: 75


number_1 = int(input(" Enter the first digit: \t"))
number_2 = int(input(" Enter the second digit: \t"))

print(f" The maximum is: \t\t\t{max(number_1, number_2)}")

print(f"\n=======================| Task 1.4 |=======================")
#       Optional: Write a program that gets 3-digit number from the user and reverses it.
#     You can use only numbers and their operators.
#     Don`t use a string here!
#
#     Enter the initial number: 123
#     The reverse number is: 321


inp_number = int(input(" Enter the initial number: \t"))
# inp_number = 123  # data for testing

n_3 = inp_number % 10
n_2 = (inp_number // 10) % 10
n_1 = inp_number // 100

# print(f" {n_1 = } \n {n_2 = } \n {n_3 = }")   # output for testing

reversed_number = n_3 * 100 + n_2 * 10 + n_1

print(f" The reverse number is: \t{reversed_number}")
