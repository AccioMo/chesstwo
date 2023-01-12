from chessClasses import *
from sys import exit
import itertools

def getPiece(piece_list):
    for piece in piece_list:
        if piece and piece.collidepoint(pygame.mouse.get_pos()):
            piece_origin = piece.center
            return piece, piece_origin
        else: pass
    return None

def checkinPosition(piece):
        dx = BOARD
        dy = BOARD
        for x in xies:
            if abs(piece[0] - x) <= abs(dx):
                dx = piece[0] - x
        for y in yies:
            if abs(piece[1] - y) <= abs(dy):
                dy = piece[1] - y
        Destination = [(piece[0] - dx), (piece[1] - dy)]
        return Destination

def setting_board(rect_pieces, img_pieces):
    for pA, p_A in itertools.zip_longest(img_pieces, rect_pieces):
        if p_A:
            screen.blit(pA, p_A)

# Main Game Loop:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255,255,255))
    screen.blit(chess_surf, (0, 0))

    setting_board(p_rectA, piecesA)
    setting_board(p_rectB, piecesB)

    if piece_played:
        for move in piece_played.moves_list:
            pygame.draw.circle(screen, (0,100,0), (move[0], move[1]), 10)

    if black_in_check:
        pygame.draw.rect(screen, (255,0,0), p_rectB[3], 4)

    if black_in_check:
        pygame.draw.rect(screen, (64,64,64), piece_touched, 4)

    if piece_played:
        for move in piece_played.capture_moves_list:
            pygame.draw.rect(screen, (0,100,0), (move[0]-30,move[1]-30,60,60), 3)

    if WhiteTurn == True:
        if pygame.mouse.get_pressed()[0]:
            clicked_piece = getPiece(p_rectA)
            if piece_touched and not piece_played:
                piece_touched.center = pygame.mouse.get_pos()
            elif clicked_piece:
                piece_touched, piece_origin = clicked_piece
                if piece_played: piece_played = None
        if piece_touched and event.type == pygame.MOUSEBUTTONUP:
            if not piece_played:
                piece_played = Pieces(piece_touched, piece_origin, "white")
                piece_played.getMoves()
            else: pass
            Destination = checkinPosition(pygame.mouse.get_pos())
            outcome = piece_played.movePiece(Destination)
            if outcome is True:
                WhiteTurn = False
                piece_touched = None
                piece_played = None
                print("moved piece")
            else:
                if outcome is None:
                    piece_touched = None
                    piece_played = None
                    print("wrong move")
                else: pass
        elif not pygame.mouse.get_pressed()[0] and piece_touched and piece_touched.center != piece_origin:
            piece_touched.center = piece_origin
            print("it works")

    elif WhiteTurn == False:
        if pygame.mouse.get_pressed()[0]:
            clicked_piece = getPiece(p_rectB)
            if piece_touched and not piece_played:
                piece_touched.center = pygame.mouse.get_pos()
            elif clicked_piece:
                piece_touched, piece_origin = clicked_piece
                if piece_played: piece_played = None
        if piece_touched and event.type == pygame.MOUSEBUTTONUP:
            if not piece_played:
                piece_played = Pieces(piece_touched, piece_origin, "black")
                piece_played.getMoves()
            else: pass
            Destination = checkinPosition(pygame.mouse.get_pos())
            outcome = piece_played.movePiece(Destination)
            if outcome is True:
                WhiteTurn = True
                piece_touched = None
                piece_played = None
                print("moved piece")
            else:
                if outcome is None:
                    piece_touched = None
                    piece_played = None
                    print("wrong move")
                else: pass
        elif not pygame.mouse.get_pressed()[0] and piece_touched and piece_touched.center != piece_origin:
            piece_touched.center = piece_origin
            print("it works")
        # if Pieces.moving(p_rectB, p_rectA):
        #     executeOrder(p_rectA)
        #     black_in_check = False
        #     WhiteTurn = True
        #     piece_touched = False
        #     moves.clear()
        #     print("White's Turn")
        #     if kingSafety(p_rectB, p_rectA):
        #         white_in_check = True
        #         moves.clear()
        #         for piece in p_rectA:
        #             if piece:
        #                 getMoves(piece, p_rectA, p_rectB)
        #         if not moves:
        #             print("CHECKMATE")
        #             pygame.Surface.fill(screen, (0,0,0))
        #         moves.clear()

    pygame.display.update()
    clock.tick(60)
    