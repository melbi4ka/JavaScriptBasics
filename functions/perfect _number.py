def purfect_number(num):
    sum_one = 0
    for i in range(1, num):
        if num % i == 0:
            sum_one += i
    if sum_one == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(purfect_number(number))
