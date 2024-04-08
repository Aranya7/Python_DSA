def revstring(abc):
    dee=""
    for i in range(len(abc)-1, -1, -1):
        dee+=abc[i]
    return dee

def revstr2(abc):
    return abc[::-1]

abcd="1234567"
r=revstring(abcd)
q=revstr2(abcd)
print(r)
print(q)
