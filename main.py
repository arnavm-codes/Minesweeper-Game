import pygame
from sprites import *
from settings import *

def run(self):
    self.playing = True
    while self.playing:
        self.clock.tick(fps)
        self.events()
        self.draw()


def draw(self):
    self.screen.fill(bg_color)
    self.board.draw(self.screen)   
    pygame.display.flip()     
    

def events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)   
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()  
            mx //= tile_size # integer divide
            my //= tile_size # integer divide
            
            if event.button == 1: #left mouse button clicked
                if not self.board.board_list[mx][my].flagged:
                   # dig and check if exploded
                    if not self.board.dig(mx, my):
                     #explode    
                        for row in self.board.board_list:
                            for tile in row:
                                if tile.flagged and tile.type != "X":
                                    tile.flagged = False
                                    tile.revealed = True
                                    tile.image = tile_not_mine 
                                elif tile.type == "X":
                                    tile.revealed = True     
                        self.playing = False            
                    
    	    
            if event.button == 3: #right mouse button clicked
                if not self.board.board_list[mx][my].revealed:
                    self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged

game = Game()
while True:
    game.new()
    game.run()
