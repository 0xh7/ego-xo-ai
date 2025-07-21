import random

class egoAI:
    def __init__(self):
        self.player = 'O'  
        
    def setPlayer(self, symbol):
        self.player = symbol
        
    def egoMove(self, game):
        available_moves = game.egoGetAvailableMoves()
        
        if len(available_moves) == 9:
            return random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
        
        best_score = float('-inf')
        best_move = None
        
        opponent = 'O' if self.player == 'X' else 'X'

        for move in available_moves:
            row, col = move
            board_copy = game.egoGetBoardCopy()
            board_copy[row][col] = self.player
            
            score = self.egoMinimax(board_copy, 0, False, opponent)
            
            if score > best_score:
                best_score = score
                best_move = move
                
        return best_move
    
    def egoCheckWin(self, board, player):
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] == player:
                return True
                
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
                
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
            
        return False
    
    def egoIsDraw(self, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    return False
        return True

    def egoMinimax(self, board, depth, is_maximizing, opponent):
        if self.egoCheckWin(board, self.player):
            return 10 - depth
        elif self.egoCheckWin(board, opponent):
            return depth - 10
        elif self.egoIsDraw(board):
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = self.player
                        score = self.egoMinimax(board, depth + 1, False, opponent)
                        board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = opponent
                        score = self.egoMinimax(board, depth + 1, True, opponent)
                        board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score
