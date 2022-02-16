import random

def two_egg_dropper(limit):
    total = 0
    addition = 0
    guess_list = []
    steps = 0
    final_text = ""

    # Generates and sums triangle numbers until it reaches or exceeds the limit
    while total <= limit:
        addition += 1
        total = (addition ** 2 + addition) / 2

    count = 0
    aggregate = 0

    # As long as the total has not exceeded the limit, the first condition continues to add to it
    # The second condition changes the first number to go over to the limit to the limit in order to save steps
    # The last condition exits the loop when the latest value is either the limit or over it
    for guess in range(addition, 0, -1):
        if aggregate < limit:
            aggregate = count + guess
            guess_list.append(aggregate)
            count += guess
        elif guess_list[-1] > limit:
            guess_list[-1] = limit
        else:
            break

    floor_range = 0

    final_text += "The max number of steps for this many floors is: " + str(addition) + "\n"

    # Generates random floor that serves as the first floor that breaks the egg
    breaking_floor = random.randint(1, limit)
    final_text += "The lowest floor the egg will break from: " + str(breaking_floor) + "\n"

    for guiding_floor in guess_list:
        steps += 1
        final_text += "Trying floor: " + str(guiding_floor) + "\n"
        if guiding_floor >= breaking_floor:
            final_text += "The first egg broke on floor " + str(guiding_floor) + "." + "\n"
            break
        floor_range += 1

    if floor_range == 0:
        for specific_floor in range(1, guess_list[floor_range]):
            steps += 1
            final_text += "Trying floor: " + str(specific_floor) + "\n"
            if specific_floor >= breaking_floor:
                final_text += "The second egg broke on floor " + str(specific_floor) + ", so the floor must be " + str(
                    guiding_floor) + "." + "\n"
                break
    else:
        new_count = 1
        for specific_floor in range(guess_list[floor_range - 1] + 1, guess_list[floor_range]):
            steps += 1
            final_text += "Trying floor: " + str(specific_floor) + "\n"
            new_count += 1
            if specific_floor >= breaking_floor:
                final_text += "The second egg broke on floor " + str(specific_floor) + ", so the floor must be " + str(
                    specific_floor) + "." + "\n"
                break
            if new_count == guess_list[floor_range] - guess_list[floor_range - 1]:
                final_text += "The second egg never broke, so the floor must be " + str(guiding_floor) + "." + "\n"

    final_text += "Solved in " + str(steps) + " steps."

    return final_text


print(two_egg_dropper(1000))
