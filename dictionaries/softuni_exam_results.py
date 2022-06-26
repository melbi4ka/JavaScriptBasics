line = input()
exam_dict = {}
submission_dict = {}

while line != "exam finished":
    explode = line.split("-")
    if len(explode) == 3:
        username = explode[0]
        language = explode[1]
        points = int(explode[2])
        if language not in submission_dict:
            submission_dict[language] = 0
        submission_dict[language] += 1

        if language not in exam_dict:
            exam_dict[language] = {username:points}
        else:
            if username in exam_dict[language].keys():
                if points > exam_dict[language][username]:
                    exam_dict[language][username] = points
            else:
                exam_dict[language][username] = points

    elif len(explode) == 2:
        username = explode[0]
        if explode[1] == "banned":
            for key, value in exam_dict.items():
                if username in value:
                    del exam_dict[key][username]

    line = input()

print("Results:")
for key, value in exam_dict.items():
    for n in value:
        print(f"{n} | {value[n]}")

print("Submissions:")
for key, value in submission_dict.items():
    print(f"{key} - {value}")
