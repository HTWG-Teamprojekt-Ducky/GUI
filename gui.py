# The following class defines GUI.
# TODO: ADD Description and complete document comments
import threading
import tkinter as tk
import numpy as np
from gym_duckietown.envs.duckietown_env import DuckietownEnv
from modules import astar, navigation, grid, mapping, findpath
import time
from Observer import Subscriber
from threading import Thread


# from exercises import basic_control
# from lokalisierung.duckietown_env import DuckietownEnv

class GUI(threading.Thread, Subscriber):

    def __init__(self):
        threading.Thread.__init__(self)
        self.root = tk.Tk()
        self.root.title('Ducky GUI')
        self.root.geometry('1920x1080')
        self.gboll = True
        self.initialise_map = mapping.Mapping(tk)
        self.canvas_and_ducky = self.initialise_map.gen_map('udem1')
        self.canvas = self.canvas_and_ducky[0]
        self.ducky = self.canvas_and_ducky[1]
        self.generated_grid = grid.Grid(self.canvas)

        self.number_of_clicks = 0
        self.text_y_display = tk.StringVar()
        self.text_x_display = tk.StringVar()
        self.text_x_actual = tk.StringVar()
        self.text_y_actual = tk.StringVar()
        self.distance_traveled_display = tk.StringVar()
        self.start_point = tk.StringVar()
        self.end_point = tk.StringVar()
        self.display_speed = tk.StringVar()

        #self.myduckietown = DuckietownEnv(GUI=self, domain_rand=False, draw_bbox=False, map_name="udem1")
        self.START = [0, 0]
        self.END = [0, 0]
        self.start = []
        self.end = []
        self.ovals = []

        self.speed = 2
        self.sleep_time = 0.2
        self.counter = 0

        self.start_set = False
        self.end_set = False

        self.line = astar.main(self.START, self.END)
        self.path = findpath.Findpath(self.canvas)

        self.coordinate_elements = {'display_x': 0, 'display_y': 0,
                                    'actual_x': 0, 'actual_y': 0,
                                    'distance_traveled': 0, 'number_clicks': 0}

    def update(self, message):
        print("Wird update auch während der simulation aufgerufen?")
        self.draw_particles(message[0])
        self.draw_ducky_bot(message[1], message[2])

    def draw_particles(self, parti):
        for x in range(0, len(parti)):
            self.canvas.delete('parti' + str(x))

        for x in range(0, len(parti)):
            print("Particle", x, "is=", parti[x].p_x, parti[x].p_y)
            self.canvas.create_oval(parti[x].p_x * 120, parti[x].p_y * 120, parti[x].p_x * 120 + 6,
                                    parti[x].p_y * 120 + 6, fill="#0000ff",
                                    tags='parti' + str(x))

    def set_gui_label_buttons(self):

        """

        :return:

        """

        tk.Button(self.root, textvariable=self.text_y_display, width=12).grid(row=0, column=1, sticky='W', padx=15,
                                                                              pady=15)
        self.text_y_display.set('Display-X: 0')

        tk.Button(self.root, textvariable=self.text_x_display, width=12).grid(row=0, column=1, sticky='W', padx=165,
                                                                              pady=15)
        self.text_x_display.set('Display-Y: 0')

        tk.Button(self.root, textvariable=self.text_x_actual, width=12).grid(row=0, column=1, sticky='W', padx=315,
                                                                             pady=15)
        self.text_x_actual.set('Actual-X: 0')

        tk.Button(self.root, textvariable=self.text_y_actual, width=12).grid(row=0, column=1, sticky='W', padx=465,
                                                                             pady=15)
        self.text_y_actual.set('Actual-Y: 0')

        tk.Button(self.root, textvariable=self.distance_traveled_display, width=14).grid(row=0, column=1, sticky='W',
                                                                                         padx=615,
                                                                                         pady=15)
        self.distance_traveled_display.set('Distance: 0cm')

        tk.Button(self.root, textvariable=self.display_speed, width=12).grid(row=1, column=1,
                                                                             sticky='NW',
                                                                             padx=615,
                                                                             pady=0)
        self.display_speed.set('Speed:' + '0' + 'cm/s')

    def keypress(self, event):

        """

        :param event:
        :return:

        """

        x = 0
        y = 0

        if event.char == "a":
            x = -6
            display_x = self.coordinate_elements['display_x'] = self.coordinate_elements['display_x'] - 1

            self.text_x_display.set('Display-X: ' + str(display_x * 6))
            self.text_x_actual.set('Actual-X: ' + str(display_x / 2))

            print(display_x)

        elif event.char == "d":
            x = 6
            display_x = self.coordinate_elements['display_x'] = self.coordinate_elements['display_x'] + 1
            self.text_x_display.set('Display-X: ' + str(display_x * 6))
            self.text_x_actual.set('Actual-X: ' + str(display_x / 2))

        elif event.char == "w":
            y = -6
            display_y = self.coordinate_elements['display_y'] = self.coordinate_elements['display_y'] - 1
            self.text_y_display.set('Display-Y: ' + str(display_y * 6))
            self.text_y_actual.set('Actual-Y: ' + str(display_y / 2))

        elif event.char == "s":
            y = 6
            display_y = self.coordinate_elements['display_y'] = self.coordinate_elements['display_y'] + 1
            self.text_y_display.set('Display-Y: ' + str(display_y * 6))
            self.text_y_actual.set('Actual-Y: ' + str(display_y / 2))

        distance_traveled = self.coordinate_elements['distance_traveled'] = self.coordinate_elements[
                                                                                'distance_traveled'] + 2.8
        self.distance_traveled_display.set('Distance: ' + "{:.1f}".format(distance_traveled) + 'cm')

        self.canvas.move(self.ducky, x, y)

    def set_start(self, event):

        """

        :param event:
        :return:

        """

        if self.start_set:
            self.canvas.delete('start')

        self.canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")
        self.start_set = True
        x = int(round(event.x / 12))
        y = int(round(event.y / 12))
        self.start.append(x)
        self.start.append(y)

        self.start_point.set('{}, {}'.format(x, y))

    def set_end(self, event):

        """

        :param event:
        :return:

        """

        if self.end_set:
            self.canvas.delete('end')

        self.canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="blue", tags="end")
        self.end_set = True
        x = int(round(event.x / 12))
        y = int(round(event.y / 12))
        self.end.append(x)
        self.end.append(y)

        self.end_point.set('{}, {}'.format(x, y))

    def draw_ducky_bot(self, ducky_pos, ducky_angle):

        """

        :param ducky_pos:
        :param old_ducky_pos:
        :return:

        """
        ducky = []
        ducky.append(ducky_pos[0] * 120)
        ducky.append(ducky_pos[2] * 120)

        print("ducky_pos in draw duckiebot", ducky_pos)

        #angle = np.arctan2(ducky_pos[0], ducky_pos[1])
        points = self.calc_points(ducky, ducky_angle - np.pi/2)
        self.canvas.delete("ducky")
        self.ducky = self.canvas.create_polygon(points, fill="red", tags='ducky')

    def move_ducky(self, line):

        """

        :param line:
        :return:

        """

        old_x = 0
        old_y = 0

        for coordinates in line:
            # delete the ducky from _init_ and also after changing position
            self.canvas.delete("ducky")

            y, x = coordinates
            scaled_x = x * 12
            scaled_y = y * 12
            self.draw_ducky_bot([scaled_x, scaled_y], (old_x, old_y))

            ducky_speed = (5.6 / self.sleep_time)

            parti = []
            for i in range(-25, 25):
                parti.append((scaled_x + i, scaled_y + i))

            # self.draw_particles(parti)

            # print the coordinates of middle point of the ducky
            # print("scaled_x = ", scaled_x, " scaled_y = ", scaled_y)
            self.text_x_display.set('Display-X: ' + str(scaled_x))
            self.text_x_actual.set('Actual-X: ' + str(scaled_x / 12))
            self.text_y_display.set('Display-Y: ' + str(scaled_y))
            self.text_y_actual.set('Actual-Y: ' + str(scaled_y / 12))
            self.display_speed.set('Speed:' + "{:.1f}".format(ducky_speed) + 'cm/s')
            distance_traveled = self.coordinate_elements['distance_traveled'] = self.coordinate_elements[
                                                                                    'distance_traveled'] + 5.6
            self.distance_traveled_display.set('Distance: ' + "{:.1f}".format(distance_traveled) + 'cm')

            old_x = scaled_x
            old_y = scaled_y

            time.sleep(self.sleep_time)

    def find_path(self):

        """

        :return:

        """
        print("so vile threads laufen", threading.active_count())
        if len(self.ovals) > 0:
            for o in self.ovals:
                self.canvas.delete(o)

        # print('INIT', self.start, self.end)
        line = []
        line = astar.main(self.start, self.end)

        if len(line) > 0:
            for i, l in enumerate(line):
                x = (4 + 4 + 4) * l[1]  # 4 = 0,
                y = (4 + 4 + 4) * l[0]

                x1, y1 = (x - 3), (y - 3)
                x2, y2 = (x + 3), (y + 3)
                self.canvas.create_oval(x1, y1, x2, y2, fill="#00ffff", tags='oval' + str(i))
                self.ovals.append('oval' + str(i))

        #t = Thread(target=self.move_ducky, args=(line,))
        #t.start()

        # subprocess.call(['python3', 'sim.py'])
        # self.move_ducky(line)
        # t = Process(target=self.startGUI, args=(line,))
        # t.start()
        #self.root.lift()
        #self.myduckietown.reset()
        #self.myduckietown.render()
        #self.myduckietown.startControl(line)
        #self.root.lift()
        t = DuckietownEnv(line=line, GUI=self, domain_rand=False, draw_bbox=False, map_name="udem1")
        t.start()
        # self.root.mainloop()
        # t = Process(target=self.move_ducky, args=(line,))
        # t.join()
        # x = Thread(target=self.myduckietown.start, args=(line,))
        # x.start()

        print("wie viele threads laufen?", threading.active_count())

        # x = Thread(target=self.myduckietown.start, args=(line,))
        # x.start()
        self.start = []
        self.end = []
        # self.myduckietown.start(line)

    def startGUI(self, line):
        self.myduckietown.reset()
        self.myduckietown.render()
        self.myduckietown.start(line)

    def draw_buttons(self):

        """

        :return:

        """

        tk.Button(self.root, textvariable=self.start_point, bg='green', fg='white', width=12).grid(row=1, column=1,
                                                                                                   sticky='NW',
                                                                                                   padx=15,
                                                                                                   pady=0)
        self.start_point.set('Start')
        tk.Button(self.root, textvariable=self.end_point, bg='blue', fg='white', width=12).grid(row=1, column=1,
                                                                                                sticky='NW',
                                                                                                padx=165,
                                                                                                pady=0)
        self.end_point.set('End')

        tk.Button(self.root, text='A*', width=12, command=self.find_path, bg='#00ffff').grid(row=1, column=1,
                                                                                             sticky='NW',
                                                                                             padx=315,
                                                                                             pady=0)
        tk.Checkbutton(self.root, text='Enable/Disable grid', command=self.generated_grid.check_grid).grid(row=1,
                                                                                                           column=1,
                                                                                                           sticky='NW',
                                                                                                           padx=465,
                                                                                                           pady=0)

    @staticmethod
    def calc_points(pos, angle):

        """
        :param pos: mm
        :param angle:
        :return:

        """
        print("calc angle=", angle)
        offx = 21 / 2
        offy = 36 / 2

        pointx1 = pos[0] + (np.cos(angle) * -offx - np.sin(angle) * offy)
        pointy1 = pos[1] + (np.sin(angle) * -offx + np.cos(angle) * offy)

        pointx2 = pos[0] + (np.cos(angle) * -offx - np.sin(angle) * -offy)
        pointy2 = pos[1] + (np.sin(angle) * -offx + np.cos(angle) * -offy)

        pointx3 = pos[0] + (np.cos(angle) * offx - np.sin(angle) * -offy)
        pointy3 = pos[1] + (np.sin(angle) * offx + np.cos(angle) * -offy)

        pointx4 = pos[0] + (np.cos(angle) * offx - np.sin(angle) * offy)
        pointy4 = pos[1] + (np.sin(angle) * offx + np.cos(angle) * offy)

        return [[pointx3, pointy3], [pointx4, pointy4], [pointx1, pointy1], [pointx3, pointy3]]

    def main(self):
        self.set_gui_label_buttons()
        self.draw_buttons()

        self.root.bind("<Key>", self.keypress)
        self.root.bind("<Button-2>", self.set_start)
        self.root.bind("<Button-3>", self.set_end)

        navigation.Navigation(self.canvas)
        self.root.mainloop()

if __name__ == "__main__":
    t = Thread(target=GUI().main(), args=())
    t.start()
    # GUI().main()
    print("hallo ich kann sachen machen")
