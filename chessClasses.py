from chessRoot import *

class Pieces:
    def __init__(self, piece, origin, color):
        self.piece = piece
        self.color = color
        self.piece_list, self.enemy_piece_list = self.getColor()
        self.Origin = origin
        self.originX = origin[0]
        self.originY = origin[1]

    def getColor(self):
        w_list = [p for p in p_rectA]
        b_list = [p for p in p_rectB]
        if self.color == "white": return w_list, p_rectB
        elif self.color == "black": return b_list, p_rectA

    # Makes next section more readable:
    def is_rook(self):
        if (self.piece_list).index(self.piece) == 0 or (self.piece_list).index(self.piece) == 7:
            return True
    def is_knight(self):
        if self.piece_list.index(self.piece) == 1 or self.piece_list.index(self.piece) == 6:
            return True
    def is_bishop(self):
        if self.piece_list.index(self.piece) == 2 or self.piece_list.index(self.piece) == 5:
            return True
    def is_king(self):
        if self.piece_list.index(self.piece) == 3:
            return True
    def is_queen(self):
        if self.piece_list.index(self.piece) == 4:
            return True
    def is_white_pawn(self):
        if self.piece_list == p_rectA and 8 <= self.piece_list.index(self.piece) <= 15:
            return True
    def is_black_pawn(self):
        if self.piece_list == p_rectB and 8 <= self.piece_list.index(self.piece) <= 15:
            return True

    # What piece was moved and where can it go:
    def getMoves(self):
        if self.is_rook():
            moves, capture_moves = self.rookMoves()

        elif self.is_knight():
            moves, capture_moves = self.knightMoves()

        elif self.is_bishop():
            moves, capture_moves = self.bishopMoves()

        elif self.is_king():
            moves, capture_moves = self.kingMoves()

        elif self.is_queen():
            moves, capture_moves = self.queenMoves()

        elif self.is_white_pawn() or self.is_black_pawn():
            moves, capture_moves = self.pawnMoves()
        
        self.moves_list = self.moveKingSafety(moves)
        self.capture_moves_list = self.moveKingSafety(capture_moves)

    def moveKingSafety(self, moves):
        o = (self.piece_list).index(self.piece)
        king_piece = self.piece_list[3]
        if o == 3:
            for move in moves:
                king = Pieces(king_piece, move, self.color)
                king.piece_list[o][0], king.piece_list[o][1] = move[0]-(PIECE_SIZE/2), move[1]-(PIECE_SIZE/2)
                if king.kingInDanger(): moves[moves.index(move)] = None
        else:
            for move in moves:
                king = Pieces(king_piece, king_piece.center, self.color)
                king.piece_list[o][0], king.piece_list[o][1] = move[0]-(PIECE_SIZE/2), move[1]-(PIECE_SIZE/2)
                if king.kingInDanger(): moves[moves.index(move)] = None
        moves = [x for x in moves if x != None]
        return moves

    # How the rooks move:
    def rookMoves(self):
        moves = []
        capture_moves = []
        for factor1 in ss:
            for pos in range(SQUARE, BOARD, SQUARE):
                self.move = [(self.originX + pos*factor1), (self.originY)]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                        break
                    else: moves.append(self.move)
                else: break
        for factor1 in ss:
            for pos in range(SQUARE, BOARD, SQUARE):
                self.move = [(self.originX), (self.originY + pos*factor1)]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                        break
                    else: moves.append(self.move)
                else: break
        return moves, capture_moves

    # How the knights move:
    def knightMoves(self):
        moves = []
        capture_moves = []
        for factor1 in ss:
            for factor2 in ss:
                self.move = [(self.originX + SQUARE*factor1*factor2), (self.originY + SQUARE*2*factor1)]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                    else: moves.append(self.move)
        for factor1 in ss:
            for factor2 in ss:
                self.move = [(self.originX + SQUARE*2*factor1*factor2), (self.originY + SQUARE*factor1)]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                    else: moves.append(self.move)
        return moves, capture_moves

    # How the bishops move:
    def bishopMoves(self):
        moves = []
        capture_moves = []
        for factor1 in ss:
            for pos in range(SQUARE, BOARD, SQUARE):
                self.move = [(self.originX + pos*factor1), (self.originY + pos*factor1)]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                        break
                    else: moves.append(self.move)
                else: break
        for factor1 in ss:
            for pos in range(SQUARE, BOARD, SQUARE):
                self.move = [(self.originX + pos*factor1), (self.originY - pos*factor1)]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                        break
                    else: moves.append(self.move)
                else: break
        return moves, capture_moves

    # How the king moves
    def kingMoves(self):
        moves = []
        capture_moves = []
        for factor1 in ss:
            for factor2 in ss:
                self.move = [self.originX + SQUARE*factor1*factor2, self.originY + SQUARE*factor1]
                if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                    else: moves.append(self.move)
            self.move = [self.originX + SQUARE*factor1, self.originY]
            if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                    else: moves.append(self.move)
            self.move = [self.originX, self.originY + SQUARE*factor1]
            if all(0 <= it <= BOARD for it in self.move) and self.checkForFriend():
                    if self.checkForEnemy():
                        capture_moves.append(self.move)
                    else: moves.append(self.move)
        return moves, capture_moves

    # How the queen moves:
    def queenMoves(self):
        moves, capture_moves = [m+c for m,c in zip(self.bishopMoves(), self.rookMoves())]
        return moves, capture_moves

    # How the pawns move:
    def pawnMoves(self):
        moves = []
        capture_moves = []
        s = 1
        place = A2
        if self.color == "white":
            s = -1
            place = A7
        self.move = [self.originX, self.originY + SQUARE*s]
        if all(0 <= it <= BOARD for it in self.move) and not any(piece and list(piece.center) == self.move for piece in allpieces):
            moves.append(self.move)
            self.move = [self.originX, self.originY + SQUARE*s*2]
            if all(0 <= it <= BOARD for it in self.move) and self.originY == place and not any(piece and list(piece.center) == self.move for piece in allpieces):
                moves.append(self.move)
        for factor in ss:
            self.move = [self.originX + SQUARE*s*factor, self.originY + SQUARE*s]
            if all(0 <= it <= BOARD for it in self.move) and self.checkForEnemy() and self.checkForFriend():
                capture_moves.append(self.move)
        return moves, capture_moves

    # Checks if there is an frindly piece on a square:
    def checkForFriend(self):
        if any(piece and list(piece.center) == self.move for piece in self.piece_list): return False
        else: return True

    # Checks if there is an enemy piece on the square:
    def checkForEnemy(self):
        if any(piece and list(piece.center) == self.move for piece in self.enemy_piece_list): return True
        else: return False

    # Returns True if the King is in check;
    def kingInDanger(self):
        for move in self.rookMoves()[1]:
            if self.enemy_piece_list[0] and move == list(self.enemy_piece_list[0].center):
                return True
            elif self.enemy_piece_list[7] and move == list(self.enemy_piece_list[7].center):
                return True
            elif self.enemy_piece_list[4] and move == list(self.enemy_piece_list[4].center):
                return True
        for move in self.knightMoves()[1]:
            if self.enemy_piece_list[1] and move == list(self.enemy_piece_list[1].center):
                return True
            elif self.enemy_piece_list[6] and move == list(self.enemy_piece_list[6].center):
                return True
        for move in self.bishopMoves()[1]:
            if self.enemy_piece_list[2] and move == list(self.enemy_piece_list[2].center):
                return True
            elif self.enemy_piece_list[5] and move == list(self.enemy_piece_list[5].center):
                return True
            elif self.enemy_piece_list[4] and move == list(self.enemy_piece_list[4].center):
                return True
        for move in self.kingMoves()[1]:
            if self.enemy_piece_list[3] and move == list(self.enemy_piece_list[3].center):
                return True
        for move in self.pawnMoves()[1]:
            if any(enemy and move == list(enemy.center) for enemy in self.enemy_piece_list[8:16]):
                return True
        return False

    def movePiece(self, Destination):
        self.move = Destination
        if list(self.Origin) != Destination:
            for move in (self.moves_list+self.capture_moves_list):
                if move == Destination:
                    (self.piece).center = Destination
                    if self.checkForEnemy():
                        self.enemy_piece_list[(self.enemy_piece_list).index(self.piece)] = None
                    return True
            (self.piece).center = self.Origin
            return None
        else:
            (self.piece).center = self.Origin
            return False
