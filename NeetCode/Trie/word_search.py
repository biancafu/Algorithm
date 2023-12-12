# this question is actually in the backtracking part
# able to solve it after debugging (took about 15-20 min, debug took 10 min)
# 44% speed 35% memory (can be faster if we swap out len(board) with a variable, and move end of word to the top, when index == len(word) return True)
class Solution(object):
    def exist(self, board, word):
        """
        backtrack
        dfs function where it takes i,j from matrix and char of next 

        nested for loop go through whole matrix
        then dfs each one to see if it returns true

        mistake 1: careless, the boundary is i >= len(board) not >
        mistake 2: forgot to take care of visited cells
        """
        visited = set()
        def dfs(i,j, word_index): #using word index instead of slicing word for faster time (slicing is O(n)) 
            #breaking condition
            if (i < 0 or i >= len(board) or 
            j < 0 or j >= len(board[0]) or 
            (i,j) in visited or word[word_index] != board[i][j]):
            #didnt check for word >= len(word) because I am returning at last index of word so it wont go to wordindex+1 that round (wont go out of range)
                return False
            
            visited.add((i,j))
            #if its end of word and it matched (didnt return False), then we found the word
            if word_index == len(word)-1 :
                visited.remove((i,j))
                return True
     
            #other wise, keep on searching the next character
            result =  (dfs(i+1, j, word_index + 1) or 
            dfs(i-1, j, word_index + 1) or 
            dfs(i, j+1, word_index + 1) or 
            dfs(i, j-1, word_index + 1)
            )
            visited.remove((i,j))
            return result



        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0):
                    return True
        
        return False

        


s = Solution()
a = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
print(a)