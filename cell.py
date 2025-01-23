from line import Line
from point import Point


class Cell:
    def __init__(self, nwpoint, sepoint):
        self.nwpoint = nwpoint
        self.nepoint = Point(sepoint.x, nwpoint.y)
        self.sepoint = sepoint
        self.swpoint = Point(nwpoint.x, sepoint.y)
        self.center = Point((nwpoint.x + sepoint.x) / 2, (nwpoint.y + sepoint.y) / 2)
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.lines = {
            'N': Line(nwpoint, self.nepoint),
            'E': Line(self.nepoint, sepoint),
            'S': Line(sepoint, self.swpoint),
            'W': Line(self.swpoint, nwpoint)
        }

    def draw(self, canvas):
        if self.walls['N']:
            self.lines['N'].draw(canvas)
        if self.walls['E']:
            self.lines['E'].draw(canvas)
        if self.walls['S']:
            self.lines['S'].draw(canvas)
        if self.walls['W']:
            self.lines['W'].draw(canvas)

    def draw_move(self, canvas, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        line = Line(self.center, to_cell.center)
        line.draw(canvas, fill_color=color)
