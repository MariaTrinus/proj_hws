""" Лекція 10. Context Manager. Files """

from random import randint
from csv import writer, reader

print(f"\n=======================| Task 1 |=======================")


#   Write a program that
#       generates 26 text files
#           named A.txt, B.txt, and so on up to Z.txt.
#       To each file append a random number
#           between 1 and 100.
#   Create a summary file (summary.txt)
#       that contains the name of the file and the number in that file:
#   A.txt: 67
#   B.txt: 12
#   ...
#   Z.txt: 98

def write_to_file(file_name: str, input_data: str):
    file_name_txt = file_name + '.txt'
    with open(file_name_txt, 'w') as file:
        file.write(input_data)


def add_to_file(file_name: int, input_data: str):
    file_name = chr(file_name)
    with open("summary.txt", 'a') as file:
        file.write(file_name + ".txt: " + input_data + "\n")


def read_from_file(file_name: str) -> str:
    """
    Read number from file
    :param file_name: file name without extension
    :return: data from file
    """
    data_in_file = 0
    file_name_txt = file_name + '.txt'

    with open(file_name_txt, 'r') as file:
        data_in_file = file.read()

    return data_in_file


def generates_files() -> None:
    """
    Generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
    To each file append a random number between 1 and 100.
    :return: None
    """
    start = ord("A")
    end = ord("Z")

    for name_ord in range(start, end + 1):
        write_to_file(chr(name_ord), str(randint(1, 100)))


def create_a_summary_file():
    start = ord("A")
    end = ord("Z")

    with open("summary.txt", 'w') as file:
        file.write("")

    for name_ord in range(start, end + 1):
        number_from_file = read_from_file(chr(name_ord))
        add_to_file(name_ord, number_from_file)


generates_files()
create_a_summary_file()

print(f" You can open file 'summary.txt' and check the result )")

print(f"\n=======================| Task 2 |=======================")

#   Create a file with some content.
#   Create a second file
#       and copy the content of the first file
#       to the second file
#       in upper case.

file_content = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
                "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
                "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
                "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                "culpa qui officia deserunt mollit anim id est laborum.")


def create_a_file(file_name: str, input_data: str):
    with open(file_name, 'w') as file:
        file.write(input_data)


create_a_file("lower_case.txt", file_content)
upper_case_file_content = read_from_file("lower_case").upper()
create_a_file("upper_case.txt", upper_case_file_content)

print(f" You can open file 'upper_case.txt' and check the result )")

print(f"\n=======================| Task 3 |=======================")

#   Write a program
#       that will simulate user scores in a game.
#   Create a list with 5 players’ names
#       after that simulate 100 rounds for each player.
#   As a result of the game create a list
#       with the player's name and score (0-1000 range).
#   And save it to a CSV file.

#   The file should look like this:
#   Player name, Score
#   Josh, 56
#   Luke, 784
#   Kate, 90
#   Mark, 125
#   Mary, 877
#   Josh, 345
#   ...

players_names = ["Josh", "Luke", "Kate", "Mark", "Mary"]


def game_result_generation(names: list, rounds: int, max_score_range: int) -> list:
    names_and_scores = []
    for round_ in range(rounds):
        for name in names:
            names_and_scores.append([name, randint(0, max_score_range)])
    return names_and_scores


def write_to_csv(file_name: str, data: list, csv_header: list):
    create_a_file(file_name, "")
    with open(file_name, 'w') as file:
        csv_writer = writer(file)
        csv_writer.writerow(csv_header)
        for line in data:
            csv_writer.writerow(line)


game_result = game_result_generation(players_names, 100, 1000)
write_to_csv("name_and_score.csv", game_result, ["Player name", "Score"])

print(f" You can open file 'name_and_score.csv' and check the result )")

print(f"\n=======================| Task 4 |=======================")


#   Write a script
#       that reads the data from the previous CSV file
#       and creates a new file called high_scores.csv
#           where each row contains the player name and their highest score.
#   The final score
#       should be sorted by descending to the highest score.

#   The output CSV file should look like this:
#   Player name, Highest score
#   Kate, 907
#   Mary, 897
#   Luke, 784
#   Mark, 725
#   Josh, 345

def read_from_csv(file_name: str) -> list:
    name_and_score = []
    with open(file_name, mode='r') as file:
        read = reader(file)
        name_and_score += read
    return name_and_score


def highest_score(names: list, name_and_score: list):
    """
    Finds and records the highest scores of each player in a csv file
    :param names: list of players` names
    :param name_and_score: list of names and their score
    :return: None
    """
    name_and_highest_score = []

    for name in names:
        max_score = 0

        for i in range(len(name_and_score)):
            # print(f" {name_and_score[i] = }")
            if name_and_score[i] != [] and name_and_score[i][0] == name and int(name_and_score[i][1]) > max_score:
                max_score = int(name_and_score[i][1])
        name_and_highest_score.append([name, max_score])

    write_to_csv('name_and_highest_score.csv', name_and_highest_score, ["Player name", "Highest score"])


highest_score(players_names, read_from_csv("name_and_score.csv"))
print(f" You can open file 'name_and_highest_score.csv' and check the result )")
