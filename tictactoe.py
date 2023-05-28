import pygame
import sys
import numpy as np

pygame.init

#Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
Circle_Radius = 60
Circle_Width = 15
CROSS_WIDTH = 25
SPACE = 55


#color
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR =  (239, 231, 200)
CROSS_COLOR = (66, 66, 66)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOR )

#boards
boards = np.zeros( (BOARD_ROWS, BOARD_COLS) )

def draw_Figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if boards[row] [col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), Circle_Radius, Circle_Width)
            
            elif boards[row] [col] == 2:
                pygame.draw.line( screen, LINE_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), ( col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line( screen, LINE_COLOR, ( col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                
                

def mark_Square(Row, Col, Player):
    boards[Row, Col] = Player


def avilable_Square(Row, Col):
    if boards[Row] [Col] == 0:
        return True
    else:
        return False

def is_Board_Full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if boards[row] [col] == 0:
                return False
    
    return True


def Check_Win(player):
    for col in range(BOARD_COLS):
        if boards[0][col] == player and boards[1][col] == player and boards [2][col] == player:
            draw_Vertical_Winning_Line(col, player)
            return True
        
    #horizontal win check
    for row in range(BOARD_ROWS):
        if boards[row][0] == player and boards[row][1] == player and boards[row][2] == player:
            draw_Horizontal_Winning_Line(row, player)
            return True
        
    if boards[2][0] == player and boards[1][1] == player and boards [0][2] == player:
        draw_asc_Diagonal(player)
        return True
    
    if boards[0][0] == player and boards[1][1] == player and boards[2][2] == player:
        draw_desc_Diagonal(player) #error
        return True
    
    return False



def draw_Vertical_Winning_Line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT- 15), 15)

def  draw_Horizontal_Winning_Line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line( screen, color,(15, posY), (WIDTH -15, posY), 15)

def draw_asc_Diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    player.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH -15, 15), 15)

def draw_desc_Diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    player.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15) #error

def restart():
    screen.fill(BG_COLOR)
    draw_Lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            boards[row][col] = 0
    
def draw_Lines():
    #1st Horizontal Line
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    #2nd Horizontal Line
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

draw_Lines()

player = 1
game_Over = False

#main Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_Over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)


            if avilable_Square( clicked_row, clicked_col ):
                if player == 1:
                    mark_Square(clicked_row, clicked_col, 1)
                    if Check_Win(player): #error
                        game_Over = True
                    player = 2

                elif player == 2:
                    mark_Square(clicked_row, clicked_col, 2)
                    if Check_Win(player):
                        game_Over = True
                    player = 1
                draw_Figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_Over = False

    pygame.display.update()
