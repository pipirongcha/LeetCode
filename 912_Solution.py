class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.MergeSort(nums, 0, len(nums)-1)
        return nums

    def MergeSort(self, nums, left, right):
        if(left>= right):
            return

        mid = (left+right)//2
        
        self.MergeSort(nums, left, mid)
        self.MergeSort(nums, mid+1, right)
        self.Merge(nums, left, right, mid)

    def Merge(self, nums, left, right, mid):
        tmp = []
        i = left
        j = mid+1

        while(i <= mid and j <= right):
            if(nums[i] < nums[j]):
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        
        while(i <= mid):
            tmp.append(nums[i])
            i += 1
        
        while(j <= right):
            tmp.append(nums[j])
            j += 1

        for l in range(len(tmp)):
            nums[left+l] = tmp[l]