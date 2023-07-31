#faster than 99% and memory 95% well !
#https://leetcode.com/problems/permutation-in-string/submissions/
def checkInclusion(s1, s2):
        f = {}
        for s in s1:
            if s in f:
                f[s] += 1
            else:
                f[s] = 1
        l = 0
        r = 0
        while r < len(s2):
            s = s2[r]

            if s not in f:
                if s2[l] in s1 and l < r:
                    f[s2[l]] = f.get(s2[l], 0) + 1
                    l += 1
                    continue
                else:
                    l += 1
                
            else: #s in f
                f[s] -= 1
                if f[s] == 0:
                    f.pop(s)
            r += 1
            if not f:
                return True
        return False

# a solution easier to understand
def checkInclusion(s1, s2):
        count1, count2 = 26 * [0], 26 * [0]
        if len(s1) > len(s2): return False
        for i, s in enumerate(s1):
            count1[ ord(s) - ord('a') ] += 1
            count2[ ord(s2[i]) - ord('a') ] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if count1 == count2:
                return True
            
            count2[ ord(s2[r]) - ord('a') ] += 1
            count2[ ord(s2[l]) - ord('a') ] -= 1
            l += 1
        
        return count1 == count2
                

            
            



            
            


a = checkInclusion("adc", "dcda")
print(a)