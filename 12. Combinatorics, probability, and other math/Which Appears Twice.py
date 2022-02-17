import random

# Code used to test function starts
# Creates a random integer in the interval [10, 9999] to serves as the length of the list
limit = random.randint(10, 9999)
print("This is the generated length of the list:", limit)

# Creates a random insert value in interval [10, limit - 1] to avoid the edge case of having the integer attempt to be
# inserted out of range
insert = random.randint(1, limit - 1)
print("This is the generated value inserted into the list:", insert)

# Uses the random limit integer to create a list of size len(rand_list) == limit - 1
rand_list = list(range(1, limit))

# Inserts the random limit integer a the end of the list, then shuffles the list
rand_list.append(insert)
random.shuffle(rand_list)
# Code used to test function ends


def find_duplicate(num_list):
    total = 0
    length = len(num_list)

    for num in num_list:
        total += num

    # Uses the triangle number formula to get the result of summing all integers in over the interval
    # [1, length] without the need to actually add each individual value
    correct_total = (length ** 2 + length) / 2

    # Finding the difference between the correct_total and total only results in the distance between the added value
    # and the length of the list, so finding the difference between length and the original difference gives what must
    # be the added value
    difference = int(length - (correct_total - total))

    return difference


print("This is the generated value as determined by the program:", find_duplicate(rand_list))
