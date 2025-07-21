import pygame
from ego_game import egoGame
from ego_ui import egoUI
from ego_ai import egoAI

def egoMain():
    pygame.init()
    
    game = egoGame()  
    ai = egoAI()
    
   
    human_player = 'X'
    ai.setPlayer('O')
   
    
    ui = egoUI(game, ai, human_player)
    
 
    if ai.player == 'X':
        move = ai.egoMove(game)
        if move:
            row, col = move
            game.egoMove(row, col)
    
    ui.egoRun()
    pygame.quit()

if __name__ == "__main__":
    egoMain()
