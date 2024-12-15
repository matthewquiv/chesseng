import pygame
class Board:
    WHITE = (255, 255, 255)
    GREEN = (34,139,34)
    def __init__(self, square_size=64):
        self.square_size = square_size

    def create_initial_board(self):
        return [
            ["br", "bkn", "bb", "bq", "bki", "bb", "bkn", "br"],
            ["bp"]*8,
            [None]*8,
            [None]*8,
            [None]*8,
            [None]*8,
            ["wp"]*8,
            ["wr", "wkn", "wb", "wq", "wki", "wb", "wkn", "wr"]
        ]

    def draw_squares(self, window):
        width, height = window.get_size()
        cols = height // self.square_size
        rows = width // self.square_size
        for row in range(rows):
            for col in range(cols):
                color = self.WHITE
                if (row + col) % 2 == 1:
                    color = self.GREEN
                pygame.draw.rect(window, color, (row * self.square_size, col*self.square_size, width//cols, height//rows))
    def draw_pieces(self, window):
        pieces = {
            "wp" : pygame.image.load("images/white-bpawn2.png"),
            "wr" : pygame.image.load("images/white-rook.png"),
            "wkn": pygame.image.load("images/white-archbis.png"),
            "wb" : pygame.image.load("images/white-bishop.png"),
            "wki" : pygame.image.load("images/white-king.png"),
            "wq" : pygame.image.load("images/white-amazon.png"),
            "bp" : pygame.image.load("images/black-bpawn2.png"),
            "br" : pygame.image.load("images/black-rook.png"),
            "bkn": pygame.image.load("images/black-archbis.png"),
            "bb" : pygame.image.load("images/black-bishop.png"),
            "bki" : pygame.image.load("images/black-king.png"),
            "bq" : pygame.image.load("images/black-amazon.png")
            }
        for key in pieces:
                pieces[key] = pygame.transform.scale(pieces[key], (self.square_size, self.square_size))
        width, height = window.get_size()
        cols = width // self.square_size
        rows = height // self.square_size
        board = self.create_initial_board()
        for row in range(rows):
            for col in range(cols):
                for key in pieces:
                    if board[row][col] == key:
                        print(row, col)
                        window.blit(pieces[key], (col * self.square_size, row * self.square_size))