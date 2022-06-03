time = input().split()
time_int = []
for i in range(len(time)):
    int_time = int(time[i])
    time_int.append(int_time)

time_left = 0
time_right = 0

for n in range(0, len(time_int) // 2):
    time_left += time_int[n]
    if time_int[n] == 0:
        time_left *= 0.8

for k in range(len(time_int)-1, (len(time_int) // 2), -1):
    time_right += time_int[k]
    if time_int[k] == 0:
        time_right *= 0.8

if time_left < time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")

#print(len(time_int), middle )






    #print(time_left)


