cards = input().split(" ")
shuffles = int(input())

new_cards_list = []

for shuffles in range(shuffles):
    new_cards_list = []
    middle_cards = len(cards) // 2
    left_side = cards[0:middle_cards]
    right_side = cards[middle_cards::]
    for index in range(len(left_side)):
        new_cards_list.append(left_side[index])
        new_cards_list.append(right_side[index])
    cards = new_cards_list
print(cards)
