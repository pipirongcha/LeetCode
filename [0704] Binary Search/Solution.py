# 내 o리컬시브 풀이, O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = len(nums)//2

        if target == nums[a]:
            return a
        if len(nums) == 1:
            return -1
            

        if target < nums[a]:
            reculsive = self.search(nums[:a],target)
            if reculsive == -1:
                return -1
            else:
                return reculsive 

        elif target > nums[a]:
            reculsive = self.search(nums[a:],target)
            if reculsive == -1:
                return -1
            else:
                return a  + reculsive

        
