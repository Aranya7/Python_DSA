def twoSum1(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return None

def twoSum2(nums, target):
    hm={}
    # if len(nums)<=1:
    #     return None
    for i in range(0, len(nums)):
        if target-nums[i] in hm:
            return [hm[target-nums[i]],i]
        else:
            hm[nums[i]]=i
    return None
print(twoSum1([1,3,7,9,2], 11))
print(twoSum2([1,3,7,9,2], 11))