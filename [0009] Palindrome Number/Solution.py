#내 풀이, 전날에 짜봤던 함수랑 거의 같은 구조여서 쉽게 풀렸다
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        for i in range(len(tmp)//2):
            if tmp[i] != tmp[len(tmp)-i-1]:
                return False
        return True 
        