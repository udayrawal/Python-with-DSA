# ============================================
# Day 6: Debugging & Pattern Recognition
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
# Print all numbers that are divisible
# by both 3 and 5 from the list.
#
# Learning:
# - logical AND condition
# - filtering elements from a list
# --------------------------------------------

def divisible_by_3_and_5():
    nums = [10, 15, 30, 22, 45, 9]

    for element in nums:
        if element % 3 == 0 and element % 5 == 0:
            print(element)


# divisible_by_3_and_5()


# --------------------------------------------
# Question 3:
# Count how many times the array increases
# compared to the previous element.
#
# Learning:
# - neighbor comparison
# - index-based traversal
# - counting pattern
# --------------------------------------------

def count_increases():
    nums = [1, 3, 2, 4, 6, 5]
    count = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1

    print(count)


# count_increases()


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
    nums = [2, 9, 4, 10, 3]
    max_diff = 0

    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1])
        if diff > max_diff:
            max_diff = diff

    print(max_diff)


max_consecutive_difference()