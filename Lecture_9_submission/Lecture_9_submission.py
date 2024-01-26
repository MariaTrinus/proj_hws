""" Лекція 9. Modules """

print(f"\n=======================| Task 1 |=======================")

#   Create a file called hello.py
#       that contains a single function hello().
#   This function should accept a
#       single string parameter name
#       print the text
#           Hello {name}!
#       to the interactive window with {name}
#       replaced with the function argument.
#   Add a file called main.py
#       that imports the hello() function from hello.py
#       and calls the function with your name.


print(f"\n=======================| Task 2 |=======================")

#   Install the custom library
#   1. Create a virtual environment
#   2. Install numpy package in the virtual environment (version 1.22.4 or higher, but lower than 2.0.0)
#   3. Generate a requirements.txt file
#   4. Write a script that imports numpy.
#       Execute code from their site (https://numpy.org/)
#       and run it on a local computer
#   5. As a result, you should
#       send a screenshot of the executed code on your machine,
#       requirements.txt
#       and a .py file

# The standard way to import NumPy:
import numpy as np

# Create a 2-D array, set every second element in
# some rows and find max per row:

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
print(f" {x}")
# array([[  0,   1,   2,   3,   4],
#        [-99,   6, -99,   8, -99],
#        [-99,  11, -99,  13, -99]])

print(f" {x.max(axis=1)}")
# array([ 4,  8, 13])

# Generate normally distributed random numbers:
rng = np.random.default_rng()
samples = rng.normal(size=2500)
print(f" {samples}")

