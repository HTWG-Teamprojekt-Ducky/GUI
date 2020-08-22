import tkinter as tk
from modules import astar, navigation, grid, mapping, findpath

global canvas, ducky

root = tk.Tk()
root.title('Ducky GUI');
root.geometry('1920x1080')

dmap = mapping.Mapping(tk)
coordinate_elements = {'display_x': 0, 'display_y': 0, 'actual_x': 0, 'actual_y': 0, 'distance_traveled': 0, 'number_clicks': 0}

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
    global coordinate_elements
    x = 0;
    y = 0

    if event.char == "a":
        x = -6
        display_x = coordinate_elements['display_x'] = coordinate_elements['display_x'] - 1

        text_x_display.set('Display-X: ' + str(display_x * 6))
        text_x_actual.set('Actual-X: ' + str(display_x / 2))

        print(display_x)

    elif event.char == "d":
        x = 6
        display_x = coordinate_elements['display_x'] = coordinate_elements['display_x'] + 1
        text_x_display.set('Display-X: ' + str(display_x * 6))
        text_x_actual.set('Actual-X: ' + str(display_x / 2))

    elif event.char == "w":
        y = -6
        display_y = coordinate_elements['display_y'] = coordinate_elements['display_y'] - 1
        text_y_display.set('Display-Y: ' + str(display_y * 6))
        text_y_actual.set('Actual-Y: ' + str(display_y / 2))

    elif event.char == "s":
        y = 6
        display_y = coordinate_elements['display_y'] = coordinate_elements['display_y'] + 1
        text_y_display.set('Display-Y: ' + str(display_y * 6))
        text_y_actual.set('Actual-Y: ' + str(display_y / 2))

    distance_traveled = coordinate_elements['distance_traveled'] = int(coordinate_elements['distance_traveled'] + 2.8)
    distance_traveled_display.set('Distance: ' + str(distance_traveled) + 'cm')

    canvas.move(ducky, x, y)

def callback(event):
    global number_of_clicks

    number_of_clicks += 1

    if number_of_clicks == 1:
        canvas.delete("end")
        canvas.delete("start")

        canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")
        print("clicked at", event.x, event.y)
    elif number_of_clicks == 2:

        canvas.delete("end")
        canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="blue", tags="end")
        print("clicked at", event.x, event.y)
        number_of_clicks = 0

    print(number_of_clicks)

    print(number_of_clicks)

mapx = dmap.gen_map('udem1')
canvas = mapx[0];
ducky = mapx[1]
gridx = grid.Grid(canvas)

START = [35, 15]
END = [40, 55]

line = astar.main(START, END)
root.bind("<Key>", keypress)

start_set = False;
end_set = False
start = [];
end = [];
ovals = []

path = findpath.Findpath(canvas)

start_point = tk.StringVar()
tk.Button(root, textvariable=start_point, bg='green', fg='white', width=12).grid(row=1, column=1, sticky='NW', padx=15, pady=0)
start_point.set('Start')

end_point = tk.StringVar()
tk.Button(root, textvariable=end_point, bg='blue', fg='white', width=12).grid(row=1, column=1, sticky='NW', padx=165, pady=0)
end_point.set('End')

def set_start(event):
    global start_set;
    global start_point;
    global start

    if start_set:
        canvas.delete('start')

    canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")
    start_set = True
    x = int(round(event.x / 12));
    y = int(round(event.y / 12))
    start.append(x);
    start.append(y)

    start_point.set('{}, {}'.format(x, y))

def set_end(event):
    global end_set;
    global end_point;
    global end

    if end_set:
        canvas.delete('end')

    canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="blue", tags="end")
    end_set = True
    x = int(round(event.x / 12));
    y = int(round(event.y / 12))
    end.append(x);
    end.append(y)

    end_point.set('{}, {}'.format(x, y))

def find_path():
    if len(ovals) > 0:
        for o in ovals:
            canvas.delete(o)

    global start;
    global end;

    print('INIT', start, end)
    line = astar.main(start, end)

    for i, l in enumerate(line):
        x = (4 + 4 + 4) * l[1]  # 4 = 0,
        y = (4 + 4 + 4) * l[0]

        x1, y1 = (x - 3), (y - 3)
        x2, y2 = (x + 3), (y + 3)

        canvas.create_oval(x1, y1, x2, y2, fill="#00ffff", tags='oval' + str(i))
        ovals.append('oval' + str(i))

    start = []; end = []

root.bind("<Button-2>", set_start)
root.bind("<Button-3>", set_end)

tk.Button(root, text='A*', width=12, command=find_path, bg='#00ffff').grid(row=1, column=1, sticky='NW', padx=315, pady=0)
tk.Checkbutton(root, text='Enable/Disable grid', command=gridx.check_grid).grid(row=1, column=1, sticky='NW', padx=465, pady=0)

def draw_dots(canvas):
    # 0, 0
    for l in line:
        x = (4 + 4 + 4) * l[1]  # 4 = 0,
        y = (4 + 4 + 4) * l[0]

        x1, y1 = (x - 3), (y - 3)
        x2, y2 = (x + 3), (y + 3)
        canvas.create_oval(x1, y1, x2, y2, fill="#00ffff")

navigation = navigation.Navigation(canvas)
root.mainloop()
