class Cell:
    def __init__(self, nwpoint, sepoint):
        self.nwpoint = nwpoint
        self.sepoint = sepoint
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}

    def draw(self, canvas):
        if self.walls['N']:
            canvas.create_line(self.nwpoint.x, self.nwpoint.y, self.sepoint.x, self.nwpoint.y)
        if self.walls['E']:
            canvas.create_line(self.sepoint.x, self.nwpoint.y, self.sepoint.x, self.sepoint.y)
        if self.walls['S']:
            canvas.create_line(self.nwpoint.x, self.sepoint.y, self.sepoint.x, self.sepoint.y)
        if self.walls['W']:
            canvas.create_line(self.nwpoint.x, self.nwpoint.y, self.nwpoint.x, self.sepoint.y)
