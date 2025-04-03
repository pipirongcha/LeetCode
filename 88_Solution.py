class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp = []
        for i in range(m):
            tmp.append(nums1[i])
        for i in range(n):
            tmp.append(nums2[i])
        tmp.sort()
        for i in range(len(tmp)):
            if (i < len(nums1)):
                nums1[i] = tmp[i]
            else:
                nums1.append(tmp[i])
        