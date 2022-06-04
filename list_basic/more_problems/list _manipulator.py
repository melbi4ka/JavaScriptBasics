import sys

nums = list(map(int, input().split()))
command = input().split()

while command[0] != "end":
    if command[0] == "exchange":
        idx = int(command[1])
        if idx >= len(nums) or idx < 0:
            print("Invalid index")
        else:
            first_half = nums[:idx + 1]
            second_half = nums[idx + 1:]
            nums.clear()
            nums = second_half + first_half

    elif command[0] == "max":
        if command[1] == "odd":
            counter = 0
            max_odd = -sys.maxsize
            for k in range(len(nums)):
                if nums[k] % 2 != 0:
                    counter += 1
                    if nums[k] > max_odd:
                        max_odd = nums[k]
            if counter == 0:
                print("No matches")
            else:
                index_odd = len(nums) - 1 - nums[::-1].index(max_odd)
                print(index_odd)
        elif command[1] == "even":
            counter = 0
            max_even = -sys.maxsize
            for k in range(len(nums)):
                if nums[k] % 2 == 0:
                    counter += 1
                    if nums[k] > max_even:
                        max_even = nums[k]
            if counter == 0:
                print("No matches")
            else:
                index_even = len(nums) - 1 - nums[::-1].index(max_even)
                print(index_even)

    elif command[0] == "min":
        if command[1] == "odd":
            counter = 0
            min_odd = sys.maxsize
            for k in range(len(nums)):
                if nums[k] % 2 != 0:
                    counter += 1
                    if nums[k] < min_odd:
                        min_odd = nums[k]
            if counter == 0:
                print("No matches")
            else:
                index_min_odd = len(nums) - 1 - nums[::-1].index(min_odd)
                print(index_min_odd)
        elif command[1] == "even":
            counter = 0
            min_even = sys.maxsize
            for k in range(len(nums)):
                if nums[k] % 2 == 0:
                    counter += 1
                    if nums[k] < min_even:
                        min_even = nums[k]
            if counter == 0:
                print("No matches")
            else:
                index_min_even = len(nums) - 1 - nums[::-1].index(min_even)
                print(index_min_even)

    elif command[0] == "first":
        if command[2] == "even":
            count = int(command[1])
            if count <= len(nums):
                even_count = 0
                first_even = []
                for k in range(len(nums)):
                    if even_count >= count:
                        break
                    else:
                        if nums[k] % 2 == 0:
                            first_even.append(nums[k])
                            even_count += 1
                print(first_even)
            else:
                print("Invalid count")
        elif command[2] == "odd":
            count = int(command[1])
            if count <= len(nums):
                odd_count = 0
                first_odd = []
                for k in range(len(nums)):
                    if odd_count >= count:
                        break
                    else:
                        if nums[k] % 2 != 0:
                            first_odd.append(nums[k])
                            odd_count += 1
                print(first_odd)
            else:
                print("Invalid count")

    elif command[0] == "last":
        if command[2] == "even":
            count = int(command[1])
            if count <= len(nums):
                even_count = 0
                last_even = []
                for k in range(len(nums) - 1, -1, -1):
                    if even_count >= count:
                        break
                    else:
                        if nums[k] % 2 == 0:
                            last_even.append(nums[k])
                            even_count += 1
                last_even.reverse()
                print(last_even)
            else:
                print("Invalid count")

        elif command[2] == "odd":
            count = int(command[1])
            if count <= len(nums):
                odd_count = 0
                last_odd = []
                for k in range(len(nums) - 1, -1, -1):
                    if odd_count >= count:
                        break
                    else:
                        if nums[k] % 2 != 0:
                            last_odd.append(nums[k])
                            odd_count += 1
                last_odd.reverse()
                print(last_odd)
            else:
                print("Invalid count")

    command = input().split()

print(nums)
