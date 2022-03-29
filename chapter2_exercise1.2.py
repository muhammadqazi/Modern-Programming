import random

# 1) Program to print numbers pyramid

def pyramid_numbers():

    for i in range(6, 0, -1):
        for j in range(1, i):
            print(j, end=" ")

        print("\n")

# 2) Display digits of a number


def display_digits(number):

    x = number
    while x != 0:
        print(x % 10, end=" ")
        x = int(x/10)
    print("\n")

# 3 Calculate and display the net salary of an employee


def net_salary(salary):

    if salary < 0:
        print("Invalid salary")
    if salary < 1000:
        # tax 5% and 5% fund = 10%
        tax = salary * 0.05
        fund = salary * 0.1
        net_salary = salary - tax - fund
        print("Your net salary is: $", net_salary)
    elif salary >= 1000 or salary < 3000:
        # tax 10% and 15% fund = 25%
        tax = salary * 0.1
        fund = salary * 0.15
        net_salary = salary - tax - fund
        print("Your net salary is: $", net_salary)
    elif salary >= 3000 or salary < 5000:
        # tax 15% and 15% fund = 30%
        tax = salary * 0.15
        fund = salary * 0.15
        net_salary = salary - tax - fund
        print("Your net salary is: $", net_salary)
    else:
        # 20% tax and fund
        tax = salary * 0.2
        fund = salary * 0.2
        net_salary = salary - tax - fund
        print("Your net salary is: $", net_salary)

# 3 Reverse a word


def reverse_word(word):

    word = word[::-1]
    print(word)

# 4 Display vovels and consonants in a word


def display_vowels_consonants(word):

    vovels = 0
    consonants = 0

    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            vovels += 1
            print("Vovels : ", i)

        else:
            print()
            consonants += 1
            print("Consonants : ", i)
    
    print("Total vovels : " + str(vovels))
    print("Total consonants : " + str(consonants))


# Number guessing game

def number_guessing_game():

    number = random.randint(1, 20)
    guess = int(input("Guess a number between 1 and 20: "))

    while guess != number:
        if guess < number:
            print("Too low")
        else:
            print("Too high")
        guess = int(input("Guess again: "))

    print("You guessed it!")


def main():

    # 1
    pyramid_numbers()

    # 2
    number = int(input("Enter a number: "))
    display_digits(number)

    # 3
    salary = int(input("Enter your salary: "))
    net_salary(salary)

    # 4
    word = input("Enter a word: ")
    reverse_word(word)

    # 5
    word = input("Enter a word: ")
    display_vowels_consonants(word)

    # 6
    number_guessing_game()


if __name__ == "__main__":
    main()
