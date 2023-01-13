import pygame
import numpy
import tkinter
from tkinter import messagebox


ROW_COUNT = 6
COLOUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE//2 - 5


def create_board():
    board = numpy.zeros((ROW_COUNT,COLOUMN_COUNT))   # creating a board of 6x7 of zeroes
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_input(col):
    global board
    if col >-1:
        return board[ROW_COUNT-1][col] ==0
    return False


def get_next_open_row(col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def winning_move(player, row, col):
    global board
    #horizontally
    for c in range(COLOUMN_COUNT-3):  #does not work for column and rows count other than 7 and 6, so do that
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == player:
                 return True
    #vertically
    for c in range(COLOUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == player:
                 return True
    #positive horizontal
    for c in range(COLOUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == player:
                 return True
    #negative diagonals
    for c in range(COLOUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == player:
                 return True


def print_board(board):  #not required in the final product
    print(numpy.flip(board, 0))


def draw_board(board):
    global height, width
    for c in range(COLOUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(mainwindow, (0, 0, 255), (c*SQUARE_SIZE, (r+1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(mainwindow, (0, 0, 0), (c*SQUARE_SIZE+SQUARE_SIZE//2, r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)

    for c in range(COLOUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c]==1:
                pygame.draw.circle(mainwindow, (255, 0, 0), (c*SQUARE_SIZE+SQUARE_SIZE//2, height-r*SQUARE_SIZE-SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(mainwindow, (255, 255, 0), (c*SQUARE_SIZE+SQUARE_SIZE//2, height-r*SQUARE_SIZE-SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)

    pygame.display.update()


def circle_at_top(position, color):
    global width
    pygame.draw.rect(mainwindow, (0,0,0), (0,0, width, SQUARE_SIZE))
    col = position[0] // SQUARE_SIZE
    pygame.draw.circle(mainwindow, color, (col*SQUARE_SIZE+SQUARE_SIZE//2, SQUARE_SIZE//2), RADIUS)


def new_game():
    global board
    board = create_board()


def message_box(subject, content):
    message = tkinter.Tk()
    message.attributes("-topmost",True)
    message.withdraw()
    messagebox.showinfo(subject, content)
    try:
        message.destroy()
    except:
        pass

def draw():
    global board
    if board.all():
        draw_board(board)
        message_box("Nobody won!", "Do you want to play again?")
        new_game()
        

pygame.init()
height = (ROW_COUNT+1)*SQUARE_SIZE
width = COLOUMN_COUNT*SQUARE_SIZE
mainwindow = pygame.display.set_mode((COLOUMN_COUNT*SQUARE_SIZE, height))
icon = pygame.image.load("C:\\mycode\\python\\PyGame\\Connect Four\\connect-four.png")
pygame.display.set_icon(icon)
turn = 0
board = create_board()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.MOUSEMOTION:
            if turn == 0:
                colour = (255,0,0)
            else:
                colour = (255, 255,0)
            circle_at_top(event.pos, colour)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn== 0:
                selection = event.pos[0] // SQUARE_SIZE  #column location
                if is_valid_input(selection):
                    row = get_next_open_row(col=selection)
                    drop_piece(board, row=row, col=selection, piece=1)
                    if winning_move(1, row, selection):
                        # print_board(board)
                        draw_board(board=board)
                        message_box("Player 1 wins!", "Do you want to play again?")
                        new_game()
                        break
            
            else:
                selection = event.pos[0] // SQUARE_SIZE  #column location
                if is_valid_input(selection):
                    row = get_next_open_row(col=selection)
                    drop_piece(board, row=row, col=selection, piece=2)
                    if winning_move(2, row, selection):
                        # print_board(board)
                        draw_board(board=board)
                        message_box("Player 2 wins!", "Do you want to play again?")
                        new_game()
                        break
            turn +=1
        turn = turn%2
    draw()
    draw_board(board=board)
