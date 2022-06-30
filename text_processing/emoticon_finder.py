def find_emoticon(a_line):
    for el in range(len(a_line)):
        if a_line[el] == ":" and a_line[el + 1] != " ":
            emoticon = a_line[el] + a_line[el + 1]
            print(emoticon)

line = input()
find_emoticon(line)
