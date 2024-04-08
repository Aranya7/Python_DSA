def rotate1(nums, k):
    for i in range(k):
        a = nums.pop()
        nums.insert(0, a)
    return nums

nums=[1,2,3,4,5,6,7]
print(rotate1(nums,3))

