 line = input()

 for char in range(len(line)):
     if line[char] == ":" and ;ine[char+1] != " ":
         emoticon = line[char] + line[char + 1]
         print(emoticon)
