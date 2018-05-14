#tkinter test
from tkinter import *
root = Tk()
root.title("Drag window here")
def url_open(event):
    call(["ls", "-l"])

btn = Button(root,
             text="Click me",
             width=30,height=5,
             bg="white",fg="black")
btn.bind("<Button-1>", url_open)
btn.pack()
root.mainloop()
