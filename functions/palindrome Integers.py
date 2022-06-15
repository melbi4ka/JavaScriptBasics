def palinndrome_number(nums):
    for n in range(len(nums)):
        my_number = nums[n]
        temp = my_number
        reverse_num = 0

        while my_number > 0:
            digit = my_number % 10
            reverse_num = reverse_num * 10 + digit
            my_number = my_number // 10
        if temp == reverse_num:
            is_palindrome = True
        else:
            is_palindrome = False

        print(is_palindrome)



numbers = list(map(int, input().split(", ")))
palinndrome_number(numbers)


