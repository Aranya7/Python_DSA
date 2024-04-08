def quick_sort(arr, low, hi):
    if low>=hi:
        return
    s=low
    e=hi
    mid=(low+hi)//2
    p=arr[mid]
    while s<=e:
        while arr[s]<p:
            s+=1
        while arr[e]>p:
            e-=1

        if s<=e:
            temp = arr[s]
            arr[s]=arr[e]
            arr[e]=temp
            s+=1
            e-=1

    quick_sort(arr, low, e)
    quick_sort(arr, s, hi)

arr=[17,7,9,143,2642,53,420,69,1341,1]
quick_sort(arr, 0, len(arr)-1)
print(arr)