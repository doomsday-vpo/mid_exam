# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the player receives "end" from the console,
# you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence,
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements
# •	On the following lines, you will receive integers until the command "end"
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message:
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# •	All elements in the sequence will always have a matching element.


# Examples
# Input 	Output
# 1 1 2 2 3 3 4 4 5 5
# 1 0
# -1 0
# 1 0
# 1 0
# 1 0
# end	Congrats! You have found matching elements - 1!
# Invalid input! Adding additional elements to the board
# Congrats! You have found matching elements - 2!
# Congrats! You have found matching elements - 3!
# Congrats! You have found matching elements - -2a!
# Sorry you lose :(
# 4 4 5 5



elements = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        if elements:
            print("Sorry you lose :(")
            print(" ".join(elements))
        break

    moves += 1
    indices = command.split()

    if len(indices) != 2 or not indices[0].isdigit() or not indices[1].isdigit():
        print("Invalid input! Adding additional elements to the board")
        middle = len(elements) // 2
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")
        continue

    index1, index2 = int(indices[0]), int(indices[1])

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(elements) or index2 >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        middle = len(elements) // 2
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")
        continue

    if elements[index1] == elements[index2]:
        element = elements[index1]
        print(f"Congrats! You have found matching elements - {element}!")
        elements = [e for i, e in enumerate(elements) if i not in (index1, index2)]
        if not elements:
            print(f"You have won in {moves} turns!")
            break
    else:
        print("Try again!")
