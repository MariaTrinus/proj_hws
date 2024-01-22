"""     Write a program that gets 2 numbers from the user.
    Print to the console maximum of these two variable.
    Use a built-in function for that.

    Enter the first digit: 75
    Enter the second digit: 34
    The maximum is: 75
    """

number_1 = int(input(" Enter the first digit: \t"))
number_2 = int(input(" Enter the second digit: \t"))

print(f" The maximum is: \t\t\t{max(number_1, number_2)}")
