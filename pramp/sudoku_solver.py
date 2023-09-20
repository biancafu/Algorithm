#https://leetcode.com/problems/sudoku-solver/solutions/1417073/97-faster-clean-concise-well-explained/
#different than valid sudoku where we only check existing numbers, we are solving the sudoku here
#meaning that we will have to put different numbers in blank space to check
#this will be a backtracking problem because we will have to check all spaces to find a possible solution (go through all possible solutions)
#was on the right track, but got confused as i didn't think straight, i thought if we had to go through all possible solution will be to inefficient
#thought there was a "smarter/faster" to solve


from collections import defaultdict,deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
    
        rows,cols,block,seen = defaultdict(set),defaultdict(set),defaultdict(set),deque([])
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    block[(i//3,j//3)].add(board[i][j])
                else:
                    seen.append((i,j))
        
        def dfs():
            if not seen: #no board space
                return True
            
            r,c = seen[0] #the first empty spot
            t = (r//3,c//3)
            for n in {'1','2','3','4','5','6','7','8','9'}:
                if n not in rows[r] and n not in cols[c] and n not in block[t]: #no one else this number yet
                    board[r][c]=n #switch board spot to that number
                    rows[r].add(n) #add them to the map tracking rows, columns and block
                    cols[c].add(n)
                    block[t].add(n)
                    seen.popleft() #pop it off the seen (since its no longer a space)
                    if dfs(): #check if this new board can find a solution
                        return True #True if we can find one (by returning True from dfs call)
                    else: #if not, revert back (change the number to something else)
                        board[r][c]="."
                        rows[r].discard(n)
                        cols[c].discard(n)
                        block[t].discard(n)
                        seen.appendleft((r,c)) #put the empty spot back on the board
            #if nothing works, then we can't find a solution
            return False
        
        dfs()