# ============================================
# Day 3: Lists & Counting
# ============================================


# --------------------------------------------
# Question 1:
# Take 5 numbers from the user and
# print all even numbers.
# Also count how many even numbers are present.
#
# Learning:
# - storing multiple values in a list
# - looping through a list
# - using a counter variable
# --------------------------------------------

def count_even_numbers():
    nums = []
    count = 0

    for i in range(5):
        element = int(input("Enter a number: "))
        nums.append(element)

    for num in nums:
        if num % 2 == 0:
            count += 1
            print(num)

    print("Even count:", count)


# count_even_numbers()


# --------------------------------------------
# Question 2:
# Take 5 numbers from the user.
# Count how many numbers are greater than 10.
# Print numbers that are less than or equal to 10.
#
# Learning:
# - applying conditions on list elements
# - filtering values from a list
# - counting based on a condition
# --------------------------------------------

def count_numbers_greater_than_10():
    nums = []
    count = 0

    for i in range(5):
        element = int(input("Enter a number: "))
        nums.append(element)

    for num in nums:
        if num > 10:
            count += 1
        else:
            print("Less than or equal to 10:", num)

    print("Count of numbers greater than 10:", count)


count_numbers_greater_than_10()