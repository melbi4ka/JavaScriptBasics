number_of_rooms = int(input())
is_enough = True
difference = 0

for nums in range(1, number_of_rooms+1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])
    difference += chairs - visitors
    if chairs < visitors:
        print(f"{abs(visitors - chairs)} more chairs needed in room {nums}")
        is_enough = False

if is_enough:
    print(f"Game On, {difference} free chairs left")
