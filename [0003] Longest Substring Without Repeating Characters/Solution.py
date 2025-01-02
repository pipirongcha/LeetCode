# 내 풀이로는 O(n^2) 만큼 걸렸다. 효율 측면에 있어 결코 좋지 못했다... 
class MyAnswer:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = list(s)
        substr_list = []
        result = 0

        for i in range(len(str_list)):
            substr_list = []
            for j in range(i, len(str_list)):
                if str_list[j] in substr_list:
                    break
                substr_list.append(str_list[j])
                result = max(result, len(substr_list))
                    
        return result
            

# 아래는 슬라이딩 윈도우 방식을 이용한 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() 
        left = 0
        max_length = 0

        for right in range(len(s)): 
            while s[right] in char_set: 
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length