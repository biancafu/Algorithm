class Connect4():
    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.board = [[0 for c in range(self.cols)] for r in range(self.rows)] 
        self.gameover = False
        self.winner = ""

    def is_column_available(self, col):
        return self.board[self.rows-1][col] == 0
    
    def get_next_slot(self, col): #next availble row
        for r in range(self.rows):
            if self.board[r][col] == 0:
                return r
            
    def drop_token(self, r, c, team):
        self.board[r][c] = team
    
    def print_board(self):
        print("------current board------")
        for i in range(self.rows-1, -1, -1):
            print(self.board[i])

    def winning_move(self, team):
        #horizontal
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if self.board[r][c] == team and self.board[r][c+1] == team and self.board[r][c+2] == team and self.board[r][c+3] == team:
                    return True
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if self.board[r][c] == team and self.board[r+1][c] == team and self.board[r+2][c] == team and self.board[r+3][c] == team:
                    return True
        
        for c in range(self.cols - 3):
            for r in range(self.rows - 3):
                if self.board[r][c] == team and self.board[r+1][c+1] == team and self.board[r+2][c+2] == team and self.board[r+3][c+3] == team:
                    return True
        
        for c in range(self.cols - 3):
            for r in range(3, self.rows):
                if self.board[r][c] == team and self.board[r-1][c+1] == team and self.board[r-2][c+2] == team and self.board[r-3][c+3] == team:
                    return True
    
    def start_game(self):
        print("game starts")
        turn = 0
        while not self.gameover:
            team = (turn%2)+1
            self.print_board()
            c = int(input("team"+ str(team) +": choose which column u want to drop your token? "))
            if self.is_column_available(c):
                r = self.get_next_slot(c)
                self.drop_token(r, c, team )
                if self.winning_move(team):
                    self.gameover = True
                    self.winner = str(team)
            turn += 1
        
        print("team"+self.winner+" has won the game!")
                


g = Connect4()
g.start_game()