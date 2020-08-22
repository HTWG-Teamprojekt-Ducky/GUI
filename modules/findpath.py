class Findpath():
    start_set = False;
    end_set = False
    start = [];
    end = [];
    ovals = []

    def __init__(self, canvas):
        self.canvas = canvas

    def set_start(self, event):
        global start_set;
        global start_point;
        global start

        if start_set:
            self.canvas.delete('start')

        self.canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")
        start_set = True
        x = int(round(event.x / 12));
        y = int(round(event.y / 12))
        start.append(x);
        start.append(y)

        start_point.set('{}, {}'.format(x, y))


