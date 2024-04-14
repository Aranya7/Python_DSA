def merge_sort(arr, low, high):
    if low>=high:
        return
    mid = (low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left=low
    right=mid+1
    ans=[]
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            ans.append(arr[left])
            left+=1
        else:
            ans.append(arr[right])
            right+=1

    while left<=mid:
        ans.append(arr[left])
        left+=1

    while right<=high:
        ans.append(arr[right])
        right+=1

    for i in range(len(ans)):
        arr[low+i] = ans[i]


arr = [17, 7, 9, 143, 2642, 53, 420, 69, 1341, 1]
print(arr)
merge_sort(arr, 0, len(arr)-1)
print(arr)