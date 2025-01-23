from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width=1000, height=1000):
        self.window = Tk()
        self.window.title("Maze")
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.window.update_idletasks()
        self.window.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

if __name__ == "__main__":
    window = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(100, 300)
    p3 = Point(300, 300)
    p4 = Point(300, 100)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)
    window.draw_line(l1)
    window.draw_line(l2)
    window.draw_line(l3)
    window.draw_line(l4)
    window.wait_for_close()
