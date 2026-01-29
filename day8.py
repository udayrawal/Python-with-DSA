# ============================================
# Day 8: Frequency & Counting Logic
# ============================================


# --------------------------------------------
# Question 1:
# Take 5 numbers from the user and
# count the frequency of each element.
#
# Learning:
# - dictionary usage
# - key existence checking
# - frequency counting pattern
# --------------------------------------------

def count_frequency():
    nums = []
    frequency = {}

    for i in range(5):
        element = int(input("Enter a number: "))
        nums.append(element)

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    print("Frequency:", frequency)


# count_frequency()


# --------------------------------------------
# Question 2:
# Take 5 numbers from the user and
# count how many elements are duplicates.
#
# Learning:
# - reuse frequency logic
# - condition-based counting
# - separating data collection from logic
# --------------------------------------------

def count_duplicate_elements():
    nums = []
    frequency = {}

    for i in range(5):
        element = int(input("Enter a number: "))
        nums.append(element)

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    duplicate_count = 0

    for num in frequency:
        if frequency[num] > 1:
            duplicate_count += 1

    print("Duplicate elements count:", duplicate_count)


# count_duplicate_elements()


# --------------------------------------------
# Question 3:
# Take 5 numbers from the user and
# find the most frequent element.
#
# Learning:
# - tracking maximum value
# - comparison-based replacement
# - separating count from decision
# --------------------------------------------

def most_frequent_element():
    nums = []
    frequency = {}

    for i in range(5):
        element = int(input("Enter a number: "))
        nums.append(element)

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = 0
    result = None

    for num in frequency:
        if frequency[num] > max_count:
            max_count = frequency[num]
            result = num

    print("Most frequent element:", result)


# most_frequent_element()

# ------------------------------------------------------------------
# End of Day 8: Frequency & Counting Logic
# ------------------------------------------------------------------