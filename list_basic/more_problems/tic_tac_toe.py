row_one = list(map(int, input().split()))
row_two = list(map(int, input().split()))
row_three = list(map(int, input().split()))
win_first = False
win_second = False


if row_one[0] == row_one[1] == row_one[2]:
    if row_one[0] == 1:
        win_first = True
    elif row_one[0] == 2:
        win_second = True
elif row_two[0] == row_two[1] == row_two[2]:
    if row_two[0] == 1:
        win_first = True
    elif row_two[0] == 2:
        win_second = True
elif row_three[0] == row_three[1] == row_three[2]:
    if row_three[0] == 1:
        win_first = True
    elif row_three[0] == 2:
        win_second = True
elif row_one[0] == row_two[0] == row_three[0]:
    if row_one[0] == 1:
        win_first = True
    elif row_one[0] == 2:
        win_second = True
elif row_one[1] == row_two[1] == row_three[1]:
    if row_one[1] == 1:
        win_first = True
    elif row_one[1] == 2:
        win_second = True
elif row_one[2] == row_two[2] == row_three[2]:
    if row_one[2] == 1:
        win_first = True
    elif row_one[2] == 2:
        win_second = True
elif row_one[0] == row_two[1] == row_three[2]:
    if row_one[0] == 1:
        win_first = True
    elif row_one[0] == 2:
        win_second = True
elif row_one[2] == row_two[1] == row_three[0]:
    if row_one[2] == 1:
        win_first = True
    elif row_one[2] == 2:
        win_second = True


if win_first:
    print("First player won")
elif win_second:
    print("Second player won")
else:
    print("Draw!")
    
