price_rating = [int(n) for n in input().split(", ")]
entry_point = int(input())
type_of_items = input()

left_list = []
right_list = []

for n in range(len(price_rating)):
    if n < entry_point:
        left_list.append(price_rating[n])
    elif n > entry_point:
        right_list.append(price_rating[n])

sum_left = 0
sum_right = 0

if type_of_items == "cheap":
    for n in left_list:
        if n < price_rating[entry_point]:
            sum_left += n
    for m in right_list:
        if m < price_rating[entry_point]:
            sum_right += m
elif type_of_items == "expensive":
    for n in left_list:
        if n >= price_rating[entry_point]:
            sum_left += n
    for m in right_list:
        if m >= price_rating[entry_point]:
            sum_right += m


if sum_left > sum_right:
    print(f"Left - {sum_left}")
elif sum_left < sum_right:
    print(f"Right - {sum_right}")
else:
    print(f"Left - {sum_left}")

    #100/100


