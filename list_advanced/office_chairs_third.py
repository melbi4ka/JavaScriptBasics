number_of_rooms = int(input())
all_visitors = 0
all_chairs = 0
is_enough = True

for nums in range(1, number_of_rooms+1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])
    all_visitors += visitors
    all_chairs += chairs
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {nums}")
        is_enough = False

if is_enough:
    print(f"Game On, {all_chairs - all_visitors} free chairs left")
