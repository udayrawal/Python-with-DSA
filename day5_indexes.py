# ============================================
# Day 5: Index-Based Thinking
# ============================================


# --------------------------------------------
# Question 1:
# Take 5 numbers from the user and
# print each element along with its index.
#
# Learning:
# - understanding index vs value
# - using range(len(list))
# - accessing elements using list[index]
# --------------------------------------------

def print_index_and_value():
    nums = []

    for i in range(5):
        value = int(input("Enter a number: "))
        nums.append(value)

    for i in range(len(nums)):
        print(f"Index {i} -> {nums[i]}")


# print_index_and_value()


# --------------------------------------------
# Question 2:
# Take 5 numbers from the user.
# Print numbers that are greater than
# the previous number in the list.
#
# Learning:
# - index-based comparison
# - accessing previous element using i-1
# - why index-based loops matter in DSA
# --------------------------------------------

def greater_than_previous():
    nums = []

    for i in range(5):
        value = int(input("Enter a number: "))
        nums.append(value)

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            print(nums[i])


greater_than_previous()