from math import pow

number_snowballs = int(input())
max_value = 0
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0

for number in range(number_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    quality = int(input())

    value = pow(snowball_weight / snowball_time, quality)
    if value > max_value:
        max_value = value
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = quality


print(f"{max_snowball_weight} : {max_snowball_time} = {max_value:.0f} ({max_snowball_quality})")












