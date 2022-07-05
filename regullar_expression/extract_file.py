line = input().split('\\')
new_line = line[-1].split(".")
print(f"""File name: {new_line[0]}
File extension: {new_line[1]}""")



