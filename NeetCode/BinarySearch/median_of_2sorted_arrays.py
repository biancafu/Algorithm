class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #mid point for A
            j = half - i - 2 # -2 because i is index (length would be i+1), total is length, we want j to be index so we need to -1 -> total - 1 - (i+1) = total - i - 2

            Aleft = A[i] #if i>=0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aright >= Bleft and Bright >= Aleft:
                return min(Aright, Bright) if total % 2 != 0 else (max(Aleft, Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            elif Bleft > Aright: 
                l = i + 1


s = Solution()
a = s.findMedianSortedArrays([1,2], [3,4])
print(a)