
    #neetcode solution, 82% speed 95% memory
    #understood the logic but didn't know how to implement the code

class Solution(object):
    def solveNQueens(self, n):
        res = []
        col = set() #keep track of columns
        #if in the same diagonal, the constant will be same (r-c will always = 0 for [0,0], [1,1] .. so on, so we know that if we see the same constant, that means a queen already exists in that diagonal)
        posDiag = set() #r+c (increasing r while decreasing c)
        negDiag = set() #r-c (both increasing)
        board = [["."] * n for i in range(n)]

        def backtrack(r): #increase r (no repeated rows)
            #breaking case
            if r == n:
                copy = ["".join(board[r]) for r in range(n)]
                res.append(copy)
                return

            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag: #already has a queen in same column or same diagonal, then skip
                    continue
                
                #otherwise, place a queen here
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1) 

                #cleanup
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res
                
                
                

        