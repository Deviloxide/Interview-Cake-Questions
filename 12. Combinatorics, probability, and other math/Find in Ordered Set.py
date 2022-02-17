import random

limit = random.randint(10, 9999)
print("This is the generated length of the list:", limit)

insert = random.randint(1, limit - 1)
print("This is the generated value inserted into the list:", insert)

rand_list = list(range(1, limit))

rand_list.insert(0, insert)
random.shuffle(rand_list)


def find_duplicate(num_list):
    total = 0
    length = len(num_list)

    for num in num_list:
        total += num

    correct_total = (len(num_list) ** 2 + len(num_list)) / 2

    difference = int(length - (correct_total - total))

    return difference


print("This is the generated value as determined by the program:", find_duplicate(rand_list))
