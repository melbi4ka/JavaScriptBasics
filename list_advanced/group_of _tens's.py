sequence_nums = [int(x) for x in input().split(", ")]
group_of_nums = 10
counter = 0

while counter < len(sequence_nums):
    new_numbers = []
    for num in sequence_nums:
        if group_of_nums - 10 < num <= group_of_nums:
            new_numbers.append(num)
            counter += 1
    group_of_nums += 10

    print(f"Group of {group_of_nums-10}'s: {new_numbers}")

