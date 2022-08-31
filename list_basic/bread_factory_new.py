import sys
from io import StringIO

input1 = """rest-12|order-10|eggs-100|rest-10 
"""
input2 = """order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

energy = 100
coins = 100

events = input().split("|")
is_closed = False

for el in events:
    event, number = el.split("-")
    number = int(number)

    if event == "rest":
        if energy + number > 100:
            number = 100 - energy
            energy = 100

        else:
            energy += number
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {event}.")
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
