print("Please provide AI some data to learn...")
print("The current data length is 0, 100 symbols left")

# Get and process user's input
LENGTH = 100
numbers = ""
while len(numbers) < LENGTH:
    answer = input("Print a random string containing 0 or 1:")
    for x in answer:
        if x == "0" or x == "1":
            numbers += x
    left = str(LENGTH - len(numbers))
    print("Current data length is {}, {} symbols left".format(str(len(numbers)), left))

print("Final data string: {} ".format(numbers))

# Learn the user's patterns
triads = []
for i in range(0, 8):
    trial = bin(i)
    trial = trial.lstrip("0b").zfill(3)
    triads.append(trial)

triad_dict = {}
for triad in triads:
    triad_dict[triad] = {"0": 0, "1": 0}
for number in range(len(numbers) - 3):
    current_triad = numbers[number:number + 3]
    follow_number = numbers[number + 3]
    if follow_number == "0":
        triad_dict[current_triad]["0"] += 1
    if follow_number == "1":
        triad_dict[current_triad]["1"] += 1

# Start the game
print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

# Ask the user to enter string of 0 and 1 >= 4 symbols
import random

new_answer = ""
balance = 1000
while new_answer != "enough":
    new_answer = input("Print a random string containing 0 or 1:")
    if new_answer == "enough":
        print("Game over!")
    else:
        while len(new_answer) < 4:
            new_answer = input("Print a random string containing 0 or 1:")

        predictions = ""
        for number in range(len(new_answer) - 3):
            current_triad = new_answer[number:number + 3]
            if triad_dict[current_triad]["0"] > triad_dict[current_triad]["1"]:
                predictions += "0"
            if triad_dict[current_triad]["0"] < triad_dict[current_triad]["1"]:
                predictions += "1"
            if triad_dict[current_triad]["0"] == triad_dict[current_triad]["1"]:
                predictions += str(random.randint(0, 1))

        print("predictions:", predictions)
        N = 0
        M = (len(new_answer) - 3)

        for number in range(M):
            if predictions[number] == new_answer[number + 3]:
                N += 1
                balance -= 1
            if predictions[number] != new_answer[number + 3]:
                balance += 1
        ACC = round((N / M * 100), 2)
        print("Computer guessed", N, "out of", M, "symbols right (" + str(ACC), "%)")
        print("Your balance is now $" + str(balance))
