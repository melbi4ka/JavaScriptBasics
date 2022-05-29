text = input().split('#')
water = int(input())
effort = 0
total_fire = 0
cells_put_out = []
is_Valid = False

#print('Cells:')
for line in range(len(text)):
    command = text[line].split(" = ")
    fire_type = command[0]
    value = int(command[1])
    if fire_type == 'High' and 81 <= value <= 125:
        is_Valid = True
    if fire_type == 'Medium' and 51 <= value <= 80:
        is_Valid = True
    if fire_type == 'Low' and 1 <= value <= 50:
        is_Valid = True
    if is_Valid:
        if water-value >= 0:
            water -= value
            cells_put_out.append(str(value))
            total_fire += value
            effort += value*0.25
            is_Valid = False
            #print(f' - {cells_put_out[cell]}'
print('Cells:')
for cell in range(len(cells_put_out)):
    print(f' - {cells_put_out[cell]}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
