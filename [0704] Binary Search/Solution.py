# 내 리컬시브 풀이, O(log n)
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

        
# 내 반복문 풀이, O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = len(nums)//2
        high = len(nums)-1
        low = 0
        while low<=high:
            if target == nums[a]:
                return a

            if high == low and target != nums[a]:
                return -1 

            if target > nums[a]:
                low = a
                if (high+low)//2 == low:
                    low = high
                    a = high
                else:
                    a = (high+low)//2

            elif target < nums[a]:
                high = a
                if (high+low)//2 == high:
                    high = low
                    a = high
                else:
                    a = (high+low)//2
        return -1