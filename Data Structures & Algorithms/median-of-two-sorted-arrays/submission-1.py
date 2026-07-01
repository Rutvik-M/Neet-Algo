class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=(total+1)//2
        left=0
        right=len(A)
        while left<=right:
            partitionA=(left+right)//2
            partitionB=half-partitionA
            leftA=float("-inf") if partitionA==0 else A[partitionA-1]
            rightA=float("inf") if partitionA==len(A) else A[partitionA]
            leftB=float("-inf") if partitionB==0 else B[partitionB-1]
            rightB=float("inf") if partitionB==len(B) else B[partitionB]
            if leftA<=rightB and leftB<=rightA:
                if total%2==0:
                    return (max(leftA,leftB)+min(rightA,rightB))/2
                return max(leftA,leftB)
            elif leftA>rightB:
                right=partitionA-1
            else:
                left=partitionA+1
        