def twoSum(nums, target):
    d = dict()
    for i in range(len(nums)):
        # dict.has_key only in Python2
        if d.has_key(target - nums[i]):
            return [d.get(target - nums[i]), i]
        else:
            d[nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))