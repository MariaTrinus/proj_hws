""" Лекція 19. DataKit """

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print(f"\n=======================| Task 1 |=======================")

#       Numpy
#   a. Create an array with shape (4, 3) of:
#       a. all zeros
#       b. ones
#       c. numbers from 0 to 11
#   b. Tabulate the following function:F(x)=2x^2+5,x∈[1,100] with step 1.
#   c. Tabulate the following function:F(x)=e^−x,x∈[−10,10] with step 1.

print(f" Array of all zeros: \n{np.zeros((4, 3))} \n")
print(f" Array of all ones: \n{np.ones((4, 3))} \n")
print(f" Array of numbers from 0 to 11: \n{np.arange(12).reshape((4, 3))} \n")

print(f" Tabulated function F(x) = 2x^2 + 5, x∈[1, 100]: "
      f"\n{2 * np.arange(1, 101) ** 2 + 5}\n")

print(f" Tabulated function F(x) = e^(-x), x∈[-10, 10]: "
      f"\n{np.exp(-np.arange(-10, 11))}")

print(f"\n=======================| Task 2 |=======================")

#       Pandas
#   a. Import the dataset from this address and assign it to df variable.
#   b. Select only the Team, Yellow Cards and Red Cards columns.
#   c. How many teams participated in the Euro2012?
#   d. Filter teams that scored more than 6 goals

file_path = "Euro_2012_stats_TEAM.csv"
df = pd.read_csv(file_path)

print(f" Selected columns: "
      f"\n{df[['Team', 'Yellow Cards', 'Red Cards']]}")

print(f" Number of teams participated in Euro2012: "
      f"\n{df['Team'].nunique()}")

print(f" Teams that scored more than 6 goals: "
      f"\n{df[df['Goals'] > 6]}")

print(f"\n=======================| Task 3 |=======================")

#       DataViz
#   Choose a dataset, you can use Seaborn.
#   Create a cheat sheet for yourself containing all plot types discussed in the lecture.
#   Provide the following info:
#         - Plot type
#         - Use cases (categorical data, distribution, etc.)
#         - Example on the dataset

titanic = sns.load_dataset("titanic")

# Scatter Plot
sns.scatterplot(x="age", y="fare", data=titanic)
plt.title("Scatter Plot: Age vs Fare")
plt.show()

# Histogram	      Display distribution of a single numerical variable
sns.histplot(x="age", data=titanic)
plt.title('Histogram: Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot	      Show distribution and identify outliers in numerical data
sns.boxplot(x="survived", y="age", data=titanic)
plt.title('Box Plot: Age Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.show()

# Violin Plot	  Combine box plot with kernel density estimation for better insights
sns.violinplot(x="class", y="age", data=titanic)
plt.title('Violin Plot: Age Distribution by Class')
plt.xlabel('Class')
plt.ylabel('Age')
plt.show()

# Bar Plot	      Compare categorical variables
sns.barplot(x="class", y="fare", data=titanic)
plt.title('Bar Plot: Fare by Class')
plt.xlabel('Class')
plt.ylabel('Fare')
plt.show()

# Count Plot	  Show count of observations in each category
sns.countplot(x="sex", data=titanic)
plt.title('Count Plot: Passengers by Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
