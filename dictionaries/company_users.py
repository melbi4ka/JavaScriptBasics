line = input()
company_dict = {}

while line != "End":
    explode = line.split(" -> ")
    company = explode[0]
    ids = explode[1]

    if company not in company_dict:
        company_dict[company] = []
    company_dict[company].append(ids)

    line = input()

for key, values in company_dict.items():
    new_values = []
    [new_values.append(x) for x in values if x not in new_values]
    print(f"{key}")
    result = '\n-- '.join(new_values)
    print(f"-- {result}")

#print(company_dict)


