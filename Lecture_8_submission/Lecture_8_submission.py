""" Лекція 8. Complexity. Algorithms """
#   The complexity of my algorithm
#       is O(n^2)
#   cause it contains 2 loops inside each other

import random

print(f"\n=======================| Task 1 |=======================")


#   You have 100 cats.

#   One day you decide to arrange all your cats in a giant circle.
#   Initially,
#       none of your cats have any hats on.
#   You walk around the circle 100 times,
#       always starting at the same spot, with the first cat (cat # 1).
#   Every time you stop at a cat,
#       you either put a hat on it
#           if it doesn't have one on,
#       or you take its hat off
#           if it has one on.

#   - In The first round, you stop at every cat, placing a hat on each one.
#   - In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
#   - In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
#   - You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).

#   Write a program that simply outputs which cats have hats at the end.
#   Optional: Make a function that can calculate hats with any amount of rounds and cats.

def cats_have_hats(cats_number: int, rounds_number: int) -> list:
    cats_list = [0 for i in range(cats_number)]
    for i in range(rounds_number):
        for j in range(cats_number):
            if (j + 1) % (i + 1) == 0:
                cats_list[j] = 1 if cats_list[j] == 0 else 0
    return cats_list


cats_nb = 100
rounds_nb = 100

cats_with_hat = cats_have_hats(cats_nb, rounds_nb)

for i in range(len(cats_with_hat)):
    if cats_with_hat[i] == 0:
        print(f" cat № {i + 1} has hat")
