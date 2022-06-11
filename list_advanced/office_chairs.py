number_of_rooms = int(input())
all_visitors = 0
all_chairs = 0

for nums in range(1, number_of_rooms+1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])
    if chairs < visitors:
        all_visitors += visitors
        all_chairs += chairs
        print(f"{visitors - chairs} more chairs needed in room {nums}")
    else:
        all_visitors += visitors
        all_chairs += chairs

if all_visitors <= all_chairs:
    print(f"Game On, {all_chairs - all_visitors} free chairs left")
