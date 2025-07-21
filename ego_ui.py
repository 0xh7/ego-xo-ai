import pygame
import time
# :) ههههههههه انا احب استخدم   اعرف اقدر اسويها  باي قيم   لكن  حبيت استخدم تايم   عشان اكون صريح معك
class egoUI:
    def __init__(self, game, ai, human_player):
        self.game = game
        self.ai = ai
        self.human_player = human_player  
        
       
        self.width = 600
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("ego  XO Game")
        
        
        
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.LIGHT_GRAY = (230, 230, 230)
        self.GRAY = (200, 200, 200)
        self.RED = (220, 50, 50)
        self.BLUE = (50, 100, 220)
        self.BG_COLOR1 = (240, 240, 245)
        self.BG_COLOR2 = (220, 230, 240)
        self.GRID_COLOR = (80, 80, 80)
        
       
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 80, bold=True)
        self.message_font = pygame.font.SysFont('Arial', 40)
        self.info_font = pygame.font.SysFont('Arial', 24)
        
       
        self.running = True
        self.restart_timer = 0
    
    def egoRun(self):
        clock = pygame.time.Clock()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game.game_over:
                    if self.game.current_player == self.human_player:  
                        self.egoHandleClick(event.pos)
            
           
            if self.game.current_player == self.ai.player and not self.game.game_over:
                move = self.ai.egoMove(self.game)
                if move:
                    row, col = move
                    self.game.egoMove(row, col)
            
            self.egoDraw()
            
            if self.game.game_over:
                current_time = time.time()
                if self.restart_timer == 0:
                    self.restart_timer = current_time
                elif current_time - self.restart_timer > 2: 
                   
                    if self.human_player == 'X':
                        self.human_player = 'O'
                        self.ai.setPlayer('X')
                    else:
                        self.human_player = 'X'
                        self.ai.setPlayer('O')
                    
                    self.game.egoReset()
                    self.restart_timer = 0
                    
                  
                    if self.ai.player == 'X':
                        move = self.ai.egoMove(self.game)
                        if move:
                            row, col = move
                            self.game.egoMove(row, col)
            
            pygame.display.flip()
            clock.tick(30)
    
    def egoHandleClick(self, pos):
        x, y = pos
        row = y // (self.width // 3)
        col = x // (self.width // 3)
     
        if 0 <= row < 3 and 0 <= col < 3:
            self.game.egoMove(row, col)
    
    def egoDraw(self):
     
        self.draw_gradient_background()
        
       
        self.draw_grid()
        
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 'X':
                    self.egoDrawX(row, col)
                elif self.game.board[row][col] == 'O':
                    self.egoDrawO(row, col)
        
        
        if self.game.game_over and self.game.winner and self.game.winning_line:
            self.egoDrawWinningLine()
        
       
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, 
                        (0, self.width, self.width, self.height - self.width))
        pygame.draw.line(self.screen, self.GRAY, (0, self.width), 
                        (self.width, self.width), 2)
        
        message = ""
        if self.game.game_over:
            if self.game.winner:
                message = f"Player {self.game.winner} wins"
             
                message_color = self.RED if self.game.winner == 'X' else self.BLUE
            else:
                message = "It a draw"
                message_color = self.GRAY
            
            text = self.message_font.render(message, True, message_color)
            self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.width + 50))
            
            restart_text = self.info_font.render("Restarting ....", True, self.GRAY)
            self.screen.blit(restart_text, (self.width // 2 - restart_text.get_width() // 2, self.width + 90))
        else:
            message = f"Player {self.game.current_player} turn"
            text = self.message_font.render(message, True, 
                                          self.RED if self.game.current_player == 'X' else self.BLUE)
            self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.width + 50))
    
    def draw_gradient_background(self):
        for y in range(self.width):
            
            color_ratio = y / self.width
            r = self.BG_COLOR1[0] * (1 - color_ratio) + self.BG_COLOR2[0] * color_ratio
            g = self.BG_COLOR1[1] * (1 - color_ratio) + self.BG_COLOR2[1] * color_ratio
            b = self.BG_COLOR1[2] * (1 - color_ratio) + self.BG_COLOR2[2] * color_ratio
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.width, y))
    
    def draw_grid(self):
        for i in range(1, 3):
           
            pygame.draw.line(self.screen, self.GRID_COLOR, (0, i * self.width // 3), 
                            (self.width, i * self.width // 3), 5)
           
            pygame.draw.line(self.screen, self.GRID_COLOR, (i * self.width // 3, 0), 
                            (i * self.width // 3, self.width), 5)
    
    def egoDrawX(self, row, col):
        # هنا نرسم الاكس  اعرف ان هذا اول تعليق تشوفه لكن حبيت اشكرك لانك تقرا الكود ممكن  حقا يفيدك مستقبلا 
        cell_size = self.width // 3
        padding = 30
        
        start_x = col * cell_size + padding
        start_y = row * cell_size + padding
        end_x = (col + 1) * cell_size - padding
        end_y = (row + 1) * cell_size - padding
        
       
        offset = 3
        pygame.draw.line(self.screen, (180, 30, 30), (start_x + offset, start_y + offset), 
                        (end_x + offset, end_y + offset), 8)
        pygame.draw.line(self.screen, (180, 30, 30), (start_x + offset, end_y + offset), 
                        (end_x + offset, start_y + offset), 8)
        
     
        pygame.draw.line(self.screen, self.RED, (start_x, start_y), (end_x, end_y), 8)
        pygame.draw.line(self.screen, self.RED, (start_x, end_y), (end_x, start_y), 8)
    
    def egoDrawO(self, row, col):
        # رسم  O
        cell_size = self.width // 3
        padding = 30
        center_x = col * cell_size + cell_size // 2
        center_y = row * cell_size + cell_size // 2
        radius = cell_size // 2 - padding
        
      
        for i in range(4):
            pygame.draw.circle(self.screen, (100, 150, 240, 50), 
                              (center_x, center_y), radius + 4 - i, 2)
        
     
        pygame.draw.circle(self.screen, self.BLUE, (center_x, center_y), radius, 8)
        
        
        pygame.draw.arc(self.screen, (120, 170, 255), 
                       (center_x - radius + 15, center_y - radius + 15, 
                        2 * radius - 30, 2 * radius - 30),
                       0.8, 2.8, 3)
    
    def egoDrawWinningLine(self):
        line_type, index = self.game.winning_line
        cell_size = self.width // 3
        line_color = self.RED if self.game.winner == 'X' else self.BLUE
        line_width = 10
        
        if line_type == 'row':
       
            start_x = 15
            end_x = self.width - 15
            y = index * cell_size + cell_size // 2
            pygame.draw.line(self.screen, line_color, (start_x, y), (end_x, y), line_width)
        
        elif line_type == 'col':
           
            x = index * cell_size + cell_size // 2
            start_y = 15
            end_y = self.width - 15
            pygame.draw.line(self.screen, line_color, (x, start_y), (x, end_y), line_width)
        
        elif line_type == 'diag':
            if index == 1:
              
                pygame.draw.line(self.screen, line_color, 
                                (15, 15), 
                                (self.width - 15, self.width - 15), 
                                line_width)
            else:
            
                pygame.draw.line(self.screen, line_color, 
                                (self.width - 15, 15), 
                                (15, self.width - 15), 
                                line_width)