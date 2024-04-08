## INCOMPLETE
def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[i]<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr

arr=[17,7,9,143,2642,53,420,69,1341,1]
print(insertion_sort(arr))

