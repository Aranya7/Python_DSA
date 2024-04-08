def rec_stringrev(str, i):
    if i==len(str):
        return

    rec_stringrev(str, i+1)
    print(str[i], end="")

def iter_stringrev(sr):
    for i in range(len(str)-1, -1, -1):
        print(str[i], end="")

str="yoyo master"
rec_stringrev(str, 0)
print("\nXX")
iter_stringrev(str)
# print(str[::-1])
