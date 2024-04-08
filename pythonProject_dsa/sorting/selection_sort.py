def selection_sort_rec(arr):
    return helper(arr, 999999, 0)

def helper(arr, min, s):
    if s>len(arr)-1:
        return arr
    for i in range(s,len(arr)):
        if arr[i]<min:
            min=arr[i]
            ele=i
    temp = arr[s]
    arr[s] = arr[ele]
    arr[ele] = temp
    return helper(arr, 999999, s+1)

def selection_sort_iter(arr):
    counter = 0
    for i in range(0, len(arr)):
        min = 999999
        ele=-1
        for j in range(i, len(arr)):
            if arr[j]<min:
                min=arr[j]
                ele=j
        temp = arr[counter]
        arr[counter] = arr[ele]
        arr[ele] = temp
        counter+=1
    return arr

arr=[17,7,9,143,2642,53,420,69,1341,1]
print(selection_sort_iter(arr))
print(selection_sort_rec(arr))