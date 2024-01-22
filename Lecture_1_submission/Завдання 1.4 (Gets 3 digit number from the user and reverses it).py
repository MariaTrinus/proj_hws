"""     Optional: Write a program that gets 3-digit number from the user and reverses it.
    You can use only numbers and their operators.
    Don`t use a string here!

    Enter the initial number: 123
    The reverse number is: 321
    """

inp_number = int(input(" Enter the initial number: \t"))
# inp_number = 123  # data for testing

n_3 = inp_number % 10
n_2 = (inp_number // 10) % 10
n_1 = inp_number // 100

# print(f" {n_1 = } \n {n_2 = } \n {n_3 = }")   # output for testing

reversed_number = n_3 * 100 + n_2 * 10 + n_1

print(f" The reverse number is: \t{reversed_number}")
