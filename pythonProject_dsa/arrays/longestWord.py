def LongestWord(sen):
  a=sen.split()

  max_len=0
  max_ele=-1
  for i in range(0,len(a)):
    if len(a[i])>max_len:
        # print(i)
        # print(len(i))
        max_len=len(a[i])
        max_ele=i
  # code goes here
  return a[max_ele]

print(LongestWord("I love dog"))