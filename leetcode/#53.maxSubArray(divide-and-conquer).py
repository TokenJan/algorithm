def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    else:
        mid = int(len(nums)/2)
        left_sum = maxSubArray(nums[:mid])
        right_sum = maxSubArray(nums[mid:])
        cross_sum = maxCrossArray(nums)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum
        else:
            return cross_sum

def maxCrossArray(nums):
    mid = int(len(nums)/2)
    left_max = float("-inf")
    right_max = float("-inf")
    sum = 0
    
    for i in range(mid-1, -1, -1):
        sum += nums[i]
        if sum > left_max:
            left_max = sum
            
    sum = 0
    for j in range(mid, len(nums)):
        sum += nums[j]
        if sum > right_max:
            right_max = sum
            
    return left_max + right_max

if __name__ == '__main__':
    array = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(array))