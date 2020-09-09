import yaml
from PIL import ImageTk, Image


class Mapping:
    one = []

    def __init__(self, tk):
        self.tk = tk

    def gen_map(self, name):
        global canvas
        global ducky

        with open('maps/{}.yaml'.format(name), 'r') as map_file:
            imap = yaml.load(map_file, Loader=yaml.FullLoader)

        dimension = self.calc_mapsize(imap)

        try:
            canvas.destroy()
        except:
            pass

        canvas = self.tk.Canvas(width=dimension[0], height=dimension[1], bg='black')
        canvas.grid(row=1, column=0, padx=15, pady=15)

        for row in range(len(imap['tiles'])):
            for column in range(len(imap['tiles'][0])):
                image_file = self.get_image(imap['tiles'][row][column])
                image = Image.open(image_file)
                resized_image = image.resize((120, 120), Image.ANTIALIAS)
                self.one.append(ImageTk.PhotoImage(resized_image))
                canvas.create_image(column * 120 + 60, row * 120 + 60, image=self.one[-1])

        x = 0
        y = 0

        ducky = canvas.create_rectangle(x, y, x + 21, y + 36, fill="red", tags='ducky')
        return [canvas, ducky]

    def get_image(self, name):
        name = name.replace('/', '_').lower()
        try:
            open('./ducky_pictures/' + name + '.png', 'r')
            return './ducky_pictures/' + name + '.png'
        except:
            return './ducky_pictures/' + 'cub.png'

    def calc_mapsize(self, imap):
        height = len(imap['tiles']) * 120
        width = len(imap['tiles'][0]) * 120

        return [width, height]
    #
    # def load_map():
    #     root.filename = filedialog.askopenfilename(initialdir="maps/", title="Select map",
    #                                                filetypes=(("yaml files", "*.yaml"), ("all files", "*.*")))
    #     map_file = root.filename.split('/')[-1][:-5]
    #
    #     gen_map(map_file)
