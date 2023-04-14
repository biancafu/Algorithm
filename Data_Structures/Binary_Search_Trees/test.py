def print_chessboard(dim):
    Wline = ""
    Bline = ""
    for i in range(0, dim):
        if i % 2 == 0:
            Wline += "W "
            Bline += "B "
        else:
            Wline += "B "
            Bline += "W "
    
    for i in range(0, dim):
        if i % 2 == 0:
            print(Wline)
        else:
            print(Bline)
 
print_chessboard(3)

def get_chessboard(dim):
    chessboard = [[None for i in range(dim)] for j in range(dim)]
    
    for i in range(dim * dim):
        m, n = divmod(i, dim)
        
        if (m + n) % 2:
            chessboard[m][n] = 'B'
        else:
            chessboard[m][n] = 'W'
    
    return chessboard

print(get_chessboard(3))