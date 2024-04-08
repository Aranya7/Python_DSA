# Google - Return the first number that repeats itself

def frc(arr):
    hm={}
    for i in range(0, len(arr)):
        if arr[i] not in hm.keys():    # We can use just hm instead of hm.keys() here
            hm[arr[i]]=1
        else:
            return arr[i]



abc=[5,1,2,7,23,753,843,234,6,7]
print(frc(abc))


