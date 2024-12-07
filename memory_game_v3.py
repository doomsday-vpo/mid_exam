sequence = input().split()
moves = 0

while True:
    command = input()

    if command == 'end':
        break

    index1, index2 = map(int, command.split())
    moves += 1

    if index1 == index2 or not (0 <= index1 < len(sequence) or not 0 <= index2 < len(sequence)):
        pass
    else:
        if sequence[index1] == sequence[index2]:
            element = sequence[index1]
            print(f'Congrats! You have found matching elements - {element}!')


