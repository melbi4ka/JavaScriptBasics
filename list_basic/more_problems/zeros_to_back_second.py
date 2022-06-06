info = input().split(", ")

temp = []
zeros = []

for zero in info:
    if int(zero) == 0:
        zeros.append(int(zero))
    else:
        temp.append(int(zero))
print(temp + zeros)
