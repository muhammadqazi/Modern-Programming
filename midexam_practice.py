import random
#  Write and test a program that computes the area of a circle. This program should
# request a number representing a radius as input from the user. It should use the formula
# 3.14 * radius ** 2 to compute the area and then output this result suitably labeled.

def area_of_circle(radius):
    area = 3.14 * radius ** 2
    print("The area of the circle is: ", area)

# An object’s momentum is its mass multiplied by its velocity. Write a program
# that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
# inputs and then outputs its momentum. And kinetic energy is the sum of the
# product of the mass and the velocity squared.


def kinetic_energy(mass, velocity):
    momentum = mass * velocity
    print("The momentum is: ", momentum)
    kinetic_energy = 1/2 * mass * velocity ** 2
    print("The kinetic energy is: ", kinetic_energy)


# Light travels at 3 *108
# meters per second. A light-year is the distance a light beam
# travels in one year. Write a program that calculates and displays the value of a
# light-year.

def light_year():
    light_speed = 3 * 10 ** 8
    light_year = light_speed * 365 * 24 * 60 * 60
    print("The light year is: ", (light_year/1000), "km")


# Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
# • A kilometer represents 1/10,000 of the distance between the North Pole and
# the equator.
# • There are 90 degrees, containing 60 minutes of arc each, between the North
# Pole and the equator.
# • A nautical mile is 1 minute of an arc.

def nautical_miles(kilometers):
    degreesPerMin = 90*60

    onekilo = degreesPerMin/10000

    nauticalmile = onekilo*kilometers

    print(kilometers, "is", nauticalmile, "Nautical miles")



# An employee’s total weekly pay equals the hourly wage multiplied by the total
# number of regular hours plus any overtime pay. Overtime pay equals the total
# overtime hours multiplied by 1.5 times the hourly wage. Write a program that
# takes as inputs the hourly wage, total regular hours, and total overtime hours and
# displays an employee’s total weekly pay

def weekly_pay(hourly_wage, regular_hours, overtime_hours):
    regular_pay = hourly_wage * regular_hours
    overtime_pay = hourly_wage * 1.5 * overtime_hours
    total_pay = regular_pay + overtime_pay
    print("Your total weekly pay is: ", total_pay)


# The German mathematician Gottfried Leibniz developed the following method
# to approximate the value of π:
# π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
# Write a program that allows the user to specify the number of iterations used in
# this approximation and that displays the resulting value.

def pi_approximation(iterations):
    pi = 0
    for i in range(iterations):
        if i % 2 == 0:
            pi += 1/((2*i)+1)
        else:
            pi -= 1/((2*i)+1)
    print("The value of pi is: ", pi*4)

# Teachers in most school districts are paid on a schedule that provides a salary
# based on their number of years of teaching experience. For example, a beginning
# teacher in the Lexington School District might be paid $30,000 the first year. For
# each year of experience after this first year, up to 10 years, the teacher receives a
# 2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting
# salary, the percentage increase, and the number of years in the schedule. Each row
# in the schedule should contain the year number and the salary for that year.

def salary_schedule(starting_salary, increase, years):
    salary = starting_salary
    for i in range(years):
        if i == 0:
            print(i+1, salary)
        else:
            # 2% increase
            salary = salary + ((increase/salary)* 100)
            print(i+1, salary)

# Write a program that receives a series of numbers from the user and allows the
# user to press the enter key to indicate that he or she is finished providing inputs.
# After the user presses the enter key, the program should print the sum of the
# numbers and their average.


def sum_and_average():
    sum = 0
    count = 0
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            sum += int(number)
            count += 1
    print("The sum is: ", sum)
    print("The average is: ", sum/count)

# In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,
# the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so
# on. A little mathematical analysis reveals that there are not enough ways to win
# to make the game worthwhile; however, because many people’s eyes glaze over
# at the first mention of mathematics, your challenge is to write a program that
# demonstrates the futility of playing the game. Your program should take as input
# the amount of money that the player wants to put into the pot, and play the game
# until the pot is empty. At that point, the program should print the number of
# rolls it took to break the player, as well as maximum amount of money in the pot.

def lucky_sevens(money):
    count = 0
    while money > 0:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum = dice1 + dice2
        if sum == 7:
            money += 4
        else:
            money -= 1
        count += 1
    print("The number of rolls is: ", count)
    print("The maximum amount of money in the pot is: ", money)


def main():

    # 1
    radius = int(input("Enter a radius: "))
    area_of_circle(radius)

    # 2
    mass = int(input("Enter a mass: "))
    velocity = int(input("Enter a velocity: "))
    kinetic_energy(mass, velocity)

    # 3
    light_year()

    # 4
    kilometers = int(input("Enter a number of kilometers: "))
    nautical_miles(kilometers)

    # 5
    hourly_wage = int(input("Enter your hourly wage: "))
    regular_hours = int(input("Enter your regular hours: "))
    overtime_hours = int(input("Enter your overtime hours: "))
    weekly_pay(hourly_wage, regular_hours, overtime_hours)

    # 6
    iterations = int(input("Enter the number of iterations: "))
    pi_approximation(iterations)

    # 7
    starting_salary = int(input("Enter your starting salary: "))
    increase = float(input("Enter your percentage increase: "))
    years = int(input("Enter the number of years: "))
    salary_schedule(starting_salary, increase, years)

    # 8
    sum_and_average()



if __name__ == "__main__":
    main()
