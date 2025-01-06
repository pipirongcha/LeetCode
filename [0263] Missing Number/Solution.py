#내 풀이, O(2n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i]-1
        return len(nums)
    

#아래는 O(n) 풀이법
# (nums 길이) += (nums의 모든 인덱스 숫자의 합) - (nums 내 모든 value의 합) 을 구하는 방식으로 해결
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res