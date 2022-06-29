line = input().split()
result = 0
word_one = line[0]
word_two = line[1]

if len(word_one) == len(word_two):
    for n in range(len(word_one)):
        result += ord(word_one[n]) * ord(word_two[n])

elif len(word_one) < len(word_two):
    for n in range(len(word_one)):
        result += ord(word_one[n]) * ord(word_two[n])
    for m in range(len(word_one), len(word_two)):
        result += ord(word_two[m])

elif len(word_one) > len(word_two):
    for n in range(len(word_two)):
        result += ord(word_one[n]) * ord(word_two[n])
    for m in range(len(word_two), len(word_one)):
        result += ord(word_one[m])


print(result)




