from maze import Maze
from point import Point
from window import Window

if __name__ == "__main__":
    window = Window(800, 600)

    maze = Maze(Point(150, 50), 10, 10, window)

    window.wait_for_close()
