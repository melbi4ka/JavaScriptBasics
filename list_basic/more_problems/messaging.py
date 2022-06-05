numbers = input().split()
word = list(input())
new_list = []


for i in range(len(numbers)):
    current_number = numbers[i]
    summary = 0
    for j in range(len(current_number)):
        digit = int(current_number[j])
        summary += digit
    new_list.append(summary)

end_list = []
for k in range(len(new_list)):
    if new_list[k] < len(word):
        idx = new_list[k]
        end_list.append(word[idx])
        word.pop(idx)
    else:
        idx = new_list[k] % len(word)
        end_list.append(word[idx])
        word.pop(idx)


for j in end_list:
    print(", ".join(j), end="")








#print(new_list)





