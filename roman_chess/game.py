# Шахматы - 5 практикум
abc_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

def print_color(color):
    return f'\033[{color}m'

class Figure:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return str(self.color)

    def is_valid_move(self, x1, y1, x2, y2, board):
        return False

    def print_str(self):
        print()

class Korol(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "К"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if (y2 - y1 == 0 and abs(x2 - x1) == 1) or (abs(y2 - y1) == 1 and x2 - x1 == 0) or (abs(y2 - y1) == 1 and abs(x2 - x1) == 1):
            if board.get_figure(x2, y2).image == "." or board.get_figure(x2, y2).color != self.color:
                return True
        else:
            return False

class Ferz(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "Ф"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if x1 != x2 and y1 != y2:
            if x1 == x2 or y1 == y2:
                if Ladya(self.color).is_valid_move(self, x1, y1, x2, y2, board):
                    return True
            elif abs(x1 - x2) == abs(y1 - y2):
                x_diag = 1 if x2 > x1 else -1
                y_diag = 1 if y2 > y1 else -1
                x_i = x1
                y_i = y1
                for i in range(0, abs(x1 - x2)-1, 1):
                    x_i += x_diag
                    y_i += y_diag
                    if board.get_figure(x_i, y_i).image != ".":
                        return False
                if board.get_figure(x2, y2).image == "." or board.get_figure(x2, y2).color != self.color:
                    return True


class Ladya(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "Л"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if x1 != x2 and y1 != y2:
            if x1 == x2:
                y_step = 1 if y2 > y1 else -1
                for i in range(y1 + y_step, y2, y_step):
                    if board.get_figure(x2, i).image != ".":
                        return False
                if board.get_figure(x2, y2).image != "." or board.get_figure(x2, y2).color != self.color:
                    return True
            elif y1 == y2:
                x_step = 1 if x2 > x1 else -1
                for j in range(x1 + x_step, x2, x_step):
                    if board.get_figure(j, y2).image != ".":
                        return False
                if board.get_figure(x2, y2).image != "." or board.get_figure(x2, y2).color != self.color:
                    return True


class Slon(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "С"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if (x1 != x2 and y1 != x2) and (abs(x1 - x2) == abs(y1 - y2)):
            if Ferz(self.color).is_valid_move(self, x1, y1, x2, y2, board):
                return True

class Kon(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "к"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if (abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or (abs(x2 - x1) == 1 and abs(y2 - y1) == 2):
            if board.get_figure(x2, y2).image == "." or board.get_figure(x2, y2).color != self.color:
                return True

class Peshka(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "П"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if self.color == 0:
            if y1 == y2:
                if board.get_figure(x2, y2).image == ".":
                    if x2 == x1 + 1:
                        return True
                    elif x2 == 3 and x1 == 1 and board.get_figure(x1+1, y1).image == ".":
                        return True
            elif (abs(y2 - y1) == 1) and (x2 - x1 == 1) and (board.get_figure(x2, y2).color == 1):
                return True
        elif self.color == 1:
            if y1 == y2:
                if board.get_figure(x2, y2).image == ".":
                    if x2 == x1 - 1:
                        return True
                    elif x2 == 4 and x1 == 6 and board.get_figure(x1-1, y1).image == ".":
                        return True
            elif (abs(y2 - y1) == 1) and (x1 - x2 == 1) and (board.get_figure(x2, y2).color == 0):
                return True

class Board:
    def __init__(self):
        pass

    def init_default(self):
        self.board = [["."] * 8 for i in range(8)]
        self.board[7][0:8:7] = Ladya(1), Ladya(1)
        self.board[7][1:7:5] = Kon(1), Kon(1)
        self.board[7][2:6:3] = Slon(1), Slon(1)
        for i in range(8):
            self.board[6][i] = Peshka(1)
            self.board[1][i] = Peshka(0)
        self.board[7][3] = Korol(1)
        self.board[7][4] = Ferz(1)
        self.board[0][0:8:7] = Ladya(0), Ladya(0)
        self.board[0][1:7:5] = Kon(0), Kon(0)
        self.board[0][2:6:3] = Slon(0), Slon(0)
        self.board[0][3] = Korol(0)
        self.board[0][4] = Ferz(0)
        self.white_turn = True

    def get_figure(self, x, y):
        return self.board[x][y]

    def set_figure(self, x, y, piece):
        self.board[x][y] = piece

    def move_figure(self, x1, y1, x2, y2):
        piece = self.get_figure(x1, y1)
        if not piece.is_valid_move(x1, y1, x2, y2, self):
            return False
        else:
            self.set_figure(x2, y2, piece)
            self.set_figure(x1, y1, ".")
            self.white_turn = not self.white_turn
            return True

    def print_board(self):
        abc_def = "   A   B   C   D   E   F   G   H"
        print(print_color(36), "{:^36}".format("Шахматы"), "\n", "-"*(len(abc_def)+2))
        print(print_color(0), abc_def, end="")
        for i in range(7, -1, -1):
            print(print_color(0))
            for j in range(8):
                if j == 0:
                    print(i+1, print_color(37), end="|")
                if str(self.board[i][j]) != ".":
                    if self.board[i][j].color != 0:
                        print(print_color("30;1"),end="")
                    else:
                        print(print_color("0;1"),end="")
                    print('{:^3}'.format(str(self.board[i][j])), end="")
                else:
                    print('{:^3}{:^3}'.format(print_color(37), str("-")), end="")
                print(print_color(37), end="|")
        print(print_color(36), "\n", "-"*(len(abc_def)+2))

class PlayChess:
    def __init__(self):
        self.board = Board()
        self.color_turn = 0

    def start(self):
        self.board.init_default()
        self.board.print_board()

    def game_input(self):
        pass
        # create input -> check -> move_figure(

    def game(self):
        pass
        # while True:
        #     x1, y1


board = Board()
board.init_default()
board.print_board()
