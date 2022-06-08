version = [int(k) for k in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0: # проверява дали следващия индекс напред не извън индексите, когато е наобратно последния тр да е 0
            version[index - 1] += 1
print(".".join([str(s) for s in version]))


