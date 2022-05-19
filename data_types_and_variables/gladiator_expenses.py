lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expences = 0
for fights in range (1, lost_fights_count + 1):
    if fights % 2 == 0:
        expences += helmet_price
    if fights % 3 == 0:
        expences += sword_price
    if fights % 2 == 0 and fights % 3 == 0:
        expences += shield_price
    if fights % 12 == 0:
        expences += armor_price

print(f"Gladiator expenses: {expences:.2f} aureus")
