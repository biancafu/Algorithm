
def solve(board):
    """
    *mistake: it didn't cross my mind that if one of the region's surrounding is a border 'O' this would mean that it has to be neighbor with the boarder hence forming the region tgt with the border O which means that it is the same region *
    with that in mind, it is easier to solve this question
    - differentiate which regions are the border regions, and we can do that by doing a dfs on the boarder Os
    - flip all the unmakred O's (not boarder ones) into X since it WOULD be flippable (surrounded by X) because our border O's dfs search would mark the unflippable ones (connected to border region)
    - flip all the makred O's back to regular O's (boarder Os)
    """
    m = len(board)
    n = len(board[0])
    

    def dfs(r,c):
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            return
        
        #mark border Os into T
        board[r][c] == 'T'
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    

    #differentiate boarder regions and normal regions
    #all rows boarder
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i,0)
        if board[i][n-1] == 'O':
            dfs(i,n-1)
    #all columns except first and last (becuz already check on rows)
    #easier to just do nested for loop, but i want min time
    for j in range(1,n-1):
        if board[0][j] == 'O':
            dfs(0,j)
        if board[m-1][j] == 'O':
            dfs(m-1,j)
    
    print(board)
    #we can do the 2 steps tgt becuz we will not revisit therefore the Os turned from T will stay as Os
    for i in range(m):
        for j in range(n):
            #flip the rest of the Os into X
            if board[i][j] == 'O':
                board[i][j] == 'X'
            #flip the Ts (boarder Os) back into Os
            elif board[i][j] == 'T':
                board[i][j] == 'O'


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

solve(board)
print(board)       