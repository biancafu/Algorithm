#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# 5 min but not optimal

#my solution
def lengthOfLongestSubstring(self, s):
        arr = []
        maxlength = 0
        for c in s:
            while c in arr:
                arr.pop(0)
            arr.append(c)
            maxlength = max(maxlength, len(arr))

        return maxlength

#faster solution
def lengthOfLongestSubstring_faster(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        l = 0
        maxlength = 0
        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1 #update left pointer to pass the repeated number
            #can do else: maxlength ... (a bit less memory)
            maxlength = max(maxlength, r - l + 1)
            seen[c] = r

        return maxlength