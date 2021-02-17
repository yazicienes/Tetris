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

top_left_x = (s_width - play_width) / 4
top_left_y = s_height - play_height
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

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
    positions  = []
    shape_format = shape.shape[shape.rotation % len(shape.shape)] #modulus for going back to shape 0
    for i, line in enumerate(shape_format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i )
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
def valid_space(shape, grid):
    """
    check if we are moving in to a valid space
    """
    accepted_pos = [[((j,i), for j in range (0,10) if grid (j,i) == WHITE] for i in range (20))]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True
    

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 
def get_shape():
    return Piece(5, -2, random.choice(shapes))#piece at middle of the screen and above screen
 
 
def draw_text_middle(text, size, color, surface):
    pass
   
def draw_grid_lines(surface, grid):
    #draw grid lines
    for i in range (len(grid)):
        pygame.draw.line(surface, GRAY, (top_left_x, top_left_y+ i*block_size), (top_left_x+play_width, top_left_y+ i*block_size))
        for j in range (len(grid[i])):
            pygame.draw.line(surface, GRAY, (top_left_x + j*block_size, top_left_y), (top_left_x+j*block_size, top_left_y+play_height))
 
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
    surface.blit(label, (top_left_x + play_width/2-(label.get_width()/2), 30))

    #draw grid
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
    
    pygame.draw.rect(surface, RED, (top_left_x, top_left_y, play_width, play_height), 4)

    draw_grid_lines(surface, grid)
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
    fall_speed = 0.27

    draw_window()
    
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y>0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid [y][x] = current_piece.color
        
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
                change_piece = True
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
        draw_window()
    
                    
                
 
def main_menu(win):
    main(win)
 
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption(('Tetris'))
main_menu(win)