# head={'value': 1, 'next': {'value': 10, 'next': {'value': 5, 'next': {'value': 15, 'next': None}}}}
# ok=head
# ok["next"]["next"]=2323
# print(ok)
# print(head)
#
# def find_dns_resolution_time(cache_size, cache_time, server_time, urls):
#     cache={}
#     ans=[]
#     for i in range(0,len(urls)):
#
#         if urls[i] in cache.values():
#             ans.append(cache_time)
#         else:
#             ans.append(server_time)
#         cache[i % cache_size] = urls[i]
#     for i in ans:
#         print(i)
#
#
# # Example Input
# cache_size = 3
# cache_time = 4
# server_time = 5
# urls = ["abc", "bcb", "abc", "cde", "qwe", "cde", "qwe"]
#
# # Output
# print(find_dns_resolution_time(cache_size, cache_time, server_time, urls))




# def ss(str, val, ans):
#     if val==len(str):
#         return ans
#     if str[val]=="a":
#         return ss(str, val+1, ans)
#     else:
#         return ss(str, val+1, ans+str[val])
#
# print(ss("baccad", 0, ""))

# class Solution(object):
#     def knightProbability(self, n, k, row, column):
#         """
#         :type n: int
#         :type k: int
#         :type row: int
#         :type column: int
#         :rtype: float
#         """
#
#         directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
#
#         def rec(n, k, r, c):
#             if r < 0 or r >= n or c < 0 or c >= n:
#                 return 0
#
#             if k == 0:
#                 return 1
#
#             ans = 0
#
#             for i in directions:
#                 ans += rec(n, k - 1, r + i[0], c + i[1]) / 8
#
#             return ans
#
#         if row < 0 or row >= n or column < 0 or column >= n:
#             return 0
#
#         return rec(n, k, row, column)


# def lengthOfLongestSubstring(s):
#     maxlen = 0
#     for i in range(0, len(s)):
#         track = {}
#         curans = ""
#         for j in range(i, len(s)):
#             if s[j] not in track:
#                 track[s[j]] = 1
#                 curans += s[j]
#                 maxlen = max(maxlen, len(curans))
#             else:
#                 break
#
#
#     return maxlen
#
# s="abcd"
# print(lengthOfLongestSubstring(s))
# def validPalindrome(s: str) -> bool:
#     i = 0
#     j = len(s) - 1
#     while i <= j:
#         if s[i] == s[j]:
#             i += 1
#             j -= 1
#         else:
#             tempstr1 = s[:i] + s[i + 1:]
#             tempstr2 = s[:j] + s[j + 1:]
#             if tempstr1 == tempstr1[::-1] or tempstr2 == tempstr2[::-1]:
#                 return True
#             else:
#                 return False
#     return False
#
# s = "abaca"
# print(validPalindrome(s))

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter=0
        curr=head
        hashmap={}
        while curr:
            if curr.val not in hashmap:
                hashmap[curr.val]=counter
                counter+=1
            else:
                return counter
            curr=curr.next