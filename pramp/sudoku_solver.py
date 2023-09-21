#https://leetcode.com/problems/sudoku-solver/solutions/1417073/97-faster-clean-concise-well-explained/
#different than valid sudoku where we only check existing numbers, we are solving the sudoku here
#meaning that we will have to put different numbers in blank space to check
#this will be a backtracking problem because we will have to check all spaces to find a possible solution (go through all possible solutions)
#was on the right track, but got confused as i didn't think straight, i thought if we had to go through all possible solution will be to inefficient
#thought there was a "smarter/faster" to solve

#93% speed, 90% memory
from collections import defaultdict, deque
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        PAY ATTENTION TO DETAILS! (made 2 mistakes: first didn't notice the board is made of strings not numbers, 
        second when i copy and paste, i messed up the condition (used 2 rows in stead of rows and columns))
        """
        #mistake: pay attention to details!! the "numbers" stored are not numbers, they are string!!
        #use a hashset to store all existing numbers
        rows = defaultdict(set)
        columns = defaultdict(set)
        blocks = defaultdict(set)
        spaces = deque() #use a deque to store blank spaces so we can go back to previous step like the ones we do in backtracking (easier to append/pop)

        #add all existing numbers to the hashset
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    spaces.append((r,c))
                else:
                    rows[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    blocks[(r//3,c//3)].add(board[r][c])


        def dfs(): #use this recursie function to check all possible solution for blank spaces(deque)
            #base condition when its a possible solution:
            if not spaces: #no more spaces to check (all the others passed)
                return True

            r,c = spaces[0] #don't use popleft here, this is because we will need to pop within the for loop for it to balance with the append when cases failed, and we are reverting.
            #if we only have append, and we don't pop, we will end up appending repeating coordinates
            #check a possible num to traverse down:
            for num in {'1','2','3','4','5','6','7','8','9'}:
                #we have repeated numbers, so skip
                if num in rows[r] or num in columns[c] or num in blocks[(r//3,c//3)]:
                    continue
                #we found a possible number
                board[r][c] = num
                rows[r].add(num)
                columns[c].add(num)
                blocks[(r//3,c//3)].add(num)
                spaces.popleft()

                #if it succeeded, return True
                if dfs(): 
                    return True
                #failed this num, we will remove everything and add the spot back to q to try other numbers   
                else:
                    board[r][c] = "."
                    rows[r].remove(num)
                    columns[c].remove(num)
                    blocks[(r//3,c//3)].remove(num)
                    spaces.appendleft((r,c))
            
            #if we gone through everything and dont return a True, means we failed everything so return False
            return False
        
        dfs()


                    

