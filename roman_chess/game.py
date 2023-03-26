# Шахматы - 5 практикум - rtccreator
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


class Korol(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "К"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if (y2 - y1 == 0 and abs(x2 - x1) == 1) or (abs(y2 - y1) == 1 and x2 - x1 == 0) or (
                abs(y2 - y1) == 1 and abs(x2 - x1) == 1):
            if board.get_figure(x2, y2) == "." or board.get_figure(x2, y2).color != self.color:
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
        if (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2):
            if Ladya(self.color).is_valid_move(x1, y1, x2, y2, board):
                return True
        elif (x1 != x2 and y1 != y2) and (abs(x1 - x2) == abs(y1 - y2)):
            if Slon(self.color).is_valid_move(x1, y1, x2, y2, board):
                return True


class Ladya(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "Л"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if x1 == x2 and y1 != y2:
            y_step = 1 if y2 > y1 else -1
            for i in range(y1 + y_step, y2, y_step):
                if board.get_figure(x2, i) != ".":
                    return False
            if board.get_figure(x2, y2) != ".":
                if board.get_figure(x2, y2).color != self.color:
                    return True
            else:
                return True
        elif y1 == y2 and x1 != x2:
            x_step = 1 if x2 > x1 else -1
            for j in range(x1 + x_step, x2, x_step):
                if board.get_figure(j, y2) != ".":
                    return False
            if board.get_figure(x2, y2) != ".":
                if board.get_figure(x2, y2).color != self.color:
                    return True
            else:
                return True


class Slon(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "С"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if (x1 != x2 and y1 != y2) and (abs(x1 - x2) == abs(y1 - y2)):
            x_diag = 1 if x2 > x1 else -1
            y_diag = 1 if y2 > y1 else -1
            x_i = x1
            y_i = y1
            for i in range(0, abs(x1 - x2) - 1, 1):
                x_i += x_diag
                y_i += y_diag
                if board.get_figure(x_i, y_i) != ".":
                    return False
            if board.get_figure(x2, y2) == "." or board.get_figure(x2, y2).color != self.color:
                return True


class Kon(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "к"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if (abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or (abs(x2 - x1) == 2 and abs(y2 - y1) == 1):
            if board.get_figure(x2, y2) == "." or board.get_figure(x2, y2).color != self.color:
                return True
        else:
            return False


class Peshka(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.image = "П"

    def __repr__(self):
        return self.image

    def is_valid_move(self, x1, y1, x2, y2, board):
        if self.color == 0:
            if y1 == y2:
                if board.get_figure(x2, y2) == ".":
                    if x2 == x1 + 1:
                        return True
                    elif x2 == 3 and x1 == 1 and board.get_figure(x1 + 1, y1) == ".":
                        return True
            elif (abs(y2 - y1) == 1) and (x2 - x1 == 1) and (board.get_figure(x2, y2).color == 1):
                return True
        elif self.color == 1:
            if y1 == y2:
                if board.get_figure(x2, y2) == ".":
                    if x2 == x1 - 1:
                        return True
                    elif x2 == 4 and x1 == 6 and board.get_figure(x1 - 1, y1) == ".":
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
        self.black_turn = False

    def get_figure(self, x, y):
        if 0 <= x <= 7 and 0 <= y <= 7:
            return self.board[x][y]

    def set_figure(self, x, y, piece):
        self.board[x][y] = piece

    def move_figure(self, x1, y1, x2, y2):
        piece = self.get_figure(x1, y1)
        if not piece.is_valid_move(x1, y1, x2, y2, self):
            return False
        else:
            y_1 = list(filter(lambda x: abc_dict[x] == y1, abc_dict))[0]
            y_2 = list(filter(lambda x: abc_dict[x] == y2, abc_dict))[0]
            print(f"\nФигура \"{piece}\": {y_1}{x1 + 1} -> {y_2}{x2 + 1}\n")
            self.set_figure(x2, y2, piece)
            self.set_figure(x1, y1, ".")
            self.black_turn = not self.black_turn
            return True

    def print_board(self, win_check=0):
        if win_check == 0:
            abc_def = "   A   B   C   D   E   F   G   H"
            print(print_color(36), "{:^36}".format("Шахматы"), "\n", "-" * (len(abc_def) + 2))
            print(print_color(0), abc_def, end="")
            for i in range(7, -1, -1):
                print(print_color(0))
                for j in range(8):
                    if j == 0:
                        print(i + 1, print_color(37), end="|")
                    if str(self.board[i][j]) != ".":
                        if self.board[i][j].color != 0:
                            print(print_color("30;1"), end="")
                        else:
                            print(print_color("0;1"), end="")
                        print('{:^3}'.format(str(self.board[i][j])), end="")
                    else:
                        print('{:^3}{:^3}'.format(print_color(37), str("-")), end="")
                    print(print_color(37), end="|")
            print(print_color(36), "\n", "-" * (len(abc_def) + 2))
        else:
            board_list = [x for x in self.board]
            king_count = 0
            for i in board_list:
                for j in i:
                    if j != ".":
                        if j.image == "К":
                            if j.color == 0:
                                king_count += 1
                            elif j.color == 1:
                                king_count -= 1
            return king_count


class PlayChess:
    def __init__(self):
        self.board = Board()

    def start(self):
        self.board.init_default()
        self.board.print_board()
        print("\nХорошей игры! Белые начинают.")

    def game_play(self):
        while True:
            x1, y1 = self.game_input("Введите координаты фигуры: \n", 0)
            x2, y2 = self.game_input("Введите координаты точки назначения: \n", 1)
            if self.board.move_figure(x1, y1, x2, y2):
                who = "белые." if self.board.black_turn == False else "черные."
                self.board.print_board()
                win_check = self.board.print_board(1)
                if win_check != 0:
                    if win_check == 1:
                        print("\n\nБелые победили!\n\n")
                    else:
                        print("\n\nЧерные победили!\n\n")
                    break
                print(f"\nХодят {who}")
            else:
                print("На такую координату фигура пойти не сможет! Попробуйте снова!")

    def game_input(self, tip, move_step):
        while True:
            try:
                if move_step == 0:
                    user_input = str(input(tip)).upper()
                    y = abc_dict.get(user_input[0])
                    x = int(user_input[1]) - 1
                    if self.board.get_figure(x, y) != ".":
                        if self.board.get_figure(x, y).color == self.board.black_turn:
                            self.board.black_turn = not self.board.black_turn
                            move_step = 1
                            return x, y
                        else:
                            print("\nСейчас ходят белые!") if not self.board.black_turn else print(
                                "Сейчас ходят черные!")
                    else:
                        print("\nВы выбрали пустое поле. Повторите попытку!")
                else:
                    user_input = str(input(tip)).upper()
                    y = abc_dict.get(user_input[0])
                    x = int(user_input[1]) - 1
                    if self.board.get_figure(x, y) == ".":
                        self.board.black_turn = not self.board.black_turn
                        return x, y
                    elif self.board.get_figure(x, y).color == self.board.black_turn:
                        self.board.black_turn = not self.board.black_turn
                        return x, y
                    else:
                        print("Вы выбрали в качестве точки назначения позицию своей фигуры.\nПовторите попытку! \n")
            except:
                print("\nНеверный формат ввода!\nПожалуйста, вводите координаты "
                      "только в формате БукваЦифра \nот A до H и от 1 до 8, пример: a1 или H7.\n")


game = PlayChess()
game.start()
game.game_play()
