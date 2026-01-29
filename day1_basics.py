# ============================================
# Day 1: Basics, Conditions & Simple Loops
# ============================================


# --------------------------------------------
# Question 1:
# Take a number from the user and check
# whether it is Even or Odd.
#
# Learning:
# - input()
# - int conversion
# - if-else condition
# --------------------------------------------

def even_or_odd():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# even_or_odd()


# --------------------------------------------
# Question 2:
# Take two numbers from the user and
# print which number is greater.
# If both are equal, print that they are equal.
#
# Learning:
# - if / elif / else
# - comparison operators
# --------------------------------------------

def compare_two_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2:
        print("First number is greater")
    elif num1 < num2:
        print("Second number is greater")
    else:
        print("Both are equal")


# compare_two_numbers()


# --------------------------------------------
# Question 3:
# Take a number n from the user and print
# numbers from 1 to n.
# If a number is divisible by 3, print "Fizz"
# instead of the number.
#
# Learning:
# - for loop
# - range()
# - modulo operator
# --------------------------------------------

def fizz_problem():
    n = int(input("Enter a number: "))

    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)


# fizz_problem()


# --------------------------------------------
# Question 4:
# Take a number n from the user.
# Print all even numbers less than n
# and also count how many even numbers exist.
#
# Learning:
# - loop with condition
# - counter variable
# --------------------------------------------

def count_even_numbers():
    n = int(input("Enter a number: "))
    count = 0

    for i in range(n):
        if i % 2 == 0:
            count += 1
            print(i)

    print("Even number count:", count)


# count_even_numbers()

# --------------------------------------------
# Question 5:
# Take a number n from the user.
# Print all odd numbers less than n
# and count how many odd numbers are there.
#
# Learning:
# - odd condition using modulo
# - counting without printing (optimized version)
# --------------------------------------------

def count_odd_numbers():
    n = int(input("Enter a number: "))
    count = 0

    for i in range(n):
        if i % 2 != 0:
            count += 1

    print("Odd number count:", count)


# count_odd_numbers()