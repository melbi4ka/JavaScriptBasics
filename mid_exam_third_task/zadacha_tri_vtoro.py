price_rating = [int(n) for n in input().split(", ")]
index = int(input())
type_of_items = input()

price_left = 0
price_right = 0

for num in range(len(price_rating)):
    if num < index:
        if type_of_items == "cheap":
            if price_rating[num] < price_rating[index]:
                price_left += price_rating[num]
        if type_of_items == "expensive":
            if price_rating[num] >= price_rating[index]:
                price_left += price_rating[num]

    if num > index:
        if type_of_items == "cheap":
            if price_rating[num] < price_rating[index]:
                price_right = price_rating[num]
        if type_of_items == "expensive":
            if price_rating[num] >= price_rating[index]:
                price_right = price_rating[num]

if price_left > price_right:
    print(f"Left - {price_left}")
elif price_left < price_right:
    print(f"Right - {price_right}")
else:
    print(f"Left - {price_left}")




# left_list = []
# right_list = []
#
# for n in range(len(price_rating)):
#     if n < entry_point:
#         left_list.append(price_rating[n])
#     elif n > entry_point:
#         right_list.append(price_rating[n])
#
# sum_left = 0
# sum_right = 0
#
# if type_of_items == "cheap":
#     for n in left_list:
#         if n < price_rating[entry_point]:
#             sum_left += n
#     for m in right_list:
#         if m < price_rating[entry_point]:
#             sum_right += m
# elif type_of_items == "expensive":
#     for n in left_list:
#         if n >= price_rating[entry_point]:
#             sum_left += n
#     for m in right_list:
#         if m >= price_rating[entry_point]:
#             sum_right += m
#
#
# if sum_left > sum_right:
#     print(f"Left - {sum_left}")
# elif sum_left < sum_right:
#     print(f"Right - {sum_right}")
# else:
#     print(f"Left - {sum_left}")