import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()
root.geometry('500x500')
root.title("Applications Name")
# create icon
root.iconbitmap('calcicon.ico')

# # ------------------------------------------------------------------------------------

# # creating input fields widget (pack system)
# e = tk.Entry(root, width=45, bg="pink", fg="black", borderwidth=3)
# e.pack()
# e.insert(0, "Enter your name: ")
#
# # Button Widget
# def onceclick():
#     myoutput = "You enter " + e.get()
#     mylabel = tk.Label(root, text=myoutput)
#     mylabel.pack()
#
# mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=onceclick, fg="black", bg="yellow") # state=tk.DISABLED
# mybutton.pack()
#
# quitbutton =  tk.Button(root, text="Exit", padx=20, pady=13, command=root.quit)
# quitbutton.pack()

# # ------------------------------------------------------------------------------------

# # creating input fields widget (grid system)
# e = tk.Entry(root, width=80, bg="pink", fg="black", borderwidth=3)
# e.grid(row=0, column=0, columnspan=2)
# e.insert(0, "Enter your name: ")
#
# # Button Widget
# def onceclick():
#     myoutput = "You enter " + e.get()
#     mylabel = tk.Label(root, text=myoutput)
#     mylabel.pack()
#
# mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=onceclick, fg="black", bg="yellow", state=tk.DISABLED)
# mybutton.grid(row=1, column=0)
#
# quitbutton =  tk.Button(root, text="Exit", padx=20, pady=13, command=root.quit)
# quitbutton.grid(row=1, column=1)

# # ------------------------------------------------------------------------------------

# # Define images
# myimg = ImageTk.PhotoImage(Image.open("spiderimg.png"))
# imglabel = tk.Label(image=myimg)
# imglabel.place(x=-20, y=-20)

# # ------------------------------------------------------------------------------------

# # creating label widgets (Text Widget)
# mylabel1 = tk.Label(root, text="Text To Display1")
# mylabel2 = tk.Label(root, text="                ")
# mylabel3 = tk.Label(root, text="Text To Display3")
#
# # showing it on the screen
# # mylabel.pack()
#
# # showing on screen on grid system
# mylabel1.grid(row=0, column=0)
# mylabel2.grid(row=1, column=1)
# mylabel3.grid(row=2, column=5)

# # ------------------------------------------------------------------------------------

# # Radio Button
# myvariable = tk.IntVar() # StringVar()
# # Set the default option
# myvariable.set("2")
#
# def checked(val):
#     mylabel = tk.Label(root, text=val)
#     mylabel.pack()
#
# tk.Radiobutton(root, text="Choice 1", variable=myvariable, value=1, command=lambda: checked(myvariable.get())).pack()
# tk.Radiobutton(root, text="Choice 2", variable=myvariable, value=4, command=lambda: checked(myvariable.get())).pack()
# tk.Radiobutton(root, text="Choice 3", variable=myvariable, value=8, command=lambda: checked(myvariable.get())).pack()
# tk.Label(root, text=myvariable.get()).pack()

# # ------------------------------------------------------------------------------------

# # checkbox
# var = tk.StringVar()
#
# def showvar():
#     mylabel = tk.Label(root, text=var.get()).pack()
#     varpy = var.get()
#     print(varpy)
#
# checkb = tk.Checkbutton(root, text="Choice 1", variable=var, onvalue="Checked", offvalue="Unchecked")
# checkb.deselect()
# checkb.pack()
#
# bu = tk.Button(root, text="Show Text", command=showvar).pack()


# # ------------------------------------------------------------------------------------

# # messages box
# # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
#
# def message():
#     myans = messagebox.askyesno("Message Title", "My message")
#     print(myans)
# tk.Button(root, text="MsgBox", command=message).pack()

# # ------------------------------------------------------------------------------------

# # Dropdown menu
# def showval():
#     mylabel = tk.Label(root, text=clicked.get()).pack()
#
# clicked = tk.StringVar()
# clicked.set("Monday")
#
# dropd = tk.OptionMenu(root, clicked, "Friday", "Saturday", "Sunday")
# dropd.pack()
#
# bu = tk.Button(root, text="Show Me", command=showval).pack()

# # ------------------------------------------------------------------------------------

# everthing of applications are looping constantly
root.mainloop()
