def rec_fact(value):
    if value==2:
        return value
    return value*rec_fact(value-1)

def iter_fac(value):
    ans=1
    for i in range(value,0,-1):
        ans=ans*i
    return ans


print(iter_fac(5))
print(rec_fact(5))