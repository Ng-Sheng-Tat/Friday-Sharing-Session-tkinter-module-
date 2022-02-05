import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()
root.geometry('500x500')
# create icon
root.iconbitmap('calcicon.ico')

# creating input fields widget
e = tk.Entry(root, width=45, bg="pink", fg="black", borderwidth=3)
e.pack()
e.insert(0, "Enter your name: ")

""" (Text Widget)
# creating label widgets
mylabel1 = tk.Label(root, text="Text To Display1")
mylabel2 = tk.Label(root, text="                ")
mylabel3 = tk.Label(root, text="Text To Display3")

# showing it on the screen
# mylabel.pack()

# showing on screen on grid system
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)
mylabel3.grid(row=2, column=5)
"""

""" (Button Widget)

"""
def onceclick():
    myoutput = "You enter " + e.get()
    mylabel = tk.Label(root, text=myoutput)
    mylabel.pack()

"""
Define images
myimg = ImageTk.PhotoImage(Image.open("spiderimg.png"))
imglabel = tk.Label(image=myimg)
imglabel.place(x=0, y=0)

mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=onceclick, fg="black", bg="yellow") # state=tk.DISABLED
mybutton.pack()

quitbutton =  tk.Button(root, text="Exit", padx=20, pady=13, command=root.quit)
quitbutton.pack()
"""

"""
# Radio Button
myvariable = tk.IntVar() # StrVar()
# Set the default option
myvariable.set("2")

def checked(val):
    mylabel = tk.Label(root, text=val)
    mylabel.pack()

tk.Radiobutton(root, text="Choice 1", variable=myvariable, value=1, command=lambda: checked(myvariable.get())).pack()
tk.Radiobutton(root, text="Choice 2", variable=myvariable, value=2, command=lambda: checked(myvariable.get())).pack()
myLabel = tk.Label(root, text=myvariable.get())
myLabel.pack()
"""
"""
# messages box
def message():
    messagebox.showinfo("Message Title", "My message")

tk.Button(root, text="MsgBox", command=message).pack()
"""

"""
# checkbox
def showvar():
    mylabel = tk.Label(root, text=var.get()).pack()

var = tk.IntVar()
c = tk.Checkbutton(root, text="Text to display", variable=var)
c.pack()
bu = tk.Button(root, text="Show Text", command=showvar).pack()
"""

# Dropdown menu
def showval():
    mylabel = tk.Label(root, text=clicked.get()).pack()

clicked = tk.StringVar()
clicked.set("Friday")

dropd = tk.OptionMenu(root, clicked, "Friday", "Saturday", "Sunday")
dropd.pack()

bu = tk.Button(root, text="Show Me", command=showval).pack()

# everthing of applications are looping constantly
root.mainloop()
