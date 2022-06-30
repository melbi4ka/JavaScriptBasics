# line = input()
#
# for char in range(len(line)):
#     if line[char] == ":" and ;ine[char+1] != " ":
#         emoticon = line[char] + line[char + 1]
#         print(emoticon)
def find_emoticon(a_line):
    for el in range(len(a_line)):
        if a_line[el] == ":" and a_line[el + 1] != " ":
            emoticon = a_line[el] + a_line[el + 1]
            print(emoticon)


line = input()
find_emoticon(line)
