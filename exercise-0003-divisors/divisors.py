"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

Date: 13.11.2019
"""



def main():
    number = input("Please enter a number: ")
    print(find_divisors(number))


def find_divisors(number):
    divisors = []
    for i in range(1, int(number)+1):
        if int(number) % i == 0:
            divisors.append(i)
    return divisors
