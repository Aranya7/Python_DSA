def msa(arr1,arr2):
    marray=[]
    a=0
    b=0
    while a<len(arr1) and b<len(arr2):
        if arr1[a]<arr2[b]:
            marray.append(arr1[a])
            a+=1

        else:
            marray.append(arr2[b])
            b+=1

    while a<len(arr1):
        marray.append(arr1[a])
        a+=1

    while b<len(arr2):
        marray.append(arr2[b])
        b+=1

    return marray

q=[1,4,23,99]
r=[3,16,17,101, 999]
ans=msa(q,r)
print(ans)