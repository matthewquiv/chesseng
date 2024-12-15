import pygame, sys
from ChessBoard import Board
pygame.init()

def main():

    WIDTH, HEIGHT = 512, 512
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Board")

    board = Board(square_size=WIDTH//8)
    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        board.draw_squares(WINDOW)
        board.draw_pieces(WINDOW)
        pygame.display.update()

main()