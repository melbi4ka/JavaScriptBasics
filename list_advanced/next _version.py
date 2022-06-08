version = int("".join(input().split(".")))
# convert el in input to single el , join them with nothing
# then convert it to int
new_version = version + 1
# add 1 to increase

print(".".join ([str(el) for el in str(new_version)]))
# comprehension - take int like str , for-loop to take elements like str
# then join


