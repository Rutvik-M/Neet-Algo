class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=(total+1)//2
        if len(B)<len(A):
            A,B = B,A
        left,right=0,len(A)
        while left<=right:
            partA=(left+right)//2
            partB=half-partA
            leftA=float("-inf") if partA==0 else A[partA-1]
            rightA=float("inf") if partA==len(A) else A[partA]
            leftB = float("-inf") if partB==0 else B[partB-1]
            rightB=float("inf") if partB==len(B) else B[partB]
            if leftA<=rightB and leftB<=rightA:
                if total%2==0:
                    return (max(leftA,leftB)+min(rightA,rightB))/2
                return max(leftA,leftB)
            elif leftA>rightB:
                right=partA-1
            else:
                left=partA+1

