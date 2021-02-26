import tkinter


def draw_axes(canvas):
    print("Drawing axes...")
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")
    print("Axes has been drawn!")
    pass


def draw_plot(canvas, x, y, xp, yp):
    print("Drawing plots...")
    canvas.create_line(x, -y, xp, -yp, fill="red")
    print("Plot has been drawn!")
    pass


mainWindow = tkinter.Tk()
mainWindow.title("Plot")
mainWindow.geometry("640x480")

mainCanvas = tkinter.Canvas(mainWindow, width=640, height=480)
mainCanvas.grid(row=0, column=0)
draw_axes(mainCanvas)

for i in range(-100, 101):
    draw_plot(mainCanvas, i * 5, (i * i) / 5, (i - 1) * 5, (i-1) * (i - 1) / 5)
    pass

mainWindow.mainloop()
