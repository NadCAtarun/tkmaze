import time

from cell import Cell
from point import Point


class Maze:
    def __init__(self, nw_point, num_rows, num_cols, window, cell_size=50):
        self.nw_point = nw_point
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.window = window
        self.cells = []
        self.create_cells()
        self.animate()

    def cell_nw_point(self, row, col):
        return Point(self.nw_point.x + self.cell_size * col, self.nw_point.y + self.cell_size * row)

    def cell_se_point(self, row, col):
        return Point(self.nw_point.x + self.cell_size * (col + 1), self.nw_point.y + self.cell_size * (row + 1))

    def create_cells(self):
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                cell = Cell(self.cell_nw_point(r, c), self.cell_se_point(r, c))
                row.append(cell)
            self.cells.append(row)

    def animate(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.window.canvas)
                self.window.redraw()
                time.sleep(0.05)
