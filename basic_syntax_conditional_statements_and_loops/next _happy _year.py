current_year = int(input())

while True:
    current_year += 1
    string_current_year = str(current_year)
    if len(string_current_year) == len(set(string_current_year)):
        print(current_year)
        break

#sep21ex

