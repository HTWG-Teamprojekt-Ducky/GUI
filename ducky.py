import tkinter as tk
from tkinter import filedialog
import yaml
from PIL import ImageTk, Image
from modules import astar, navigation

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
    canvas.grid(row=1, column=0, padx=15, pady=15)

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
actual_x = 0

display_y = 0
actual_y = 0

distance_traveled = 0
number_of_clicks = 0

text_y_display = tk.StringVar()
tk.Button(root, textvariable=text_y_display, width=12).grid(row=0, column=1, sticky='W', padx=15, pady=15)
text_y_display.set('Display-X: 0')

text_x_display = tk.StringVar()
tk.Button(root, textvariable=text_x_display, width=12).grid(row=0, column=1, sticky='W', padx=165, pady=15)
text_x_display.set('Display-Y: 0')

text_x_actual = tk.StringVar()
tk.Button(root, textvariable=text_x_actual, width=12).grid(row=0, column=1, sticky='W', padx=315, pady=15)
text_x_actual.set('Actual-X: 0')

text_y_actual = tk.StringVar()
tk.Button(root, textvariable=text_y_actual, width=12).grid(row=0, column=1, sticky='W', padx=465, pady=15)
text_y_actual.set('Actual-Y: 0')

distance_traveled_display = tk.StringVar()
tk.Button(root, textvariable=distance_traveled_display, width=12).grid(row=0, column=1, sticky='W', padx=615, pady=15)
distance_traveled_display.set('Distance: 0cm')


def keypress(event):
    global display_x
    global actual_x
    global display_y
    global actual_y
    global distance_traveled

    x = 0
    y = 0

    if event.char == "a":
        x = -6
        display_x = display_x - 1
        text_x_display.set('Display-X: ' + str(display_x * 6))
        text_x_actual.set('Actual-X: ' + str(display_x / 2))

    elif event.char == "d":
        x = 6
        display_x = display_x + 1
        text_x_display.set('Display-X: ' + str(display_x * 6))
        text_x_actual.set('Actual-X: ' + str(display_x / 2))

    elif event.char == "w":
        y = -6
        display_y = display_y - 1
        text_y_display.set('Display-Y: ' + str(display_y * 6))
        text_y_actual.set('Actual-Y: ' + str(display_y / 2))

    elif event.char == "s":
        y = 6
        display_y = display_y + 1
        text_y_display.set('Display-Y: ' + str(display_y * 6))
        text_y_actual.set('Actual-Y: ' + str(display_y / 2))

    distance_traveled = int(distance_traveled + 2.8)
    distance_traveled_display.set('Distance: ' + str(distance_traveled) + 'cm')

    canvas.move(ducky, x, y)

    print(canvas.coords(ducky))


def callback(event):
    """
    This callback to generate two points on grid, green as starting point and blue as
    endpoint for ducky.
    """
    # TODO: Give all the points between start and endpoint and map accordingly for A* with 0 and 1s
    global number_of_clicks

    number_of_clicks += 1

    if number_of_clicks == 1:
        canvas.delete("end")
        canvas.delete("start")

        canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")
        print("clicked at", event.x, event.y)
        # text_x_display.set('X-Koordinate_Display: ' + "str(display_x * 6) + event.x")
        # text_x_actual.set('X-Koordinate_Actual: ' + "str(display_x / 20) + event.x")

    elif number_of_clicks == 2:

        canvas.delete("end")
        canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="blue", tags="end")
        print("clicked at", event.x, event.y)
        number_of_clicks = 0

    print(number_of_clicks)



    print(number_of_clicks)
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
    """
    This scaling to scale the coordinates from yaml file and obtain a
    tile size of 2.8 cm. We take the global coordinates and add the
    coordinates with itself and 1 for scaling.
    """

    for element in list_of_coordinates:

        gui_coordinates = []

        for coordinates in element:
            integer_part, decimal_part = map(int, str(coordinates).split(".", 1))

            # global tiles coordinates remain same while scaling
            # the elements inside the tiles needs to scaled
            # so we always scale the decimal part
            scaled_integer_part = integer_part

            # scaling is done in two steps here
            # we double the coordinate
            scaled_decimal_part1 = decimal_part + decimal_part
            # add one to the the scaled decimal
            scaled_decimal_part2 = decimal_part + decimal_part + 1

            # TODO:format to keep trailing zeros
            scaled_coordinate1 = (float(str(scaled_integer_part) + "." + str(scaled_decimal_part1)))
            scaled_coordinate2 = (float(str(scaled_integer_part) + "." + str(scaled_decimal_part2)))

            gui_coordinates.append((scaled_coordinate1, scaled_coordinate2))

        scaled_coordinates_[element] = gui_coordinates

    print("scaled coordinates - ", scaled_coordinates_)


def scaled_to_gui_coordinates():
    list_values = scaled_coordinates_.values()
    counter = 0
    for scaled_element in list_values:

        gui_coordinates = []

        for scaled_coordinate1, scaled_coordinate2 in scaled_element:

            integer_part1, decimal_part1 = map(int, str(scaled_coordinate1).split(".", 1))
            integer_part2, decimal_part2 = map(int, str(scaled_coordinate2).split(".", 1))

            if integer_part1 == 0:
                scaled_integer_part1 = integer_part1
            else:
                scaled_integer_part1 = integer_part1 * 120

            scaled_decimal_part1 = decimal_part1 * 6

            if integer_part2 == 0:
                scaled_integer_part2 = integer_part2
            else:
                scaled_integer_part2 = integer_part2 * 120

            scaled_decimal_part2 = decimal_part2 * 6

            final_scaled_x_and_y1 = scaled_integer_part1 + scaled_decimal_part1
            final_scaled_x_and_y2 = scaled_integer_part2 + scaled_decimal_part2

            gui_coordinates.append(final_scaled_x_and_y1)
            gui_coordinates.append(final_scaled_x_and_y2)

        gui_final_coordinates_[counter] = gui_coordinates
        counter = counter + 1

    print("gui final coordinates - ", gui_final_coordinates_)


def convert_to_ducky_four_coordinates(a, b):
    # TODO: Set bounds so that ducky generated stays on road

    x, y, x1, y1 = 0, 0, 0, 0

    if a != 0 & b != 0:
        x1, y1 = 2 * a, 2 * b
        x, y = x1 - 42, y1 - 72

    return x, y, x1, y1


def place_coordinates(canvas):
    # take canvas as root
    label = canvas.create_rectangle(120, 120, 120 + 42, 120 + 72, fill="yellow")



gen_map('udem1')

START = [35, 15]
END = [40, 55]

line = astar.main(START, END)
root.bind("<Key>", keypress)

"""
    Setting waypoints through mouse-clicks
    Functions: set_start, set_end
"""

start_set = False; end_set = False
start = []; end = []; ovals = []

start_point = tk.StringVar()
tk.Button(root, textvariable=start_point, bg='green', fg='white', width=12).grid(row=1, column=1, sticky='NW', padx=15, pady=0)
start_point.set('Start')

end_point = tk.StringVar()
tk.Button(root, textvariable=end_point, bg='blue', fg='white', width=12).grid(row=1, column=1, sticky='NW', padx=165, pady=0)
end_point.set('End')

def set_start(event):
    global start_set; global start_point; global start

    if start_set:
        canvas.delete('start')

    canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")
    start_set = True
    x = int(round(event.x/12)); y = int(round(event.y/12))
    start.append(x); start.append(y)

    start_point.set('{}, {}'.format(x, y))

def set_end(event):
    global end_set; global end_point; global end

    if end_set:
        canvas.delete('end')

    canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="blue", tags="end")
    end_set = True
    x = int(round(event.x/12)); y = int(round(event.y/12))
    end.append(x); end.append(y)

    end_point.set('{}, {}'.format(x, y))


def find_path():

    if len(ovals) > 0:
        for o in ovals:
            canvas.delete(o)

    global start; global end;
    print('INIT', start, end)
    line = astar.main(start, end)

    for i,l in enumerate(line):
        x = (4 + 4 + 4) * l[1]  # 4 = 0,
        y = (4 + 4 + 4) * l[0]

        x1, y1 = (x - 3), (y - 3)
        x2, y2 = (x + 3), (y + 3)

        oval = canvas.create_oval(x1, y1, x2, y2, fill="#00ffff", tags='oval' + str(i))
        ovals.append('oval' + str(i))

    start = []; end = []

root.bind("<Button-2>", set_start)
root.bind("<Button-3>", set_end)

def enable_grid():
        global canvas
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

tk.Button(root, text='A*', width=12, command=find_path, bg='pink').grid(row=1, column=1, sticky='NW', padx=315, pady=0)
tk.Checkbutton(root, text='Enable grid', command=enable_grid).grid(row=1, column=1, sticky='NW', padx=465, pady=0)
"""
    Calculating realistic coordinates based on yaml-Coordinates
    Functions: exchange_coords
"""



print(line)


def draw_dots(canvas):
    # 0, 0

    for l in line:
        x = (4 + 4 + 4) * l[1]  # 4 = 0,
        y = (4 + 4 + 4) * l[0]

        x1, y1 = (x - 3), (y - 3)
        x2, y2 = (x + 3), (y + 3)
        canvas.create_oval(x1, y1, x2, y2, fill="#00ffff")


navigation = navigation.Navigation(canvas)

place_coordinates(canvas)
#draw_grid_board(canvas)
global_to_scaled_coordinates(array_of_local_coordinates)
scaled_to_gui_coordinates()

root.mainloop()
