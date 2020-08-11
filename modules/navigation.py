class Navigation():
    def __init__(self, canvas):
        self.canvas = canvas

    def set_start(self, event):
        global number_of_clicks

        number_of_clicks += 1

        if number_of_clicks == 1:
            self.canvas.delete("end")
            self.canvas.delete("start")
            self.canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="green", tags="start")

            print("clicked at", event.x, event.y)

        elif number_of_clicks == 2:
            self.canvas.delete("end")
            self.canvas.create_rectangle(event.x, event.y, event.x + 6, event.y + 6, fill="blue", tags="end")

            print("clicked at", event.x, event.y)
            number_of_clicks = 0
