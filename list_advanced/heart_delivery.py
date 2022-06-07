neighbor = [int(s) for s in input().split("@")]
command = input().split()
position = 0


while command[0] != "Love!":
    value = int(command[1])
    position += value
    if position >= len(neighbor):
        position = 0

    neighbor[position] -= 2

    if neighbor[position] == 0:
        print(f"Place {position} has Valentine's day.")
    if neighbor[position] < 0:
        print(f"Place {position} already had Valentine's day.")

    command = input().split()


print(f"Cupid's last position was {position}.")

failed_house = [house for house in neighbor if house > 0]
if len(failed_house) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_house)} places.")
