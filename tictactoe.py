import pygame, sys
import numpy as np

pygame.init()

# CONSTANTS-------------------------------------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 15
SQUARE_SIZE = 200
SPACE = 55 
ROWS = 3
COLS = 3
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (255, 255, 255)
CROSS_COLOR = (66, 66, 66)
# -----------------------------------------------

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)
                            # from-coord  to-coord  width
# pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)

board = np.zeros((ROWS, COLS))
print(board)

def draw_lines():
    # 1st horiz
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2nd horiz
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # 1st vert
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2nd vert
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures(row, col):
    # for row in range(ROWS):
    #     for col in range(COLS):
    if board[row][col] == 1:
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(col*200+100), int(row*200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
    elif board[row][col] == 2:
        pygame.draw.line(screen, RED, (col*200+SPACE, row*200+200-SPACE), (col*200+200-SPACE, row*200+SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

# checking if the square has been marked yet
def available_square(row, col):
    return board[row][col] == 0
    
    # if board[row][col] == 0:
    #     return True
    # else:
    #     return False

def is_board_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False
    return True

draw_lines()

player = 1

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX = event.pos[0] # x-coord
        mouseY = event.pos[1] # y-coord
        clicked_row = int(mouseY // SQUARE_SIZE)
        clicked_col = int(mouseX // SQUARE_SIZE)
        
        if available_square(clicked_row, clicked_col):
            mark_square(clicked_row, clicked_col, player)
            draw_figures(clicked_row, clicked_col)
            print(board)
            player = player%2 + 1
        
    pygame.display.update()
