def bubble_sort_rec(arr, s, e):
    if e==0:
        return arr
    for i in range(s, e):
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    return bubble_sort_rec(arr, s, e-1)

def bubble_sort_iter(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

arr=[17,7,9,143,2642,53,420,69,1341,1]
print(bubble_sort_rec(arr, 0, len(arr)-1))
print(bubble_sort_iter(arr))