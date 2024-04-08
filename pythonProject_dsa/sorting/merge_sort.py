def merge_sort(arr, s, e):
    if s>=e:
        return [arr[s]] if s == e else []
    mid = (e+s)//2
    left = merge_sort(arr, s, mid)
    right = merge_sort(arr, mid+1, e)
    return merge(left, right)

def merge(left, right):
    i=0
    j=0
    final=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            final.append(left[i])
            i+=1
        elif left[i]>right[j]:
            final.append(right[j])
            j+=1

    while i<len(left):
        final.append(left[i])
        i+=1

    while j<len(right):
        final.append(right[j])
        j+=1

    return final

arr=[17,7,9,143,2642,53,420,69,1341,1]
print(merge_sort(arr, 0, len(arr)-1))