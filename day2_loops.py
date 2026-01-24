# ============================================
# Day 2: Loops & Summation
# ============================================


# --------------------------------------------
# Question 1:
# Take a number n from the user and print
# numbers from 1 to n.
# Also calculate the sum of these numbers.
#
# Learning:
# - for loop with range(start, end)
# - how range(1, n+1) works
# - using a variable to store sum
# --------------------------------------------

def sum_from_1_to_n():
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n + 1):
        total += i
        print(i)

    print("Sum:", total)


# sum_from_1_to_n()


# --------------------------------------------
# Question 2:
# Take a number n from the user and print
# numbers starting from 0 to n-1.
# Also calculate their sum.
#
# Learning:
# - how range(n) starts from 0
# - difference between range(n) and range(1, n+1)
# --------------------------------------------

def sum_using_range_n():
    n = int(input("Enter a number: "))
    total = 0

    for i in range(n):
        total += i
        print(i)

    print("Sum:", total)


# sum_using_range_n()


# --------------------------------------------
# Question 3:
# Take a number n from the user.
# Print all even numbers from 1 to n
# and calculate the sum of even numbers.
#
# Learning:
# - conditional logic inside loop
# - filtering values using modulo
# - summing selected values
# --------------------------------------------

def sum_of_even_numbers():
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
            print(i)

    print("Total:", total)


sum_of_even_numbers()