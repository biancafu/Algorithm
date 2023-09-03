class Solution(object):
    def letterCombinations(self, digits):
        #20 min (on the right track but madea mistake otherwise about 13 min)
        #each number can have 3-4 corresponding characters
        #for each digit, we will call itself recursively with the corresponding characters to create all possibile combinations
        level = []
        res = []
        numToChar = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(i):
            if i >= len(digits):
                if level:
                    res.append(''.join(level))
                return

            for i in range(i, len(digits)):
                chars = numToChar[digits[i]]
                for char in chars:
                    level.append(char)
                    dfs(i+1)
                    level.pop()
            
        
        dfs(0)
        return res




s = Solution()
a = s.letterCombinations("23")
print(a)