import tkinter as tk
import math

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()
root.title("Weird Calculator")
memorynumber = 0

# creating input fields widget
e = tk.Entry(root, width=50, borderwidth=3)
e.grid(row=0, column=0, columnspan=5, padx=8, pady=8)

def addnum(number):
    valnow = str(e.get())
    e.delete(0, tk.END)
    e.insert(0, valnow + number)

def clearnum():
    global memorynumber
    memorynumber = 0
    e.delete(0, tk.END)

def addopr():
    screennumber = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(screennumber) + "+")

def subopr():
    screennumber = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(screennumber) + "-")

def mulopr():
    screennumber = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(screennumber) + "x")

def divopr():
    screennumber = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(screennumber) + "/")

def dotopr():
     screennumber = e.get()
     e.delete(0, tk.END)
     e.insert(0, str(screennumber) + ".")

def powopr():
    screennumber = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(screennumber) + "^")


def equalopr():
    operationlist = ["+", "-", "x", "/"]
    eqnscreen = str(e.get())
    oprindex = [-1, int(len(eqnscreen))]

    for i in range(len(eqnscreen)):
        if eqnscreen[i] in operationlist:
            oprindex.append(i)


    oprindex.sort()

    valuelist = []
    for i in range(len(oprindex)):
        try:
            valuelist.append(float(eqnscreen[oprindex[i]+1:oprindex[i+1]]))

        except:
            # valuelist.append(eqnscreen[oprindex[i]+1:oprindex[i+1]])
            pass
    print(valuelist)

    del oprindex[0]
    del oprindex[-1]
    print(oprindex)

    global memorynumber
    memorynumber = valuelist[0]

    for i in range(len(oprindex)):
        try:
            if eqnscreen[oprindex[i]] == "+":
                memorynumber += float(valuelist[i+1])
            elif eqnscreen[oprindex[i]] == "-":
                memorynumber -= float(valuelist[i+1])
            elif eqnscreen[oprindex[i]] == "x":
                memorynumber *= float(valuelist[i+1])
            elif eqnscreen[oprindex[i]] == "/":
                memorynumber /= float(valuelist[i+1])
        except:
            pass


    e.delete(0, tk.END)
    e.insert(0, memorynumber)



def trial():
    return

padxvar = 13
padyvar = 13
widthvar = 8
# define text button
buclear = tk.Button(root, text="clear", padx=padxvar, pady=padyvar, width=widthvar, command=clearnum)
bu1 = tk.Button(root, text="1", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("1"))
bu2 = tk.Button(root, text="2", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("2"))
bu3 = tk.Button(root, text="3", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("3"))
bu4 = tk.Button(root, text="4", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("4"))
bu5 = tk.Button(root, text="5", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("5"))
bu6 = tk.Button(root, text="6", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("6"))
bu7 = tk.Button(root, text="7", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("7"))
bu8 = tk.Button(root, text="8", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("8"))
bu9 = tk.Button(root, text="9", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("9"))
bu0 = tk.Button(root, text="0", padx=padxvar, pady=padyvar, width=widthvar, command=lambda: addnum("0"))
budot = tk.Button(root, text=".", padx=padxvar, pady=padyvar, width=widthvar, command=dotopr)
bueq = tk.Button(root, text="=", padx=padxvar, pady=padyvar, width=widthvar, command=equalopr)

# define apps button
buword = tk.Button(root, text="word", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
buexcel = tk.Button(root, text="excel", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
bupad = tk.Button(root, text="pad", padx=padxvar, pady=padyvar, width=widthvar, command=trial)

# define functions buttons
buexp = tk.Button(root, text="e", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
bulog = tk.Button(root, text="log", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
buln = tk.Button(root, text="ln", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
butan = tk.Button(root, text="tan", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
bucos = tk.Button(root, text="cos", padx=padxvar, pady=padyvar, width=widthvar, command=trial)
busin = tk.Button(root, text="sin", padx=padxvar, pady=padyvar, width=widthvar, command=trial)

# define operations buttons
buadd = tk.Button(root, text="+", padx=padxvar, pady=padyvar, width=widthvar, command=addopr)
busub = tk.Button(root, text="-", padx=padxvar, pady=padyvar, width=widthvar, command=subopr)
bumul = tk.Button(root, text="x", padx=padxvar, pady=padyvar, width=widthvar, command=mulopr)
budiv = tk.Button(root, text="/", padx=padxvar, pady=padyvar, width=widthvar, command=divopr)
bupow = tk.Button(root, text="power", padx=padxvar, pady=padyvar, width=widthvar, command=powopr)

# put button onto the screen
buttonlist = [buclear, bupad, buexcel, buexp, buadd, bu1, bu2, bu3, buln, busub, bu4, bu5, bu6, busin, bumul, bu7, bu8, bu9, bucos, budiv, bueq, budot, bu0, butan, bupow]
counter = 0
for j in range(1, 6):
    for i in range(0, 5):
        buttonlist[counter].grid(row=j, column=i)
        counter += 1



mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=trial, fg="black", bg="yellow") # state=tk.DISABLED

# everthing of applications are looping constantly
root.mainloop()
