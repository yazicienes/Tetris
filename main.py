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

top_left_x = 0
top_left_y = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# SHAPE FORMATS
 #2D represent rotation
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....'
      ]]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....'
      ]]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....'
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
    return Piece(5, -2, random.choice(shapes))#piece at middle of the screen and above screen
 
 
def draw_text_middle(text, size, color, surface):
    pass
   
def draw_grid(surface, grid):
    #draw grid
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size), 0)
    
    pygame.draw.rect(surface, RED, (top_left_x, top_left_y, play_width, play_height), 4)

 
def clear_rows(grid, locked):
    pass
 
 
def draw_next_shape(shape, surface):
    pass
 
 
def draw_window(surface, grid):
    surface.fill(BLACK)
    #title
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, WHITE)
    #draw label at the middle of the screen
    surface.blit(label, (top_left_x, play_width/2-(label.get_width()/2), 30))

    draw_grid(surface, grid)
    pygame.display.update()
 
def main(win):
    locked_positions ={}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation +=1
                    if not (valid_space(current_piece, grid)):
                        current_piece -= 1
    draw_window(win, grid)
                    
                
 
def main_menu(win):
    main(win)
 
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption(('Tetris'))
main_menu(win)