import pygame
import random

#constants

s_width = 800
s_height = 700
play_width = 300  
play_height = 600  
block_size = 30
n_block = 10
n_shapes = 7
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# SHAPE FORMATS
 #2D represent rotation
S = [[\'.....\',
      \'......\',
      \'..00..\',
      \'.00...\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..00.\',
      \'...0.\',
      \'.....\'
      ]]
 
Z = [[\'.....\',
      \'.....\',
      \'.00..\',
      \'..00.\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'.00..\',
      \'.0...\',
      \'.....\']]
 
I = [[\'..0..\',
      \'..0..\',
      \'..0..\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'0000.\',
      \'.....\',
      \'.....\',
      \'.....\']]
 
O = [[\'.....\',
      \'.....\',
      \'.00..\',
      \'.00..\',
      \'.....\']]
 
J = [[\'.....\',
      \'.0...\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..00.\',
      \'..0..\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'...0.\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..0..\',
      \'.00..\',
      \'.....\']]
 
L = [[\'.....\',
      \'...0.\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..0..\',
      \'..00.\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'.0...\',
      \'.....\'],
     [\'.....\',
      \'.00..\',
      \'..0..\',
      \'..0..\',
      \'.....\'
      ]]
 
T = [[\'.....\',
      \'..0..\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..00.\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'.00..\',
      \'..0..\',
      \'.....\'
      ]]

#globals

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

 
def create_grid(locked_positions={}):
    """
    locked_positions= dictionary ; position, color
    """
    grid = [ [ BLACK for x in range (10)] for x in range(20)]#20 rows 10 columns

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c #change color in the grid
    return grid
 
def convert_shape_format(shape):
    pass
 
def valid_space(shape, grid):
    pass
 
def check_lost(positions):
    pass
 
def get_shape():
    return random.choice(shapes)
 
 
def draw_text_middle(text, size, color, surface):
    pass
   
def draw_grid(surface, row, col):
    surface.fill(BLACK)
    #title
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, WHITE)
    #draw label at the middle of the screen
    surface.blit(label, (top_left_x, play_width/2-(label.get_width()/2), 30))

    for i in range (len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size), 0)
    
    pygame.draw.rect(surface, RED, (top_left_x, top_left_y, play_width, play_height))

    pygame.display.update()
 
def clear_rows(grid, locked):
    pass
 
 
def draw_next_shape(shape, surface):
    pass
 
 
def draw_window(surface):
    pass
 
def main():
    pass
 
def main_menu():
    pass
 
main_menu()