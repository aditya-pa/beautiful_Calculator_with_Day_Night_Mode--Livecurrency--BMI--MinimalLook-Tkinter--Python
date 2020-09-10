import tkinter
import webbrowser
from tkinter import *
root=tkinter.Tk()
var=''
hist=''
BR="#d3d3d3"
FR="#000000"
DBR="#FFFFFF"
DFR="#000000"
HBR="#4169E6"
HFR="#ffffff"
B=0
flag=False
f=True
def basic():
    calf.tkraise()
    calf.focus_set()
def about_me():
    st='it is developed by Aditya Pandey'
    aalf.tkraise()
    aalf.focus_set()
    label_about=Label(aalf, text = st, font =('Verdana', 13))
    label_about.grid(row=0,column=0)
    pt = PhotoImage(file = "A.png")
    pe = photo.subsample(3, 3)
    Button(aalf, text = 'Click Me !', image = pe,compound = LEFT,command=openlinkedin).grid(row=3,column=0)
    lin=Button(aalf, text = 'Linkedin', relief='groove',compound = LEFT,command=openlinkedin,font = ('verdana',22))
    lin.grid(row=1,column=0)
    git=Button(aalf, text = 'Github',  relief='groove',compound = LEFT,command=github,font = ('verdana',22))
    git.grid(row=2,column=0)
    mainloop() 
  

def openlinkedin():
    webbrowser.open('https://www.linkedin.com/in/aditya-pa/')
def github():
    webbrowser.open('https://github.com/aditya-pa/calculator')

def change():
    global flag
    global BR
    global FR
    global DBR
    global DFR
    global HBR
    global HFR
    if flag:
        BR="#d3d3d3"
        FR="#000000"
        DBR="#FFFFFF"
        DFR="#000000"
        HBR="#4169E6"
        HFR="#ffffff"
        invert_colours()
        flag=False
    else:
        BR="#000000"
        FR="#696969"
        DBR="#f5f5f5"
        DFR="#808080"
        HBR="#808080"
        HFR="#ffffff"
        invert_colours()
        flag=True

def invert_colours():
    button_1.config(
    background = BR,
    fg = FR,
    border=B)
    button_2.config(
    background = BR,
    fg = FR,
    border=B)
    button_3.config(
    background = BR,
    fg = FR,
    border=B)
    button_4.config(
    background = BR,
    fg = FR,
    border=B)
    button_5.config(
    background = BR,
    fg = FR,
    border=B)
    button_6.config(
    background = BR,
    fg = FR,
    border=B)
    button_7.config(
    background = BR,
    fg = FR,
    border=B)
    button_8.config(
    background = BR,
    fg = FR,
    border=B)
    button_9.config(
    background = BR,
    fg = FR,
    border=B)
    button_0.config(
    background = BR,
    fg = FR,
    border=B)
    button_.config(
    background = BR,
    fg = FR,
    border=B)
    button_plus.config(
    background = BR,
    fg = FR,
    border=B)
    button_minus.config(
    background = BR,
    fg = FR,
    border=B)
    button_photo.config(
    background = BR,
    fg = FR,
    border=B)
    button_square.config(
    background = BR,
    fg = FR,
    border=B)
    button_mul.config(
    background = BR,
    fg = FR,
    border=B)
    button_e.config(
    background = BR,
    fg = FR,
    border=B)
    button_c.config(
    background = BR,
    fg = FR,
    border=B)
    button_pm.config(
    background = BR,
    fg = FR,
    border=B)
    button_p.config(
    background = BR,
    fg = FR,
    border=B)
    button_u.config(
    background = BR,
    fg = FR,
    border=B)
    button_div.config(
    background = BR,
    fg = FR,
    border=B)
    entry_1.config(
    background = DBR,
    fg = DFR,)
    label_2.config(
    background = DBR,
    fg = DFR,)
    label.config(
    background = DBR,
    fg = DFR,)
    root.config(
    background = DBR,
    )
    frame_1.config(
    background = DBR
    )
    frame_x.config(
    background = DBR
    )

    
    
def entered1(event):
    button_1.config(
        background = HBR,
        fg = HFR,)


def leave1(event):
    button_1.config(
        background = BR,
        fg = FR,)


def entered2(event):
    button_2.config(
        background = HBR,
        fg = HFR)


def leave2(event):
    button_2.config(
        background = BR,
        fg = FR)


def entered3(event):
    button_3.config(
        background = HBR,
        fg = HFR)


def leave3(event):
    button_3.config(
        background = BR,
        fg = FR)

def entered4(event):
    button_4.config(
        background = HBR,
        fg = HFR)


def leave4(event):
    button_4.config(
        background = BR,
        fg = FR)


def entered5(event):
    button_5.config(
        background = HBR,
        fg = HFR)
        


def leave5(event):
    button_5.config(
        background = BR,
        fg = FR)


def entered6(event):
    button_6.config(
        background = HBR,
        fg = HFR)
        

def leave6(event):
    button_6.config(
        background = BR,
        fg = FR)
def entered7(event):
    button_7.config(
        background = HBR,
        fg = HFR)
def leave7(event):
    button_7.config(
        background = BR,
        fg = FR)
def entered8(event):
    button_8.config(
        background = HBR,
        fg = HFR)
def leave8(event):
    button_8.config(
        background = BR,
        fg = FR)
def entered9(event):
    button_9.config(
        background = HBR,
        fg = HFR)
def leave9(event):
    button_9.config(
        background = BR,
        fg = FR)
def entered0(event):
    button_0.config(
        background = HBR,
        fg = HFR)
def leave0(event):
    button_0.config(
        background = BR,
        fg = FR)
def entered_(event):
    button_.config(
        background = HBR,
        fg = HFR)
def leave_(event):
    button_.config(
        background = BR,
        fg = FR)
def enteredplus(event):
    button_plus.config(
        background = HBR,
        fg = HFR)
def leaveplus(event):
    button_plus.config(
        background = BR,
        fg = FR)
def enteredminus(event):
    button_minus.config(
        background = HBR,
        fg = HFR)
def leaveminus(event):
    button_minus.config(
        background = BR,
        fg = FR)
def enteredphoto(event):
    button_photo.config(
        background = HBR,)
def leavephoto(event):
    button_photo.config(
        background = BR,)
def enteredsquare(event):
    button_square.config(
        background = HBR,
        fg = HFR)
def leavesquare(event):
    button_square.config(
        background = BR,
        fg = FR)
def enteredmul(event):
    button_mul.config(
        background = HBR,
        fg = HFR)
def leavemul(event):
    button_mul.config(
        background = BR,
        fg = FR)
def enterede(event):
    button_e.config(
        background = HBR,
        fg = HFR)
def leavee(event):
        button_e.config(
        background = BR,
        fg = FR)
def enteredc(event):
    button_c.config(
        background = HBR,
        fg = HFR)
def leavec(event):
    button_c.config(
        background = BR,
        fg = FR)
def enteredpm(event):
    button_pm.config(
        background = HBR,
        fg = HFR)
def leavepm(event):
    button_pm.config(
        background = BR,
        fg = FR)
def enteredp(event):
    button_p.config(
        background = HBR,
        fg = HFR)
def leavep(event):
    button_p.config(
        background = BR,
        fg = FR)
def enteredu(event):
    button_u.config(
        background = HBR,
        fg = HFR)
def leaveu(event):
    button_u.config(
        background = BR,
        fg = FR)
def entereddiv(event):
    button_div.config(
        background = HBR,
        fg = HFR)
def leavediv(event):
    button_div.config(
        background = BR,
        fg = FR)
def clicked1(v):
    global var
    if len(var) > 1:
        if var[-1] == "." and v == '.':
            pass

        elif var[-1] == "+":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "+":
                pass
            else:
                var=var + v
        elif var[-1] == "-":
            if v == '+':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "-":
                pass
            else:
                var=var + v



        elif var[-1] == "*":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "*":
                pass
            else:
                var=var + v

        elif var[-1] == "/":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "/":
                pass
            else:
                var=var + v



        else:
            var=var + v
    else:
        var=var + v
    data.set(var)
def clicked(v):
    global var
    if len(var) == 1 and var[0] == "0":
        if v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**":
            var=var + v
        else:
            var=v
        data.set(var)
    elif len(var) == 0:
        if v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**":
            var=var + "0" + v
        else:
            var=var + v
    elif var == '(-0)':
        if not (v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**"):
            var="(-" + v + ")"
        else:
            var=var + v
    elif var[0:2] == '(-' and var[-1] == ')':
        if not (v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**"):
            var=var[:-1] + v + ")"

        else:
            var=var + v

    elif len(var) > 5 and var[-5:] == '**0.5':
        if var[-5:] == "**0.5":
            if v == '+':
                var=var[:-5]
                var=var + v
            elif v == '*':
                var=var[:-5]
                var=var + v
            elif v == '/':
                var=var[:-5]
                var=var + v
            elif v == '-':
                var=var[:-5]
                var=var + v
            elif v == "**":
                var=var[:-5]
                var=var + v

            elif v == "**2":
                var=var[:-5]
                var=var + v
            elif v == "**0.5":
                pass
            else:
                var=var + v
        else:
            clicked1(v)

    elif len(var) > 3 and var[-3:] == '**2':
        if var[-3:] == "**2":
            if v == '+':
                var=var[:-3]
                var=var + v
            elif v == '*':
                var=var[:-3]
                var=var + v
            elif v == '/':
                var=var[:-3]
                var=var + v
            elif v == '-':
                var=var[:-3]
                var=var + v
            elif v == "**":
                var=var[:-3]
                var=var + v
            elif v == "**0.5":
                var=var[:-3]
                var=var + v
            elif v == "**2":
                pass
            else:
                var=var + v
        else:
            clicked1(v)

    elif len(var) > 2 and var[-2:] == '**':
        if var[-2:] == "**":

            if v == '+':
                var=var[:-2]
                var=var + v
            elif v == '*':
                var=var[:-2]
                var=var + v
            elif v == '/':
                var=var[:-2]
                var=var + v
            elif v == '-':
                var=var[:-2]
            elif v == "**0.5":
                var=var[:-2]
                var=var + v
            elif v == "**2":
                var=var[:-2]
                var=var + v
            elif v == "**":
                pass
            else:
                var=var + v
        else:
            clicked1(v)

    elif len(var) == 2 and var[1] == "0" and var[0] == "-":
        var="(-" + v + ")"


    elif len(var) > 1:
        if var[-1] == "." and v == '.':
            pass
        elif var[-1] == "+":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "+":
                pass
            else:
                var=var + v
        elif var[-1] == "-":
            if v == '+':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "-":
                pass
            else:
                var=var + v



        elif var[-1] == "*":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "*":
                pass
            else:
                var=var + v

        elif var[-1] == "/":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "/":
                pass
            else:
                var=var + v



        else:
            var=var + v
    else:
        var=var + v
    data.set(var)
def pm():
    global var
    if len(var) == 0:
        var="(-0)"
    elif (var[0:2] == '-(' or var[0:2] == '(-') and var[-1] == ')':
        var=var[2:]
        var=var[:-1]
    elif var[0] == '-':
        var=var[1:]
    else:
        var="-(" + var + ")"
    data.set(var)
def delete():
    global var
    if var[-1]==')':
        for i,j in enumerate(var):
            if j=='(':
                var=var[:i]+var[i+1:]
            
            


    var=var[:-1]
    data.set(var)
def c():
    global var,hist
    if var == '':
        hist=''
    label.config(text=hist)
    var=""
    data.set(var)

def solve():
    global var
    global hist
    try:
        hist=var
        label.config(text=hist)
        ans=eval(var)            
        ans=round(ans,4)
        var=str(ans)
            
        if var[0] == "-":
            var="(" + var + ")"
        data.set(var)
        
    except ZeroDivisionError:
        data.set("Can't Divide by Zero")
    except SyntaxError:
        data.set("Syntax Error")
    except:
        data.set("Invalid Input")
def enterpress(event):
    solve()
def click(event):
    clicked(event.char)
def deleteclick(event):
    c()
def backspace(event):
    delete()
def resize():
    global f
    global root
    if f:
        root.resizable(1,1)
        f=False
    else:
        root.resizable(0,0)
        f=True

def clicked_history(event):
    global hist
    global var
    data.set(hist)
    var=hist
    hist=""
    label.config(text=hist)
    
root.geometry("290x418")
root.resizable(0,0)
root.title("Calculator")
icon=PhotoImage(file = "calculator.png")
root.tk.call('wm','iconphoto',root._w,icon)
root.config(bg=DBR)
calf=Frame(root,bg=DBR)
calf.grid(row=0,column=0,sticky = N+S+W+E)
aalf=Frame(root,bg=DBR)
aalf.grid(row=0,column=0,sticky = N+S+W+E)
calf=Frame(root,bg=DBR)
calf.grid(row=0,column=0,sticky = N+S+W+E)
calf.tkraise()
calf.focus_set()
calf.bind('0',click)
calf.bind('<Return>',enterpress)
calf.bind('1',click)
calf.bind('2',click)
calf.bind('3',click)
calf.bind('4',click)
calf.bind('5',click)
calf.bind('6',click)
calf.bind('7',click)
calf.bind('8',click)
calf.bind('9',click)
calf.bind('.',click)
calf.bind('*',click)
calf.bind('+',click)
calf.bind('-',click)
calf.bind('/',click)
calf.bind('<Delete>',deleteclick)
calf.bind('<BackSpace>',backspace)  
menubar = Menu(root) 
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Basic calculator', command = basic) 
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Format', menu = edit)
edit.add_command(label ='DAY/NIGHT MODE', command = change)
edit.add_separator()
edit.add_command(label ='Resize OR NOT', command = resize) 
  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='About', command = about_me) 
  
# display Menu 
root.config(menu = menubar) 



data=StringVar()
data.set(var)
frame_x=Frame(calf,bg=DBR)
frame_x.grid(row = 0, column = 0, sticky = N+S+W+E)
frame_1=Frame(calf,bg=DBR)
frame_1.grid(row = 1, column = 0, sticky = N+S+W+E)
frame_2=Frame(calf)
frame_2.grid(row = 2, column = 0, sticky = N+S+W+E)
frame_3=Frame(calf)
frame_3.grid(row = 3, column = 0, sticky = N+S+W+E)
frame_4=Frame(calf)
frame_4.grid(row = 4, column = 0, sticky = N+S+W+E)
frame_5=Frame(calf)
frame_5.grid(row = 5, column = 0, sticky = N+S+W+E)
frame_6=Frame(calf)
frame_6.grid(row = 6, column = 0, sticky = N+S+W+E)
frame_7=Frame(calf)
frame_7.grid(row = 7, column = 0, sticky = N+S+W+E)
label_2=Label(frame_1,background=DBR,justify='right')
label_2.grid(row = 0, column = 0, sticky = E)
label=Label(frame_x,background=DBR,text = hist,font = ('verdana',18))
label.bind('<Button-1>',clicked_history)
label.grid(row = 0, column = 0)
entry_1=Label(frame_1,
              textvariable = data,
              font = ('verdana',18),
              background = DBR,
              border = 0,
              fg = DFR,)
entry_1.grid(row = 1, column = 1)
button_1=Button(
    frame_2,
    command = lambda:clicked("1"),
    text = '1',
    height = 1,
    width = 4,
    border = B,
    relief = 'groove',
    background = BR,
    fg = FR,
    font = ('verdana',20))
button_1.grid(row = 0, column = 0, sticky = W)
button_1.bind('<Enter>',entered1)
button_1.bind('<Leave>',leave1)
button_2=Button(
    frame_2,
    height = 1,
    width = 4,
    command = lambda:clicked("2"),
    border = B,
    background = BR,
    fg = FR,
    text = '2',
    relief = 'groove',
    font = ('verdana',20))
button_2.grid(row = 0, column = 1, sticky = W,)
button_2.bind('<Enter>',entered2)
button_2.bind('<Leave>',leave2)
button_3=Button(
    frame_2,
    command = lambda:clicked("3"),
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    text = '3',
    relief = 'groove',
    font = ('verdana',20))
button_3.grid(row = 0, column = 2, sticky = W)
button_3.bind('<Enter>',entered3)
button_3.bind('<Leave>',leave3)
button_4=Button(
    frame_2,
    command = lambda:clicked("4"),
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    text = '4',
    relief = 'groove',
    font = ('verdana',20))
button_4.grid(row = 0, column = 3, sticky = W)
button_4.bind('<Enter>',entered4)
button_4.bind('<Leave>',leave4)

button_5=Button(
    frame_3,
    command = lambda:clicked("5"),
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    text = '5',
    relief = 'groove',
    font = ('verdana',20))
button_5.grid(row = 0, column = 0, sticky = W)
button_5.bind('<Enter>',entered5)
button_5.bind('<Leave>',leave5)
button_6=Button(
    frame_3,
    command = lambda:clicked("6"),
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    text = '6',
    font = ('verdana',20))
button_6.grid(row = 0, column = 1, sticky = W)
button_6.bind('<Enter>',entered6)
button_6.bind('<Leave>',leave6)
button_7=Button(
    frame_3,
    command = lambda:clicked("7"),
    relief = 'groove',
    text = '7',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    font = ('verdana',20))
button_7.grid(row = 0, column = 2, sticky = W)
button_7.bind('<Enter>',entered7)
button_7.bind('<Leave>',leave7)
button_8=Button(
    frame_3,
    command = lambda:clicked("8"),
    relief = 'groove',
    text = '8',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    font = ('verdana',20))
button_8.grid(row = 0, column = 3, sticky = W)
button_8.bind('<Enter>',entered8)
button_8.bind('<Leave>',leave8)

button_9=Button(
    frame_4,
    command = lambda:clicked("9"),
    text = '9',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_9.grid(row = 0, column = 0, sticky = W)
button_9.bind('<Enter>',entered9)
button_9.bind('<Leave>',leave9)
button_0=Button(
    frame_4,
    command = lambda:clicked("0"),
    text = '0',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_0.grid(row = 0, column = 1, sticky = W)
button_0.bind('<Enter>',entered0)
button_0.bind('<Leave>',leave0)
button_=Button(
    frame_4,
    command = lambda:clicked("."),
    text = '.',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_.grid(row = 0, column = 2, sticky = W)
button_.bind('<Enter>',entered_)
button_.bind('<Leave>',leave_)
button_pm=Button(
    frame_4,
    command = lambda:pm(),
    text = '±',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_pm.grid(row = 0, column = 3, sticky = W)
button_pm.bind('<Enter>',enteredpm)
button_pm.bind('<Leave>',leavepm)

button_p=Button(
    frame_6,
    command = lambda:clicked("**"),
    border = B,
    background = BR,
    fg = FR,
    height = 1,
    width = 4,
    text = '^',
    relief = 'groove',
    font = ('verdana',20))
button_p.grid(row = 0, column = 0, sticky = W)
button_p.bind('<Enter>',enteredp)
button_p.bind('<Leave>',leavep)
button_u=Button(
    frame_6,
    command = lambda:clicked("**0.5"),
    text = '√x',
    border = B,
    background = BR,
    fg = FR,
    height = 1,
    width = 4,
    relief = 'groove',
    font = ('verdana',20))
button_u.grid(row = 0, column = 1, sticky = W)
button_u.bind('<Enter>',enteredu)
button_u.bind('<Leave>',leaveu)
button_square=Button(
    frame_6,
    command = lambda:clicked("**2"),
    text = 'x²',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_square.grid(row = 0, column = 2, sticky = W)
button_square.bind('<Enter>',enteredsquare)
button_square.bind('<Leave>',leavesquare)
photo=PhotoImage(file = 'A2.png')
button_photo=Button(
    frame_6,
    border = B,
    background = BR,
    fg = FR,
    height = 50,
    width = 72,
    command = delete,
    image = photo,
    
    relief = 'groove',
    font = ('verdana',20))
button_photo.grid(row = 0, column = 3, sticky = W)
button_photo.bind('<Enter>',enteredphoto)
button_photo.bind('<Leave>',leavephoto)

button_plus=Button(
    frame_5,
    command = lambda:clicked("+"),
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    text = '+',
    font = ('verdana',20))
button_plus.grid(row = 0, column = 0, sticky = W)
button_plus.bind('<Enter>',enteredplus)
button_plus.bind('<Leave>',leaveplus)
button_minus=Button(
    frame_5,
    command = lambda:clicked("-"),
    text = '-',
    border = B,
    height = 1,
    width = 4,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_minus.grid(row = 0, column = 1, sticky = W)
button_minus.bind('<Enter>',enteredminus)
button_minus.bind('<Leave>',leaveminus)
button_mul=Button(
    frame_5,
    command = lambda:clicked("*"),
    text = '*',
    border = B,
    background = BR,
    fg = FR,
    height = 1,
    width = 4,
    relief = 'groove',
    font = ('verdana',20))
button_mul.grid(row = 0, column = 2, sticky = W)
button_mul.bind('<Enter>',enteredmul)
button_mul.bind('<Leave>',leavemul)
button_div=Button(
    frame_5,
    command = lambda:clicked("/"),
    text = '/',
    border = B,
    background = BR,
    fg = FR,
    height = 1,
    width = 4,
    relief = 'groove',
    font = ('verdana',20))
button_div.grid(row = 0, column = 3, sticky = W)
button_div.bind('<Enter>',entereddiv)
button_div.bind('<Leave>',leavediv)
button_e=Button(
    frame_7,
    command = lambda:solve(),
    text = '=',
    font = ('verdana',20),
    border = B,
    height = 1,
    width = 10,
    background = BR,
    fg = FR,
    relief = 'groove')
button_e.grid(row = 0, column = 0, sticky = W)
button_e.bind('<Enter>',enterede)
button_e.bind('<Leave>',leavee)
button_c=Button(
    frame_7,
    command = lambda:c(),
    text = 'C',
    border = B,
    background = BR,
    fg = FR,
    height = 1,
    width = 7,
    relief = 'groove',
    font = ('verdana',20))
button_c.grid(row = 0, column = 1, sticky = W)
button_c.bind('<Enter>',enteredc)
button_c.bind('<Leave>',leavec)
root.mainloop()

    
