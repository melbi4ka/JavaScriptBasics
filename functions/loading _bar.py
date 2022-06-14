def loading_bar(num):
    loading_num = num//10
    if num == 100:
        return f"{num}% Complete!\n[{'%' * loading_num}]"
    elif num < 100:
        return f"{num}% [{'%' * loading_num}{'.' * (10-loading_num)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
