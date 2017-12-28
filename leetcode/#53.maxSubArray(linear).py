def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cum_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        cum_sum = max(nums[i], cum_sum + nums[i])
        max_sum = max(cum_sum, max_sum)
    return max_sum

if __name__ == '__main__':
    array = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(array))