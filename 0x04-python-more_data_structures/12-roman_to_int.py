#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if len(roman_string) == 0:
        return 0
    if str(roman_string) != roman_string:
        return 0
    vals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    nums = list()
    for ch in roman_string:
        nums.append(vals.get(ch, 0))

    left = nums[0]
    for i in range(1, len(nums)):
        right = nums[i]
        four = (left == 1 and right == 5)
        nine = (left == 1 and right == 10)
        forty = (left == 10 and right == 50)
        ninety = (left == 10 and right == 100)
        fourhund = (left == 100 and right == 500)
        ninehund = (left == 100 and right == 1000)
        if four or nine or forty or ninety or fourhund or ninehund:
            nums[i-1] = right - left
            nums[i] = 0
        left = nums[i]

    return sum(nums)
