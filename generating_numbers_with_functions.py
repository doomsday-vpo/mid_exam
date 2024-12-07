def add_to_start(numbers, values_to_add):
    return values_to_add + numbers


def remove_greater_than(numbers, value):
    return [x for x in numbers if x <= value]


def replace_value(numbers, value, replacement):
    if value in numbers:
        index = numbers.index(value)
        numbers[index] = replacement
    return numbers


def remove_at_index(numbers, index):
    if 0 <= index < len(numbers):
        numbers.pop(index)
    return numbers


def find_even(numbers):
    return [x for x in numbers if x % 2 == 0]


def find_odd(numbers):
    return [x for x in numbers if x % 2 != 0]


def process_command(numbers, command):
    tokens = command.split()

    if "add to start" in command:
        numbers = add_to_start(numbers, [int(x) for x in tokens[3:]])
    elif "remove greater than" in command:
        numbers = remove_greater_than(numbers, int(tokens[3]))
    elif tokens[0] == "replace":
        numbers = replace_value(numbers, int(tokens[1]), int(tokens[2]))
    elif "remove at index" in command:
        numbers = remove_at_index(numbers, int(tokens[3]))
    elif command == "find even":
        print(*find_even(numbers))
    elif command == "find odd":
        print(*find_odd(numbers))

    return numbers


def main():
    numbers = [int(x) for x in input().split()]
    command = input()

    while command != "END":
        numbers = process_command(numbers, command)
        command = input()

    print(", ".join(str(x) for x in numbers))


if __name__ == "__main__":
    main()
