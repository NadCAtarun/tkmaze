from line import Line
from point import Point
from window import Window

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
