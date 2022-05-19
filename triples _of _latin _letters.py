number = int(input())
for num_one in range(number):
    char_one = chr(num_one + 97)
    for num_two in range(number):
        char_two = chr(num_two + 97)
        for num_tree in range(number):
            char_tree = chr(num_tree + 97)
            print(char_one + char_two + char_tree)
