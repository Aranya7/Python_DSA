def mz(nums):
    a=0
    for i in nums:
        if i!=0:
            nums[a]=i
            a+=1

    for i in range(a,len(nums)):
        nums[i]=0
    return nums




nums=[0,0,1]


abcd=mz(nums)
print(abcd)