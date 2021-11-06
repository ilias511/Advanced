import random
from PIL import Image
import os
import tkinter as tk
win = tk.Tk()


def play():
    folder = r'C:\Users\HLIAS\PycharmProjects\Advanced\self-projects\gui\numbers'

    a = random.choice(os.listdir(folder))

    def show(img):
        img.show()
    file = folder + '\\' + a
    img = Image.open(file)
    show(img)

win.geometry('650x250')
button= tk.Button(text='Press for random number',
                  fg = 'white',
                  bg = 'red',
                  command=play)
button.pack(side=tk.BOTTOM)
win.mainloop()




