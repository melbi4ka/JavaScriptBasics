number = int(input())
free_space = 255
sum_litters = 0

for nums in range(number):
    litters = int(input())

    if sum_litters + litters > free_space:
        print("Insufficient capacity!")
    else:
        sum_litters += litters

print(sum_litters)














