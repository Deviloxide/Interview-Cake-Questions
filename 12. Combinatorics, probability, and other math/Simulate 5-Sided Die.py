import random

rand5_results = []


def rand7():
    return random.randint(1, 7)


# This solution is pretty simple, but only works due to the fact that rand7() generates more numbers than necessary not
# too few. So, taking only the necessary values, in this case [1...5], from an already uniform distribution.
def rand5():
    while True:
        chance = rand7()
        if chance < 6:
            return chance


limit = 999999

for i in range(0, limit):
    rand5_results.append(rand5())

# Shows the relative frequencies to show that the values are uniform for all values. They should all be ~20% and with a
# sufficiently high limit
print(str((rand5_results.count(1) / limit) * 100) + "%")
print(str((rand5_results.count(2) / limit) * 100) + "%")
print(str((rand5_results.count(3) / limit) * 100) + "%")
print(str((rand5_results.count(4) / limit) * 100) + "%")
print(str((rand5_results.count(5) / limit) * 100) + "%")
