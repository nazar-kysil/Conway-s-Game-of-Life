import numpy as np

class GameOfLife:
    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        if matrix is not None:
            self.matrix = matrix
        else:
            self.matrix = np.zeros((rows, cols))

    def neighbors(self, x, y):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                count_x = (x + i) % self.rows
                count_y = (y + j) % self.cols
                count += self.matrix[count_x, count_y]
        return count

    def update(self):
        new_matrix = np.zeros((self.rows, self.cols))
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.neighbors(i, j)
                if self.matrix[i, j] == 1 and neighbors in [2, 3]:
                    new_matrix[i, j] = 1
                elif self.matrix[i, j] == 0 and neighbors == 3:
                    new_matrix[i, j] = 1
                else:
                    new_matrix[i, j] = 0
        self.matrix = new_matrix

class FileGameOfLife(GameOfLife):
    def __init__(self, file):
        lines = []
        with open(f"sample_patterns/{file}.txt", 'r') as f:
            for line in f:
                row = []
                for char in line.strip():
                    if char == 'X':
                        row.append(1)
                    else:
                        row.append(0)
                lines.append(row)
        matrix = np.array(lines)
        rows, cols = matrix.shape
        super().__init__(rows, cols, matrix)