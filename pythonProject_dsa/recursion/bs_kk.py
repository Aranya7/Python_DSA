def bs(arr, target, s, e):
    if s > e:
        return -1
    mid=(s+e)//2
    if arr[mid]==target:
        return mid
    if arr[mid]<target:
        return bs(arr, target, mid+1, e)
    if arr[mid]>target:
        return bs(arr, target, s, mid-1)

arr=[2,4,6,12,621,7245,12441, 14791431]
print(bs(arr, 6251, 0, len(arr)-1))