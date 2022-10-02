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

