def bs(arr, target):
    s=0
    e=len(arr)-1
    while s<=e:
        mid = (s + e) // 2
        if arr[mid]==target:
            return True
        if arr[mid]<target:
            s=mid+1
        else:
            e=mid-1
    return False

arr=[2,4,6,12,621,7245,12441, 14791431]
print(bs(arr, 621))