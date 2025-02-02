# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon('s rooms. '
# Each room is separated with ')|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp."
# o	After that, print your current health: "Current health: {health} hp."
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster.
# You should remove the monster's attack from your health.
# o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"
# Input / Constraints
# You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
# Output
# Print the corresponding messages described above.

#example input:
#rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000
#example output:
# You slayed rat.
# You slayed bat.
# You healed for 10 hp.
# Current health: 80 hp.
# You slayed rat.
# You found 100 bitcoins.
# You died! Killed by boss.
# Best room: 7

def mu_online(rooms):
    health = 100
    bitcoins = 0
    room_count = 0

    for room in rooms.split('|'):
        room_count += 1
        command, value = room.split()
        value = int(value)

        if command == 'potion':
            heal_amount = min(value, 100 - health)
            health += heal_amount
            print(f"You healed for {heal_amount} hp.")
            print(f"Current health: {health} hp.")
        elif command == 'chest':
            bitcoins += value
            print(f"You found {value} bitcoins.")
        else:
            health -= value
            if health > 0:
                print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                print(f"Best room: {room_count}")
                return

    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


dungeon = input()
mu_online(dungeon)
