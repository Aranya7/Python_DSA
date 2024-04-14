def reversePairs(nums):
    # BF
    # count=0
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]>2*nums[j]:
    #             count+=1
    # return count

    def merge_sort(nums, s, e):
        count = 0
        if s >= e:
            return count
        mid = (s + e) // 2
        count += merge_sort(nums, s, mid)
        count += merge_sort(nums, mid + 1, e)
        count += countrevp(nums, s, mid, e)
        merge(nums, s, mid, e)
        return count

    def countrevp(nums, s, mid, e):
        right=mid+1
        count=0
        for i in range(s, mid+1):
            while right<=e and nums[i]>2*nums[right]:
                right+=1
            count+=(right-(mid+1))
        return count

    def merge(nums, s, mid, e):
        left = s
        right = mid + 1
        ans = []
        while left <= mid and right <= e:
            if nums[left] <= nums[right]:
                ans.append(nums[left])
                left += 1
            elif nums[right]<nums[left]:
                ans.append(nums[right])
                right += 1

        while left <= mid:
            ans.append(nums[left])
            left += 1
        while right <= e:
            ans.append(nums[right])
            right += 1

        for i in range(len(ans)):
            nums[s + i] = ans[i]

    return merge_sort(nums, 0, len(nums) - 1)

nums=[1,3,2,3,1]
print(reversePairs(nums))