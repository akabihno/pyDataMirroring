import subprocess
from tkinter import *

list_name = ["nautilus", "chrome", "firefox", "bash", "gnome-system-monitor", "pulseaudio", "cat", "sublime_text"]

root = Tk()
root.title("Drag window here")
root.geometry("800x650+0+0")
root.wait_visibility(root)
root.attributes("-alpha", 0.5)
def url_open(event):
    for i in list_name:
        ps_name = i
        command = "ps -A|grep {}".format(ps_name)
        process_list = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output = process_list.communicate()[0]
        output = str(output)
        print(output)
        #print(type(output))
        if "chrome" in output:
        	print("done")

btn = Button(root,
             text="Active programms",
             width=15,height=3,
             bg="white",fg="black")
btn.bind("<Button-1>", url_open)
btn.pack()
root.mainloop()
