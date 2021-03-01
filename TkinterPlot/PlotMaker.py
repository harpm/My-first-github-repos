import tkinter
import math

mainWindow = tkinter.Tk()
mainCanvas = tkinter.Canvas(mainWindow, width=640, height=480)


def __init__():
    make_window()
    make_canvas()
    draw_axes()


def make_window():
    mainWindow.title("Plot")
    mainWindow.geometry("640x480")


def make_canvas():
    mainCanvas.grid(row=0, column=0)


def draw_axes():
    mainCanvas.update()
    x_origin = mainCanvas.winfo_width() / 2
    y_origin = mainCanvas.winfo_height() / 2
    mainCanvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    mainCanvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    mainCanvas.create_line(0, -y_origin, 0, y_origin, fill="black")
    pass


def draw_plot(x, y, dot_size):
    mainCanvas.create_line(x, -y, x - dot_size, - y - dot_size, fill="red")
    pass


def draw_circle(radius, g, h, dot_size=1.0, tolerance=100):
    for x in range(g * tolerance, (g + radius) * tolerance):
        x /= tolerance
        y = h + math.sqrt(radius ** 2 - (g - x) ** 2)
        draw_plot(x, y, dot_size)
        draw_plot(x, 2 * h - y, dot_size)
        draw_plot(2 * g - x, y, dot_size)
        draw_plot(2 * g - x, 2 * h - y, dot_size)
        pass

    # page.create_oval(g + radius, h + radius, g - radius, h - radius, outline="red", width=dot_size)

    pass


def draw_default_plot():
    i = -100
    while i <= 100:
        x = i
        y = ((1/2) * x ** 2 + 4 * x + 8) / 10
        draw_plot(x, y, 0.1)
        i += 0.005
        pass
    mainWindow.mainloop()
    pass


if __name__ == '__main__':
    __init__()
    draw_circle(75, 0, 0, 0.015)
    draw_circle(50, 50, 50, 1)
    draw_circle(50, -50, 50, 1)
    draw_circle(50, 50, -50, 1)
    draw_circle(50, -50, -50, 1)

    mainWindow.mainloop()
