#내 풀이
class Solution:
    def IsPalindrom(self,target):
        for i in range(len(target)//2):
            if target[i] != target[len(target)-i-1]:
                return False
        return True 

    def longestPalindrome(self, s: str) -> str:
        last_idx = len(s)

        while last_idx !=0:
            for i in range(len(s)):
                result = s[i:i+last_idx]
                if self.IsPalindrom(result):
                    return result
            else:
                if len(s) <= i+last_idx:
                    break
                last_idx -= 1

        if last_idx <= 0:
            return None


#아래는 DP(Dynamic Programming)를 활용한 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str