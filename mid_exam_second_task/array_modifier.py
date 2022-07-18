numbers = input().split()
command = input()
int_numbers = []
for nums in numbers:
    int_numbers.append(int(nums))


while command != "end":
    command = command.split()

    if command[0] == "swap":
        idx_one = int(command[1])
        idx_two = int(command[2])
        int_numbers[idx_one], int_numbers[idx_two] = int_numbers[idx_two], int_numbers[idx_one]

    elif command[0] == "multiply":
        idx_one = int(command[1])
        idx_two = int(command[2])
        multply_result = int_numbers[idx_one] * int_numbers[idx_two]
        int_numbers[idx_one] = multply_result

    if command[0] == "decrease":
        for el in range(len(int_numbers)):
            int_numbers[el] = int_numbers[el] - 1
            #[n-1 for n in int_numbers]
    command = input()

str_numbers = map(str, int_numbers)
print(", ".join(str_numbers))
