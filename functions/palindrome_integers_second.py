def palinndrome_number(nums):
    for n in nums:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palinndrome_number(numbers)
