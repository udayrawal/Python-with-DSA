# ============================================
# Day 7: Array Patterns & Problem Solving
# ============================================


# --------------------------------------------
# Question 1:
# Given a list of numbers, find the average
# and print all numbers greater than the average.
#
# Learning:
# - accumulation pattern (sum)
# - calculating average
# - filtering values using condition
# --------------------------------------------

def greater_than_average():
    nums = [2, 4, 6, 8, 10]
    total = 0

    for element in nums:
        total += element

    avg = total / len(nums)

    for element in nums:
        if element > avg:
            print(element)


# greater_than_average()


# --------------------------------------------
# Question 2:
# Print all numbers that are divisible by
# 3 or 5 from the given list.
#
# Learning:
# - filtering elements using conditions
# - logical OR operator
# - looping over values instead of indexes
# --------------------------------------------

def divisible_by_3_or_5():
    nums = [4, 6, 10, 15, 22, 30]

    for element in nums:
        if element % 3 == 0 or element % 5 == 0:
            print(element)


# divisible_by_3_or_5()


# --------------------------------------------
# Question 3:
# Count how many times the array decreases
# compared to the previous element.
#
# Learning:
# - index-based traversal
# - neighbor comparison
# - counting pattern
# --------------------------------------------

def count_decreases():
    nums = [9, 7, 8, 3, 2, 5]
    count = 0

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            count += 1

    print("Number of decreases:", count)


# count_decreases()


# --------------------------------------------
# Question 4:
# Find the maximum absolute difference
# between two consecutive elements.
#
# Learning:
# - using abs() for difference
# - neighbor comparison pattern
# - max tracking logic
# --------------------------------------------

def max_consecutive_difference():
    nums = [1, 10, 4, 15, 6]
    max_diff = 0

    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1])
        if diff > max_diff:
            max_diff = diff

    print("Maximum difference:", max_diff)


max_consecutive_difference()