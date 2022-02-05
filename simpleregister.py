import tkinter as tk

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()

# creating input fields widget
e = tk.Entry(root, width=23, bg="pink", fg="black", borderwidth=3)
e.pack()
e.insert(0, "Enter your name: ")

e1 = tk.Entry(root, width=23, bg="yellow", fg="black", borderwidth=3)
e1.pack()
e1.insert(1, "Enter your student id: ")

def onceclick():
    myoutput = "You enter " + e.get() + " and " + e1.get()
    mylabel = tk.Label(root, text=myoutput)
    mylabel.pack()

mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=onceclick, fg="blue", bg="grey") # state=tk.DISABLED
mybutton.pack()

# everthing of applications are looping constantly
root.mainloop()
