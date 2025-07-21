import random

class egoGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  
        self.winner = None
        self.game_over = False
        self.winning_line = None  
    
    def egoReset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  
        self.winner = None
        self.game_over = False
        self.winning_line = None
    
    def egoMove(self, row, col):
        if self.board[row][col] == ' ' and not self.game_over:
            self.board[row][col] = self.current_player
            
            if self.egoCheckWin():
                self.winner = self.current_player
                self.game_over = True
            elif self.egoCheckDraw():
                self.game_over = True
            else:
                
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            
            return True
        return False
    
    def egoCheckWin(self):
     
        for row in range(3):
            if self.board[row][0] != ' ' and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                self.winning_line = ('row', row)
                return True
        

        for col in range(3):
            if self.board[0][col] != ' ' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                self.winning_line = ('col', col)
                return True
        
    
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winning_line = ('diag', 1)
            return True
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winning_line = ('diag', 2)
            return True
        
        return False
    
    def egoCheckDraw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True
    
    def egoGetAvailableMoves(self):
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    moves.append((row, col))
        return moves
    
    def egoGetBoardCopy(self):
        return [row[:] for row in self.board]
