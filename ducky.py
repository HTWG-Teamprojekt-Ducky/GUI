import tkinter as tk
from tkinter import filedialog
import yaml
from PIL import ImageTk, Image     

global one 
one = []

root = tk.Tk()
root.title('Ducky GUI')
root.geometry('1920x1080')

def get_image(name):
    name = name.replace('/', '_').lower()
    #print(name)
    try:
        open('./ducky_pictures/' + name + '.png', 'r')
        return './ducky_pictures/' + name + '.png'
    except:
        return './ducky_pictures/' + 'cub.png'
    
canvas = tk.Canvas(width=1024, height=768, bg='black')
canvas.pack(side=tk.TOP)

with open('maps/udem1.yaml', 'r') as map_file:
    imap = yaml.load(map_file, Loader=yaml.FullLoader)
        
for row in range(len(imap['tiles'])):
    print(row)
    for column in range(len(imap['tiles'][0])):
        image_file = get_image(imap['tiles'][row][column])
        image = Image.open(image_file)
        resized_image = image.resize((120, 120), Image.ANTIALIAS)
        one.append(ImageTk.PhotoImage(resized_image))
        canvas.create_image(column * 120 + 60, row * 120 + 60, image=one[-1])
 
x = 0; y = 0
canvas.create_rectangle(x, y, 15, 15, fill="yellow")

"""
gif1 = ImageTk.PhotoImage(file='./ducky_pictures/grass.png')
canvas.create_image(0, 300, image=gif1)
gif2 = ImageTk.PhotoImage(file='./ducky_pictures/asphalt.png')
canvas.create_image(256, 0, image=gif2)
"""

def callback():
    root.filename =  filedialog.askopenfilename(initialdir = "maps/",title = "Select map",filetypes = (("yaml files","*.yaml"),("all files","*.*")))
    map_file = root.filename.split('/')[-1]
    
    render_map(map_file)

def render_map(name, canvas):
    with open('maps/' + name, 'r') as map_file:
        imap = yaml.load(map_file, Loader=yaml.FullLoader)
    
    for row in range(len(imap['tiles'])):
        for column in range(len(imap['tiles'][0])):
            image_file = get_image(imap['tiles'][row][column])
            image = Image.open(image_file)
            resized_image = image.resize((120, 120), Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(resized_image)
            gif2 = ImageTk.PhotoImage(file='./ducky_pictures/asphalt.png')
            canvas.create_image(row, column, image=gif2)
            #tile = tk.Label(root, image=tk_image)
            #tile.image = tk_image
            #tile.grid(row=row, column=column)
                               
#render_map('udem1.yaml', canvas)
tk.Button(text='Load map (.yaml)', command=callback).pack()

root.mainloop()