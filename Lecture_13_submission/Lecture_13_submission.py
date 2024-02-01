""" Лекція 13. OOP. Class """

print(f"\n=======================| Task 1 |=======================")


#   Create add method to add two countries together.
#   This method should
#       create another country object
#           with the name of the two countries combined
#       and the population of the
#           two countries added together.

#   bosnia = Country('Bosnia', 10_000_000)
#   herzegovina = Country('Herzegovina', 5_000_000)
#
#   bosnia_herzegovina = bosnia.add(herzegovina)
#   bosnia_herzegovina.population -> 15_000_000
#   bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = self.name + " " + other_country.name
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(f" {bosnia_herzegovina.population  = }")
print(f" {bosnia_herzegovina.name        = }")

print(f"\n=======================| Task 2 |=======================")


#   Implement the previous method with a magic method

#   bosnia = Country('Bosnia', 10_000_000)
#   herzegovina = Country('Herzegovina', 5_000_000)
#
#   bosnia_herzegovina = bosnia + herzegovina
#   bosnia_herzegovina.population -> 15_000_000
#   bosnia_herzegovina.name -> 'Bosnia Herzegovina'

#   To make this code working, comment the previous class Country

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = self.name + " " + other_country.name
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(f" {bosnia_herzegovina.population  = }")
print(f" {bosnia_herzegovina.name        = }")

print(f"\n=======================| Task 3 |=======================")


#   Create a Car class with the following attributes:
#       brand
#       model
#       year
#       speed
#   The Car class should have the following methods:
#       accelerate
#       brake
#       display_speed
#   The accelerate method should increase the speed by 5,
#       and the brake method should decrease the speed by 5.
#   Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        print("Current speed:", self.speed)


car = Car("Toyota", "Tundra", 2024)

car.accelerate()
car.display_speed()

car.brake()
car.display_speed()

print(f"\n=======================| Task 4 |=======================")


#   Create a Robot class with the following attributes:
#       orientation (left, right, up, down)
#       position_x
#       position_y
#   The Robot class should have the following methods:
#       move
#       turn
#       display_position
#   The move method should
#       take a number of steps
#       and move the robot in the direction it is currently facing.
#   The turn method should
#       take a direction (left or right)
#       and turn the robot in that direction.
#   The display_position method should print the current position of the robot.

class Robot:
    def __init__(self, orientation, position_x=0, position_y=0):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        match self.orientation:
            case "left":
                self.position_x -= steps
            case "right":
                self.position_x += steps
            case "up":
                self.position_y += steps
            case "down":
                self.position_y -= steps

    def turn(self, direction):
        match direction:
            case "left":
                match self.orientation:
                    case "left":
                        self.orientation = "down"
                    case "right":
                        self.orientation = "up"
                    case "up":
                        self.orientation = "left"
                    case "down":
                        self.orientation = "right"
            case "right":
                match self.orientation:
                    case "left":
                        self.orientation = "up"
                    case "right":
                        self.orientation = "down"
                    case "up":
                        self.orientation = "right"
                    case "down":
                        self.orientation = "left"

    def display_position(self):
        print(f" Current position: ({self.position_x}, {self.position_y})")


robot = Robot("right")

robot.move(3)
robot.display_position()

robot.turn("left")
robot.move(2)
robot.display_position()
