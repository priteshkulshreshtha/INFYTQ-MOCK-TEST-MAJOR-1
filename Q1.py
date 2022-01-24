nums = [2,7,11,15]
target = 9


def findNum(nums, target):
    d = {}
    
    for i, num in enumerate(nums):
        if target - num in d:
            return [i, d[target-num]]
        else:
            d[num] = i

print(findNum(nums, target))