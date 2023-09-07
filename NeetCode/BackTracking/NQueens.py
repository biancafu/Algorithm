class Solution(object):
    #neetcode solution, 96% speed 40% memory
    #understood the logic but didn't know how to implement the code
    def solveNQueens(self, n):
        res = []
        col = set() #we don't need row, since we are placing 1 col in every row (no repeated rows)
        posDiag = set() #r+c = contant
        negDiag = set() #r-c = constant
        board = [["."] * n for i in range(n)]
            
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res
        