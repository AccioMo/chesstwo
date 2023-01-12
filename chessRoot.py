import pygame

pygame.init()

BOARD = 640
PIECE_SIZE = 60
SQUARE = 80
A1 = 40
A2 = A1+SQUARE
A3 = A2+SQUARE
A4 = A3+SQUARE
A5 = A4+SQUARE
A6 = A5+SQUARE
A7 = A6+SQUARE
A8 = A7+SQUARE

screen = pygame.display.set_mode((BOARD, BOARD))
clock = pygame.time.Clock()

yies = [A1, A2, A3, A4, A5, A6, A7, A8]
xies = yies
ss = [1, -1]

piece_touched = None
piece_played = None
WhiteTurn = True
black_in_check = False
white_in_check = False
virtual_position = None

chess_surf = pygame.image.load('.\\graphics\\chess1.png').convert_alpha()
kingW = pygame.image.load('.\\graphics\\kingW.png').convert_alpha()
kingB = pygame.image.load('.\\graphics\\kingB.png').convert_alpha()
queenW = pygame.image.load('.\\graphics\\queenW.png').convert_alpha()
queenB = pygame.image.load('.\\graphics\\queenB.png').convert_alpha()
bishopW = pygame.image.load('.\\graphics\\bishopW.png').convert_alpha()
bishopB = pygame.image.load('.\\graphics\\bishopB.png').convert_alpha()
knightW = pygame.image.load('.\\graphics\\knightW.png').convert_alpha()
knightB = pygame.image.load('.\\graphics\\knightB.png').convert_alpha()
rookW = pygame.image.load('.\\graphics\\rookW.png').convert_alpha()
rookB = pygame.image.load('.\\graphics\\rookB.png').convert_alpha()
pawnW = pygame.image.load('.\\graphics\\pawnW.png').convert_alpha()
pawnB = pygame.image.load('.\\graphics\\pawnB.png').convert_alpha()

chess_surf = pygame.transform.scale(chess_surf, (BOARD, BOARD))

piecesA = [rookW, knightW, bishopW, kingW, queenW, bishopW, knightW, rookW, pawnW, pawnW, pawnW, pawnW, pawnW, pawnW, pawnW, pawnW]
piecesB = [rookB, knightB, bishopB, kingB, queenB, bishopB, knightB, rookB, pawnB, pawnB, pawnB, pawnB, pawnB, pawnB, pawnB, pawnB]

p_rectA = []
p_rectB = []

x1 = A1
y1 = A8
for rectA in piecesA:
    p_rectA.append(rectA.get_rect(center=(x1, y1)))
    x1 += SQUARE
    if x1 == BOARD + A1:
        x1 = A1
        y1 -= SQUARE

x1 = A1
y1 = A1
for rectB in piecesB:
    p_rectB.append(rectB.get_rect(center=(x1, y1)))
    x1 += SQUARE
    if x1 == BOARD + A1:
        x1 = A1
        y1 += SQUARE

allpieces = p_rectA + p_rectB

