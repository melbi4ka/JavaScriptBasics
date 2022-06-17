def sorted_nums(nums):
    nums.sort()
    return nums


numbers = list(map(int, input().split()))
print(sorted_nums(numbers))
