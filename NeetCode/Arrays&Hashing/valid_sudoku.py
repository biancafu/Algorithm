from collections import defaultdict
class Solution(object):
    #using hashmap to store each row, column and cube/block value
    #key will be the row/column/cube number, values will be stored in an array
    #if this array has the checked value stored already, then its wrong
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = defaultdict(list)
        column = defaultdict(list)
        cube = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == '.':
                    continue
                
                if (curr in row[i] or 
                curr in column[j] or 
                curr in cube[(i//3, j//3)]):
                    return False
                row[i].append(curr)
                column[j].append(curr)
                cube[(i//3, j//3)].append(curr)
        
        return True

    #using list 
    #we are storing in a big list with tuples of (row number, value), (column number, value), and (cube number, value)
    #when we put that list into set, if the len does not equal, that means there are repeated values
    #since sets don't carry duplicates
    def isValidSudoku_set(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))