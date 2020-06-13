import tkinter as tk
import yaml
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Ducky GUI')
root.geometry('1920x1080')

with open('map.yaml', 'r') as map_file:
    imap = yaml.load(map_file, Loader=yaml.FullLoader)

"""
R1|C1|C2|C3
R2|
R3|

def set_image():
    
    
    return img

for row in range(10):
   for column in range(10):
       canvas = tk.Canvas(root, width=300, height=300)
       canvas.pack()
       img = tk.PhotoImage(file="cub.png")  
       canvas.create_image(20,20, anchor=tk.NW, image=img)
       tk.Label(root, text='R%s/C%s'%(row, column), borderwidth=1, relief='groove').grid(row=row,column=column)

"""

columns = 10
tile_counter = 0

print(imap['tiles'])

def get_image(name):
    name = name.replace('/', '_').lower()
    #print(name)
    try:
        open('./ducky_pictures/' + name + '.png', 'r')
        return './ducky_pictures/' + name + '.png'
    except:
        return './ducky_pictures/' + 'cub.png'
    
for row in range(len(imap['tiles'])):
    for column in range(len(imap['tiles'][0])):
        image_file = get_image(imap['tiles'][row][column])
        tile_counter += 1
        # r, c = divmod(tile_counter-1, columns)
        image = Image.open(image_file)
        resized_image = image.resize((120, 120), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized_image)
        tile = tk.Label(root, image=tk_image)
        tile.image = tk_image
        tile.grid(row=row, column=column)
    
root.mainloop()