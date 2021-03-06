import tkinter as tk
import math
from PIL import ImageTk, Image
from tkinter import font as tkFont
import subprocess

# everything in tkinter is widgets, creating the root widgets
root = tk.Tk()

# setting widget title and size
root.title("Weird Calculator")
root.geometry('530x580')

# create icon
root.iconbitmap('calcicon2.ico')

# reading image decoration
myimg = ImageTk.PhotoImage(Image.open("calcimgbg.png"))
label = tk.Label(root, image = myimg)
label.grid(row=0, column=4)

# setting image for buttons
clearimg = ImageTk.PhotoImage(file="clearbg.png")
equalimg = ImageTk.PhotoImage(file="equalbg.png")

# setting font style format
fontfamily = tkFont.Font(family='Times New Roman', size=10, weight=tkFont.BOLD)

# creating input fields widget (entry widget)
e = tk.Entry(root, width=60, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

# for the calculation of memory value
memorynumber = 0

# to get the existing value in the screen and concatenate with the new numbers
def addnum(number):
    valnow = str(e.get())
    e.delete(0, tk.END)
    e.insert(0, valnow + number)

# add the math functions together with the numbers
def mathfunc(opr):
    valnow = str(e.get())
    e.delete(0, tk.END)
    e.insert(0, valnow + opr)

# clear everything
def clearnum():
    global memorynumber
    memorynumber = 0
    e.delete(0, tk.END)

# to get the existing value in the screen and concatenate with the operators symbols such as +, -, x, /, ^ and dot
def allopr(oprs):
    screennumber = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(screennumber) + str(oprs))

# handling the complex functions one by one instantly
def calcnow():
    screennumber = e.get()
    # print(screennumber)
    symbollist = []
    for i in range(len(screennumber)-1, -1, -1):
        # print(screennumber[i])
        if screennumber[i] == "^":
            j = i
            power = float(screennumber[i+1:])
            # print(f"power: {power}")
            for k in range(i, -1, -1):
                # print(screennumber[k])
                if screennumber[k] in ["+", "-", "x", "/"]:
                    val = float(screennumber[k+1:j])
                    # print(f"base: {val}")
                    break
                if k == 0:
                    val = float(screennumber[k:j])
                    # print(f"base: {val}")

            rewritevalue = round(val**power, 5)
            # print(rewritevalue)

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
        # print(screennumber[a])
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

# run the program once the button is clicked
def runexcel():
    subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

# only handles all the values seperated by operators sumbols without the name of the mathematical functions
def equalopr():
    operationlist = ["+", "-", "x", "/"]
    eqnscreen = str(e.get())
    # print(eqnscreen)
    oprindex = [-1, int(len(eqnscreen))]
    # print(oprindex)

    for i in range(len(eqnscreen)):
        # not exponential too large value, and initially it is having sign
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
    # print(valuelist)

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
budot = tk.Button(root, text=".", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar,font=fontfamily, command=lambda: allopr("."))

# calculator functions
buclear = tk.Button(root, image=clearimg, width=92, height=85, command=clearnum)
bueq = tk.Button(root, image=equalimg, width=92, height=85, command=equalopr)
buref = tk.Button(root, text="\u21BB", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=calcnow)

# define apps button
buexcel = tk.Button(root, text="excel", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=runexcel)

# define functions buttons
buexp = tk.Button(root, text="EXP", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("EXP"))
buln = tk.Button(root, text="log", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("log"))
butan = tk.Button(root, text="tan", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("tan"))
bucos = tk.Button(root, text="cos", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("cos"))
busin = tk.Button(root, text="sin", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: mathfunc("sin"))

# define operations buttons
buadd = tk.Button(root, text="+", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: allopr("+"))
busub = tk.Button(root, text="-", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: allopr("-"))
bumul = tk.Button(root, text="x", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: allopr("x"))
budiv = tk.Button(root, text="/", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: allopr("/"))
bupow = tk.Button(root, text="power", padx=padxvar, pady=padyvar, width=widthvar, height=heightvar, font=fontfamily, command=lambda: allopr("^"))

# put button onto the screen
buttonlist = [buclear, buref, buexcel, buexp, buadd, bu1, bu2, bu3, buln, busub, bu4, bu5, bu6, busin, bumul, bu7, bu8, bu9, bucos, budiv, bueq, budot, bu0, butan, bupow]
counter = 0
for j in range(1, 6):
    for i in range(0, 5):
        buttonlist[counter].grid(row=j, column=i)
        counter += 1

# everthing of applications are looping constantly
root.mainloop()
