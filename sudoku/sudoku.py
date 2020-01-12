class Sudoku:
    def __init__(self, arr=[[0 for i in range(9)] for j in range(9)]):
        self.arr = arr
        self.node = [0, 0]
    def find(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.arr[i][j] == 0:
                    self.node[0] = i
                    self.node[1] = j
                    return True
        return False
    def ccr(self, row, num):
        for i in range(0, 9):
            if self.arr[row][i] == num:
                return False
        return True
    def ccc(self, col, num):
        for i in range(0, 9):
            if self.arr[i][col] == num:
                return False
        return True
    def ccb(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.arr[row + i][col + j] == num:
                    return False
        return True
    def check(self, row, col, num):
        return self.ccr(row, num) and self.ccc(col, num) and self.ccb(row - row%3, col - col%3, num)
    def solve(self):
        self.node = [0, 0]
        if not self.find():
            return True
        row = self.node[0]
        col = self.node[1]
        for num in range(0, 10):
            if self.check(row, col, num):
                self.arr[row][col] = num
                if self.solve():
                    return True
                self.arr[row][col] = 0
        return False
if __name__ == "__main__":
    BOARD = Sudoku([
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ])
    BOARD.solve()
    print(BOARD.arr)
