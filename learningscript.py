import tkinter as tk

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()

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

mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=onceclick, fg="black", bg="yellow") # state=tk.DISABLED
mybutton.pack()

# everthing of applications are looping constantly
root.mainloop()
