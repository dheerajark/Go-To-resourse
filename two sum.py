# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


def two_sum(arr, target):
    hash = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in hash:
            return [hash[complement], i]
        hash[num] = i
    return []


arr = [2, 7, 3, 4]
target = 11
result = two_sum(arr, target)
print(result)