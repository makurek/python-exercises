"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

Date: 13.11.2019

"""

# Solution 1 with reverse loop

def isPalindrome(str):

    rev = []
    for i in range(len(str), 0, -1):
        rev.append(str[i-1])
    n = ''.join(rev)
    if str == n:
        return "yes"
    else:
        return "no"

# Solution 2
# is x mutable?

def isPalindrome2(str):

    x = ''
    for i in range(0, len(str)):
        x += str[len(str) - i - 1]
    print (x)


def main():

    str = input("Please enter a string: ")
    print(isPalindrome2(str))


main()
