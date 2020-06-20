import tkinter as tk
from tkinter import filedialog
import yaml
from PIL import ImageTk, Image

global canvas
global c1

one = []
root = tk.Tk()
root.title('Ducky GUI')
root.geometry('1920x1080')


def calc_mapsize(imap):
    height = len(imap['tiles']) * 120
    width = len(imap['tiles'][0]) * 120

    return [width, height]


def get_image(name):
    name = name.replace('/', '_').lower()
    try:
        open('./ducky_pictures/' + name + '.png', 'r')
        return './ducky_pictures/' + name + '.png'
    except:
        return './ducky_pictures/' + 'cub.png'


def gen_map(name):
    global canvas
    global c1

    with open('maps/{}.yaml'.format(name), 'r') as map_file:
        imap = yaml.load(map_file, Loader=yaml.FullLoader)

    dimension = calc_mapsize(imap)

    try:
        canvas.destroy()
    except:
        pass

    canvas = tk.Canvas(width=dimension[0], height=dimension[1], bg='black')
    canvas.grid(row=1, column=1)

    for row in range(len(imap['tiles'])):
        for column in range(len(imap['tiles'][0])):
            image_file = get_image(imap['tiles'][row][column])
            image = Image.open(image_file)
            resized_image = image.resize((120, 120), Image.ANTIALIAS)
            one.append(ImageTk.PhotoImage(resized_image))
            canvas.create_image(column * 120 + 60, row * 120 + 60, image=one[-1])

    x = 0
    y = 0

    c1 = canvas.create_rectangle(x, y, x + 15, y + 15, fill="yellow")


def load_map():
    root.filename = filedialog.askopenfilename(initialdir="maps/", title="Select map",
                                               filetypes=(("yaml files", "*.yaml"), ("all files", "*.*")))
    map_file = root.filename.split('/')[-1][:-5]

    gen_map(map_file)

    draw_grid_board(canvas)


tk.Button(text='Load map (.yaml)', command=load_map).grid(row=0, column=1, sticky='W', padx=15, pady=15)


def keypress(event):
    x = 0
    y = 0

    if event.char == "a":
        x = -15
    elif event.char == "d":
        x = 15
    elif event.char == "w":
        y = -15
    elif event.char == "s":
        y = 15
    canvas.move(c1, x, y)


def draw_grid_board(canvas):
    # draw grid on grid
    x1 = 0
    x2 = 1000
    for k in range(0, 1000, 15):
        y1 = k
        y2 = k
        canvas.create_line(x1, y1, x2, y2)
    # draw vertical lines
    y1 = 0
    y2 = 1000
    for k in range(0, 1000, 15):
        x1 = k
        x2 = k
        canvas.create_line(x1, y1, x2, y2)


root.bind("<Key>", keypress)
gen_map('udem1')
draw_grid_board(canvas)

root.mainloop()
