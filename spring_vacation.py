# A group of friends decides to go on a trip for a few days during spring vacation. They have a certain budget.
# Your task is to calculate their expenses during the trip and find out if they will have enough money to finish the vacation.
# Create a program that calculates traveling expenses by entering the following information:
# •	Days of the vacation
# •	Budget for the whole group
# •	The number of people
# •	Price for fuel per kilometer - it's the price for fuel that their car consumes per kilometer
# •	Food expenses per person for a day
# •	Hotel room (accommodation) price for one night per person
# Before starting the trip, the group pays the total price for food and accommodation. If the group is larger than 10, it receives a 25% discount on the accommodation expenses.
# Every day, they travel some distance, and you should calculate the expenses for the traveled kilometers.
# At the end of every third and every fifth day, they have some additional expenses, which are 40% of the current value of the expenses.
# At the end of every seventh day, they receive a small amount of money for their expenses - equal to the result of the calculation currentExpenses / numberOfPeople.
# If the expenses exceed the budget at some point, stop calculating and print the following message:
# "Not enough money to continue the trip. You need {money}$ more."
# If the budget is enough:
# "You have reached the destination. You have {money}$ budget left."
# Print the result formatted 2 digits after the decimal separator.
# Note: We accept that the days of the vacations to be equal to the number of nights in the hotel.
# Input
# •	On the 1st line, you are going to receive the days of the trip - an integer in the range [1…20].
# •	On the 2nd line - the budget - a real number in the range [0.00 - 100000.00].
# •	On the 3rd line - the number of people - an integer in the range [1 - 20].
# •	On the 4th line - the price for fuel per kilometer - a real number in the range [0.00 - 2.00].
# •	On the 5th line - food expenses per person for a day - a real number in the range [0.00 - 50.00].
# •	On the 6th line - the room's price for a night per person - a real number in the range [0.00 - 1000.00].
# •	On the next n lines - one for each of the days - the traveled distance in kilometers per day - a real number in the range [0.00 - 1000.00].


days = int(input())
budget = float(input())
people = int(input())
fuel = float(input())
food = float(input())
room = float(input())

# Calculate initial expenses
total_food = food * people * days
total_room = room * people * days

# Apply 25% discount on accommodation if group > 10
if people > 10:
    total_room = total_room * 0.75

# Initial expenses are just food and room (not fuel yet)
total_expenses = total_food + total_room

for day in range(1, days + 1):
    distance = float(input())
    # Add fuel cost for the day
    total_expenses += distance * fuel

    # Additional expenses on 3rd and 5th days
    if day % 3 == 0 or day % 5 == 0:
        total_expenses += total_expenses * 0.4

    # Money received on 7th day
    if day % 7 == 0:
        total_expenses -= total_expenses / people

    if total_expenses > budget:
        break

if total_expenses > budget:
    print(f"Not enough money to continue the trip. You need {total_expenses - budget:.2f}$ more.")
else:
    print(f"You have reached the destination. You have {budget - total_expenses:.2f}$ budget left.")

