# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.
# Constraints
# •	There won't be any duplicate items in the initial list
# Output
# •	Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"

# example input:
# Tomatoes!Potatoes!Bread
# Unnecessary Milk
# Urgent Tomatoes
# Go Shopping!

# example output:
# Tomatoes, Potatoes, Bread


groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    if command.startswith("Urgent"):
        item = command.split(" ")[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif command.startswith("Unnecessary"):
        item = command.split(" ")[1]
        if item in groceries:
            groceries.remove(item)
    elif command.startswith("Correct"):
        old_item = command.split(" ")[1]
        new_item = command.split(" ")[2]
        if old_item in groceries:
            groceries[groceries.index(old_item)] = new_item
    elif command.startswith("Rearrange"):
        item = command.split(" ")[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input()
print(", ".join(groceries))
