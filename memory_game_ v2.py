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
        elements.insert(middle, "-" + str(moves) + "a")
        elements.insert(middle, "-" + str(moves) + "a")
        continue

    index1 = int(indices[0])
    index2 = int(indices[1])

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(elements) or index2 >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        middle = len(elements) // 2
        elements.insert(middle, "-" + str(moves) + "a")
        elements.insert(middle, "-" + str(moves) + "a")
        continue

    if elements[index1] == elements[index2]:
        element = elements[index1]
        print(f"Congrats! You have found matching elements - {element}!")
        new_elements = []
        for i in range(len(elements)):
            if i != index1 and i != index2:
                new_elements.append(elements[i])
        elements = new_elements
        if not elements:
            print(f"You have won in {moves} turns!")
            break
    else:
        print("Try again!")
