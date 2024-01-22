""" Write a program that
    gets two int variables
    and swaps their values.
    Do it in 3 different ways."""

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
