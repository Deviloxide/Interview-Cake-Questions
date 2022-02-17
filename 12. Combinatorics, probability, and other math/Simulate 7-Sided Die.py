import random

rand7_results = []

def rand5():
    return random.randint(1, 5)

def rand7():
    chance = 0

    while chance == 0:
        chance_array = [
            [1, 2, 3, 4, 5],
            [6, 7, 1, 2, 3],
            [4, 5, 6, 7, 1],
            [2, 3, 4, 5, 6],
            [7, 0, 0, 0, 0]
       ]

        chance = chance_array[rand5() - 1][rand5() - 1]

    return chance


limit = 999999

for i in range(0, limit):
    rand7_results.append(rand7())

# Shows the relative frequencies to show that the values are uniform for all values. They should all be ~20% and with a
# sufficiently high limit
print(str((rand7_results.count(1) / limit) * 100) + "%")
print(str((rand7_results.count(2) / limit) * 100) + "%")
print(str((rand7_results.count(3) / limit) * 100) + "%")
print(str((rand7_results.count(4) / limit) * 100) + "%")
print(str((rand7_results.count(5) / limit) * 100) + "%")
print(str((rand7_results.count(6) / limit) * 100) + "%")
print(str((rand7_results.count(7) / limit) * 100) + "%")
