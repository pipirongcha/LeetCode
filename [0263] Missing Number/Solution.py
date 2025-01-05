#내 풀이, O(2n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i]-1
        return len(nums)
    

#아래는 O(n) 풀이법
#i가 nums[i] 동일하지 않을 때만 리스트의 총 길이값에 해당 인덱스 값을 빼주는 방식
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res