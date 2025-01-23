from tkinter import Tk, BOTH, Canvas

class Window():
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

if __name__ == "__main__":
    window = Window(800, 600)
    window.wait_for_close()
