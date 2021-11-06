import tkinter as tk

screen = tk.Tk()

greeting = tk.Label(
    text = 'Hello people',
    fg = 'black',
    bg = 'purple',
    width=100,
    height=50
)
greeting.pack()


label = tk.Entry()
label.pack()
name = label.get()

label.insert(0,'Real')
button = tk.Button(
    text = 'DONT CLICK',
    width = 80,
    height=20,
    bg = 'red',
    fg = 'yellow'

)
button.pack()

screen.mainloop()