# ============================================
# Day 4: Max, Min & Comparison Logic
# ============================================


# --------------------------------------------
# Question 1:
# Take 5 numbers from the user and
# find the largest number.
#
# Learning:
# - initializing with first element
# - comparison-based replacement
# --------------------------------------------

def find_largest_number():
    nums = []

    for i in range(5):
        nums.append(int(input("Enter a number: ")))

    largest = nums[0]

    for element in nums:
        if element > largest:
            largest = element

    print("Largest:", largest)


# find_largest_number()


# --------------------------------------------
# Question 2:
# Take 5 numbers from the user and
# find the smallest number.
#
# Learning:
# - min logic using comparison
# - replacement instead of counting
# --------------------------------------------

def find_smallest_number():
    nums = []

    for i in range(5):
        nums.append(int(input("Enter a number: ")))

    smallest = nums[0]

    for element in nums:
        if element < smallest:
            smallest = element

    print("Smallest:", smallest)


# find_smallest_number()


# --------------------------------------------
# Question 3:
# Take 5 numbers from the user and
# find the second largest number.
#
# Learning:
# - tracking two values
# - updating order correctly
# --------------------------------------------

def find_second_largest():
    nums = []

    for i in range(5):
        nums.append(int(input("Enter a number: ")))

    largest = nums[0]
    second_largest = nums[0]

    for element in nums:
        if element > largest:
            second_largest = largest
            largest = element
        elif element < largest and element > second_largest:
            second_largest = element

    print("Second Largest:", second_largest)


# find_second_largest()


# --------------------------------------------
# Question 4:
# Take 5 numbers from the user and
# find the second smallest number.
#
# Learning:
# - reverse comparison logic
# - careful condition checking
# --------------------------------------------

def find_second_smallest():
    nums = []

    for i in range(5):
        nums.append(int(input("Enter a number: ")))

    smallest = nums[0]
    second_smallest = nums[0]

    for element in nums:
        if element < smallest:
            second_smallest = smallest
            smallest = element
        elif element > smallest and element < second_smallest:
            second_smallest = element

    print("Second Smallest:", second_smallest)


# find_second_smallest()