from math import floor

bisc_per_day = int(input())
count_of_workers = int(input())
bisc_per_month = int(input())
my_bisc_month = 0


for num in range(1, 31):

    if num % 3 == 0:
        reduced_bisc = floor(bisc_per_day * count_of_workers * 0.75)
        my_bisc_month += reduced_bisc
    else:
        my_bisc_month += floor(bisc_per_day * count_of_workers)


print(f"You have produced {my_bisc_month} biscuits for the past month.")
diff = abs(my_bisc_month - bisc_per_month)
percentage = diff/bisc_per_month * 100
if my_bisc_month > bisc_per_month:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")

#100/100