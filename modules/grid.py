class Grid:
    grid_items = []
    grid_enabled = False

    def __init__(self, canvas):
        self.canvas = canvas
        print(self.canvas)

    def enable_grid(self):
        canvas = self.canvas
        # draw grid on grid
        x1 = 0
        x2 = 1000
        # draw horizontal lines
        for k in range(0, 1000, 6):
            y1 = k
            y2 = k
            canvas.create_line(x1, y1, x2, y2, fill="#888888", tags='grid' + str(k))
            self.grid_items.append('grid' + str(k))
        # draw vertical lines
        y1 = 0
        y2 = 1000
        for k in range(0, 1000, 6):
            x1 = k
            x2 = k
            canvas.create_line(x1, y1, x2, y2, fill="#888888", tags='grid' + str(k))
            self.grid_items.append('grid' + str(k))

    def disabled_grid(self):
        canvas = self.canvas

        for g in self.grid_items:
            canvas.delete(g)

    def check_grid(self):
        grid_enabled = self.grid_enabled

        if grid_enabled:
            self.disabled_grid()
            self.grid_enabled = False
        else:
            self.enable_grid()
            self.grid_enabled = True
