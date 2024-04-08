#0,1,1,2,3,5,8,13,21,34,55,89...
def rec_fib(value):
    if value<=1:
        return value
    return rec_fib(value-1)+rec_fib(value-2)

def iter_fib(value):
    arr=[0,1]
    for i in range(2,value+1):
        arr.append(arr[i-2]+arr[i-1])
    return arr[value]

print(iter_fib(11))
print(rec_fib(11))