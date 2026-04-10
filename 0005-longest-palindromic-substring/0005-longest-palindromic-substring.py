class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max_s=0
        str1=""
        for i in range(n):
            for j in range(i,n):
                s1=s[i:j+1]
                if s1==s1[::-1]:
                    if len(s1)>max_s:
                        str1=s1
                        max_s=len(s1)
        return str1