import time

from cell import Cell
from point import Point
from window import Window

if __name__ == "__main__":
    window = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(300, 300)
    p3 = Point(400, 100)
    p4 = Point(600, 300)

    c1 = Cell(p1, p2)
    c1.walls["E"] = False
    c2 = Cell(p3, p4)
    c2.walls["W"] = False

    c1.draw(window.canvas)
    c2.draw(window.canvas)

    c1.draw_move(window.canvas, c2)
    window.redraw()
    time.sleep(3)
    c1.draw_move(window.canvas, c2, undo=True)

    window.wait_for_close()
