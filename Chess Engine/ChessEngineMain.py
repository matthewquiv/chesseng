import pygame, sys
from ChessBoard import Board
from config import HEIGHT, WIDTH
pygame.init()

def main(): # Game loop
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Board")

    board = Board(square_size=WIDTH//8) # Defines board to have each square to be size 64x64
    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        board.draw_squares(WINDOW) #Draws Squares
        board.draw_pieces(WINDOW) # Draws pieces ... Will definitely be adjusted
        pygame.display.update()

main()