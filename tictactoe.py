import pygame, sys
import numpy as np

pygame.init()

# CONSTANTS-------------------------------------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
ROWS = 3
COLS = 3
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
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

def mark_squares(row, col, player):
    board[row][col] = player

# checking if the square has been marked yet
def available_square(row, col):
    return board[row][col] == 0
    
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False
    return True

draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] # x-coord
            mouseY = event.pos[1] # y-coord
            
    
    pygame.display.update()

