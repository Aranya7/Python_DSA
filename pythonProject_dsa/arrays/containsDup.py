def contdup(nums):
    nums.sort()
    for i in range(0, len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

nums = [1,2,3,4]
nums2 = [1,2,3,1]

print(contdup(nums))
print(contdup(nums2))

def cd(nums):
    seen={}
    for i in nums:
        if i not in seen:
            seen[i]=True
        else:
            return True
    return False

print(cd(nums))
print(cd(nums2))