WHITE = 0
BLACK = 1
BOARD_SIZE = 8

class ReversiBoard(object):
    def __init__(self):
        self.cells = []
        for i in range(BOARD_SIZE):
            self.cells.append([None for i in range(BOARD_SIZE)])
        self.cells[3][3] = WHITE
        self.cells[3][4] = BLACK
        self.cells[4][3] = BLACK
        self.cells[4][4] = WHITE

    def put_disk(self, x, y, player):
        if self.cells[y][x] is not None:
            # 他の石がすでにあれば置くことができない
            return False

        flippabele = self.list_flippable_disks(x, y, player)
        if flippabele == []:
            return False
        self.cells[y][x] = player
        for x, y in flippabele:
            self.cells[y][x] = player

        return True

    def list_flippable_disks(self, x, y, player):
        PREV = -1
        NEXT = 1
        DIRECTION = [PREV, 0, NEXT]
        flippable = []

        for dx in DIRECTION:
            for dy in DIRECTION:
                if dx == 0 and dy == 0:
                    continue
                tmp = []
                depth = 0
                while True:
                    depth += 1
                    rx = x + (dx * depth)
                    ry = y + (dy * depth)
                    if 0 <= rx < BOARD_SIZE and 0 <= ry < BOARD_SIZE:
                        request = self.cells[ry][rx]
                        if request is None:
                            break

                        if request == player:
                            if tmp != []:
                                flippable. extend(tmp)
                        else:
                            tmp.append((rx,ry))
                    else:
                        break
        return flippable

    def show_board(self):
        print('--' *20)
        for i in self.cells:
            for cell in i:
                if cell == WHITE:
                    print('白', end="")
                elif cell == BLACK:
                    print("黒", end ="")
                else:
                    print("＊", end="")
            print("\n", end='')

    def list_possible_cells(self,player):
        possible = []
        for x in range(BOARD_SIZE):
            if self.cells[y][x] is not None:
                continue
            else:
                possible.append((x, y))
        return possible

if __name__ == "__main__":
    board = ReversiBoard()
    board.show_board()
    board.put_disk(3, 2, BLACK)
    board.show_board()
    board.put_disk(2, 2, WHITE)
    board.show_board()


                                


                                