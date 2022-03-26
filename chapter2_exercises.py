# 1) Program to show number is even or odd

def even_or_odd(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

# 2) Pyramid of stars

# not correct working on it
def pyramid_stars():
    for i in range(1, 6):
        print(" * " * i)


# 3) Program to print all the divisors of a number

def divisors(number):
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

# 4) check if input number is a prime number

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# 5) Program to print the factorial of a number

def factorial(number):
    fact = 1
    if number == 1:
        return 1
    else:
        for i in range(1, number+1):
            fact = fact * i
        return fact
        


def main():

    # 1
    number = int(input("Enter a number: "))
    even_or_odd(number)

    # 2
    pyramid_stars()

    # 3
    number = int(input("Enter a number: "))
    divisors(number)

    # 4
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("Number is prime")
    else:
        print("Number is not prime")

    # 5
    number = int(input("Enter a number: "))
    print(factorial(number))


if __name__ == "__main__":
    main()
