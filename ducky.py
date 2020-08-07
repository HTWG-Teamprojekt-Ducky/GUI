import tkinter as tk
from tkinter import filedialog
import yaml
from PIL import ImageTk, Image
from modules import astar

global canvas
global ducky

one = []
root = tk.Tk()
root.title('Ducky GUI')
root.geometry('1920x1080')

# test data for scaling
array_of_local_coordinates = [(1.4, 1.4), (1.4, 1.5), (1.4, 1.6), (1.4, 1.7), (1.4, 1.8), (1.4, 1.9), (2.4, 2.0),
                              (2.4, 2.1), (2.4, 2.2), (2.4, 2.3)]

elements = []
scaled_coordinates_ = {}
gui_final_coordinates_ = {}


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
    global ducky

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

    ducky = canvas.create_rectangle(x, y, x + 5, y + 5, fill="red")  # calculated size of ducky


def load_map():
    root.filename = filedialog.askopenfilename(initialdir="maps/", title="Select map",
                                               filetypes=(("yaml files", "*.yaml"), ("all files", "*.*")))
    map_file = root.filename.split('/')[-1][:-5]

    gen_map(map_file)

    draw_grid_board(canvas)


# stk.Button(text='Load map (.yaml)', command=load_map).grid(row=0, column=1, sticky='W', padx=15, pady=15)

display_x = 0
display_y = 0

text_y = tk.StringVar()
tk.Button(root, textvariable=text_y).grid(row=0, column=1, sticky='W', padx=165, pady=15)
text_y.set('Y-Koordinate: 0')

text_x = tk.StringVar()
tk.Button(root, textvariable=text_x).grid(row=0, column=1, sticky='W', padx=15, pady=15)
text_x.set('X-Koordinate: 0')

def keypress(event):
    global display_x
    global display_y

    x = 0
    y = 0

    if event.char == "a":
        x = -6
        display_x = display_x - 1
        text_x.set('X-Koordinate: ' + str(display_x / 2))
    elif event.char == "d":
        x = 6
        display_x = display_x + 1
        text_x.set('X-Koordinate: ' + str(display_x / 2))
    elif event.char == "w":
        y = -6
        display_y = display_y - 1
        text_y.set('Y-Koordinate: ' + str(display_y / 2))
    elif event.char == "s":
        y = 6
        display_y = display_y + 1
        text_y.set('Y-Koordinate: ' + str(display_y / 2))

    canvas.move(ducky, x, y)

    print(canvas.coords(ducky))




def draw_grid_board(canvas):
    # draw grid on grid
    x1 = 0
    x2 = 1000
    # draw horizontal lines
    for k in range(0, 1000, 6):
        y1 = k
        y2 = k
        canvas.create_line(x1, y1, x2, y2, fill="#888888")
    # draw vertical lines
    y1 = 0
    y2 = 1000
    for k in range(0, 1000, 6):
        x1 = k
        x2 = k
        canvas.create_line(x1, y1, x2, y2, fill="#888888")


def global_to_scaled_coordinates(list_of_coordinates):
    # take global coordinates and add the cordinates with 0.1 for scaling
    for element in list_of_coordinates:

        gui_coordinates = []
        for coordinates in element:
            integer_part, decimal_part = map(int, str(coordinates).split(".", 1))

            # global tiles coordinates remain same while scaling
            # the elements inside the tiles needs to scaled, so we can see properly
            scaled_integer_part = integer_part
            scaled_decimal_part1 = decimal_part + decimal_part
            scaled_decimal_part2 = decimal_part + decimal_part + 1

            # TODO:format to keep trailing zeros
            scaled_coordinate1 = (float(str(scaled_integer_part) + "." + str(scaled_decimal_part1)))
            scaled_coordinate2 = (float(str(scaled_integer_part) + "." + str(scaled_decimal_part2)))

            gui_coordinates.append((scaled_coordinate1, scaled_coordinate2))

        scaled_coordinates_[element] = gui_coordinates

def scaled_to_gui_coordinates(scaled_coordinates):
    for element in scaled_coordinates:

        gui_coordinates = []

        for scaled_coordinates in element:

            integer_part, decimal_part = map(int, str(scaled_coordinates).split(".", 1))

            if integer_part == 0:
                scaled_integer_part = integer_part
            else:
                scaled_integer_part = integer_part + 120

            scaled_decimal_part = decimal_part * 6
            final_scaled_x_and_y = scaled_integer_part + scaled_decimal_part
            gui_coordinates.append((final_scaled_x_and_y))

        gui_final_coordinates_[element] = gui_coordinates

    print(gui_final_coordinates_)


def convert_to_ducky_four_coordinates(x, y):
    x1 = 0
    y1 = 0
    return x, y, x1, y1


def place_coordinates(canvas):
    # take canvas as root
    coords = [(0, 0), (0, 5), (0, 10), (0, 15), (0, 20), (0, 25), (0, 30), (0, 35), (0, 40), (0, 45), (0, 45)]
    for c in coords:
        label = canvas.create_rectangle(120, 120, 150, 170, fill="yellow")


root.bind("<Key>", keypress)

gen_map('udem1')

START = [35, 15]
END   = [40, 55]

line = astar.main(START, END)
def draw_dots(canvas):
    # 0, 0

    for l in line:
        x = (4 + 4 + 4) * l[1] # 4 = 0,
        y = (4 + 4 + 4) * l[0]

        x1, y1 = (x - 3), (y - 3)
        x2, y2 = (x + 3), (y + 3)
        canvas.create_oval(x1, y1, x2, y2, fill="#00ffff")

draw_dots(canvas)

place_coordinates(canvas)
draw_grid_board(canvas)
global_to_scaled_coordinates(array_of_local_coordinates)
scaled_to_gui_coordinates(scaled_coordinates_)

root.mainloop()
