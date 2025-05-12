import pygame
import os

"""Colors"""
white = (255,255,255)
black = (0,0,0)
darkgrey = (40,40,40)
lightgrey = (100,100,100)
green = (0,255,0)
darkgreen = (0,200,0)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
bg_color = darkgrey

"""Game Settings"""
tile_size = 32
rows = 15
columns = 15
amounts_of_mines = 5
width = tile_size*rows
height= tile_size*columns
fps = 60
title = "Minesweeper"

tile_numbers = []
for i in range(1,9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (tile_size, tile_size)))
    
tile_empty = (pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileEmpty.png")), (tile_size, tile_size)))
tile_exploded = (pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileExploded.png")), (tile_size, tile_size)))
tile_flag = (pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileFlag.png")), (tile_size, tile_size)))
tile_mine = (pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileMine.png")), (tile_size, tile_size)))
tile_not_mine = (pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileNotMine.png")), (tile_size, tile_size)))
tile_unknown = (pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileUnknown.png")), (tile_size, tile_size)))
print("Current working directory:", os.getcwd())