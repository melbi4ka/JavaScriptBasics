import re

pattern = r"(.+) (.+) (\d*\.*\d*) \-\> (.+)"
# pattern = r"([A-Za-z0-9]+) ([A-Za-z0-9]+) (\d*\.*\d*) \-\> ([A-za-z0-9, ]+)+"
line = input()
books_dict = {}

while line != "on work":
    matches = re.findall(pattern, line)
    if matches:
        book = matches[0][0]
        author = matches[0][1]
        price = float(matches[0][2])
        chapter = matches[0][3].split(", ")

        if book not in books_dict:
            books_dict[book] = {"author": author, "price": price, "chapters": chapter}
            if books_dict[book]['price'] == 0.0:
                del books_dict[book]

    line = input()

# print(books_dict)

a_command = input()
sold_books = []

while a_command != "end work":
    if a_command not in books_dict:
        print(f"No such book here")

    else:
        sold_books.append(a_command)

    a_command = input()

# print(sold_books)
money = 0
for el in sold_books:
    for key, value in books_dict.items():
        if key == el:
            print(f"SOLD: {key} with author {value['author']}. Chapters in the book {len(value['chapters'])}")
            money += value['price']

if money == 0:
    print("Bad day :(")
elif money > 0:
    print(f"Money: {money:.2f}")
