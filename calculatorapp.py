import tkinter as tk
import math
from PIL import ImageTk, Image
from tkinter import font as tkFont

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()
root.title("Weird Calculator")
root.geometry('530x580')

# create icon
root.iconbitmap('calcicon.ico')
memorynumber = 0

# Attach backgroun image decoration
myimg = ImageTk.PhotoImage(Image.open("spiderimg1bg.png"))
label = tk.Label(root, image = myimg)
label.grid(row=0, column=0)

# setting image
clearimg = ImageTk.PhotoImage(file="clearbg.png")
equalimg = ImageTk.PhotoImage(file="equalbg.png")

# setting font
fontfamily = tkFont.Font(family='Times New Roman', size=10, weight=tkFont.BOLD)

# creating input fields widget
e = tk.Entry(root, width=60, borderwidth=10)
e.grid(row=0, column=1, columnspan=4, padx=8, pady=8)

def addnum(number):
    valnow = str(e.get())
    e.delete(0, tk.END)
    e.insert(0, valnow + number)

def mathfunc(opr):
    valnow = str(e.get())
    e.delete(0, tk.END)
    e.insert(0, valnow + opr)

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

def calcnow():
    screennumber = e.get()
    print(screennumber)
    symbollist = []
    for i in range(len(screennumber)-1, -1, -1):
        # print(screennumber[i])
        if screennumber[i] == "^":
            j = i
            power = float(screennumber[i+1:])
            print(f"power: {power}")
            for k in range(i, -1, -1):
                print(screennumber[k])
                if screennumber[k] in ["+", "-", "x", "/"]:
                    val = float(screennumber[k+1:j])
                    print(f"base: {val}")
                    break
                if k == 0:
                    val = float(screennumber[k:j])
                    print(f"base: {val}")
            rewritevalue = round(val**power, 5)
            print(rewritevalue)

    if "cos" in screennumber:
        myindex = screennumber.index("c")
        val = float(screennumber[myindex+3:])
        rewritevalue = str(math.cos(val))
    elif "sin" in screennumber:
        myindex = screennumber.index("s")
        val = float(screennumber[myindex+3:])
        rewritevalue = str(math.sin(val))
    elif "tan" in screennumber:
        myindex = screennumber.index("t")
        val = float(screennumber[myindex+3:])
        rewritevalue = str(math.tan(val))
    elif "EXP" in screennumber:
        myindex = screennumber.index("E")
        val = float(screennumber[myindex+3:])
        rewritevalue = str(math.exp(val))
    elif "log" in screennumber:
        myindex = screennumber.index("l")
        val = float(screennumber[myindex+3:])
        rewritevalue = str(math.log(val))

    for a in range(len(screennumber)-1, -1, -1):
        print(screennumber[a])
        if screennumber[a] in ["+", "-", "x", "/"]:
            putonvalue = str(screennumber[0:a+1]) + str(rewritevalue)
            break
        else:
            try:
                putonvalue = str(rewritevalue)
            except:
                pass

    try:
        e.delete(0, tk.END)
        e.insert(0, putonvalue)
    except:
        pass

def equalopr():
    operationlist = ["+", "-", "x", "/"]
    eqnscreen = str(e.get())
    print(eqnscreen)
    oprindex = [-1, int(len(eqnscreen))]
    print(oprindex)

    for i in range(len(eqnscreen)):
        if eqnscreen[i] in operationlist and eqnscreen[i-1] != "e" and i!=0:
            oprindex.append(i)

    oprindex.sort()
    valuelist = []
    for i in range(len(oprindex)):
        try:
            if oprindex[i] - oprindex[i-1] == 1:
                valuelist.append(float(eqnscreen[oprindex[i]:oprindex[i+1]]))
                del oprindex[i]
            else:
                valuelist.append(float(eqnscreen[oprindex[i]+1:oprindex[i+1]]))
        except:
            # valuelist.append(eqnscreen[oprindex[i]+1:oprindex[i+1]])
            pass
    print(valuelist)

    del oprindex[0]
    del oprindex[-1]
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

padxvar = 10
padyvar = 10
widthvar = 10
heightvar = 4

# define text button
buclear = tk.Button(root, image=clearimg, width=92, height=85, command=clearnum)
bu1 = tk.Button(root, text="1", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: addnum("1"))
bu2 = tk.Button(root, text="2", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("2"))
bu3 = tk.Button(root, text="3", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("3"))
bu4 = tk.Button(root, text="4", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("4"))
bu5 = tk.Button(root, text="5", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("5"))
bu6 = tk.Button(root, text="6", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("6"))
bu7 = tk.Button(root, text="7", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("7"))
bu8 = tk.Button(root, text="8", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("8"))
bu9 = tk.Button(root, text="9", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("9"))
bu0 = tk.Button(root, text="0", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: addnum("0"))
budot = tk.Button(root, text=".", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=dotopr)
bueq = tk.Button(root, image=equalimg, width=92, height=85, command=equalopr)

# define apps button
buword = tk.Button(root, text="word", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=trial)
buexcel = tk.Button(root, text="excel", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=trial)
buref = tk.Button(root, text="\u21BB", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=calcnow)

# define functions buttons
buexp = tk.Button(root, text="EXP", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("EXP"))
buln = tk.Button(root, text="log", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("log"))
butan = tk.Button(root, text="tan", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("tan"))
bucos = tk.Button(root, text="cos", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("cos"))
busin = tk.Button(root, text="sin", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("sin"))

# define operations buttons
buadd = tk.Button(root, text="+", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=addopr)
busub = tk.Button(root, text="-", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=subopr)
bumul = tk.Button(root, text="x", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=mulopr)
budiv = tk.Button(root, text="/", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=divopr)
bupow = tk.Button(root, text="power", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=powopr)

# put button onto the screen
buttonlist = [buclear, buref, buexcel, buexp, buadd, bu1, bu2, bu3, buln, busub, bu4, bu5, bu6, busin, bumul, bu7, bu8, bu9, bucos, budiv, bueq, budot, bu0, butan, bupow]
counter = 0
for j in range(1, 6):
    for i in range(0, 5):
        buttonlist[counter].grid(row=j, column=i)
        counter += 1

mybutton = tk.Button(root, text="Start", padx=20, pady=13, command=trial, fg="black", bg="yellow") # state=tk.DISABLED

# everthing of applications are looping constantly
root.mainloop()
