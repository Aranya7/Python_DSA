def maxSubArray(nums):
    cursum = 0
    maxsum = float('-inf')
    for i in range(0, len(nums)):
        cursum = cursum + nums[i]
        if cursum > maxsum:
            maxsum = cursum
        if cursum < 0:
            cursum = 0
    return maxsum

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))