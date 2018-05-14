#tkinter test
#import tkinter as Tk
from tkinter import *
root = Tk()
root.title("Drag window here")
root.wait_visibility(root)
root.attributes("-alpha", 0.5)
def url_open(event):
    call(["ls", "-l"])

btn = Button(root,
             text="Click me",
             width=100,height=30,
             bg="white",fg="black")
btn.bind("<Button-1>", url_open)
btn.pack()
root.mainloop()
