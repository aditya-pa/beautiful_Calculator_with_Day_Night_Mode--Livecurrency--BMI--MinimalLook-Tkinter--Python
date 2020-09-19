import tkinter
from tkinter import ttk
from tkinter import *
import requests
from bs4 import BeautifulSoup
import csv
import webbrowser
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 
root=tkinter.Tk()
var=''
hist=''
v="0"
photo1=PhotoImage(file = 'A2.png')
img1=photo1
BR="#d3d3d3"
FR="#000000"
DBR="#FFFFFF"
DFR="#000000"
HBR="#849ae3"
HFR="#ffffff"
sub="#ffffff"
B=0
flag=False
f=True
def exchange():    
    frame_E0=Frame(Ealf)
    frame_E0.grid(row=0,column=0)
    frame_E1=Frame(Ealf)
    frame_E1.grid(row=1,column=0)
    frame_E2=Frame(Ealf)
    frame_E2.grid(row=2,column=0)
    frame_E3=Frame(Ealf)
    frame_E3.grid(row=3,column=0)
    frame_E4=Frame(Ealf)
    frame_E4.grid(row=4,column=0)
    frame_E5=Frame(Ealf)
    frame_E5.grid(row=5,column=0)
    
    def click(event):
        global v
        if v=='0':
            v=event.char
        else:
            v=v+event.char
        displaychar1.set(v)
    def writing_data(w):
        with open("money_list.csv",'w',newline="") as csv_file:
            csv_writer=csv.writer(csv_file)
            for i,j in w.items():
                csv_writer.writerow([i,j])
    def getting_data():
        return_list=[]
        with open("money_list.csv",'r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for i in csv_reader:
                return_list.append(i)
        return(return_list)
    def convert(destination,money):
        dict1={}
        final_data=getting_data()
        for i in final_data:
            dict1[i[0]]=i[1]
        rate=float(dict1[destination])
        return money/rate 
    def convert2(destination,money):
        dict1={}
        final_data=getting_data()
        for i in final_data:
            dict1[i[0]]=i[1]
        rate=float(dict1[destination])
        return money*rate
    def solve(event):
        s=clicked.get()
        d=clicked1.get()
        m=int(v)
        if s==d:
            displaychar.set(str(m))
        elif s=='Rupee':
            displaychar.set(round(convert(d,m),2))
        elif d=='Rupee':
            displaychar.set(round(convert2(s,m)))
        else:
            displaychar.set(round(convert(d,(convert2(s,m))),2))
    def Eclear(event):
        global v
        v="0"
        displaychar1.set("0")
        displaychar.set("0")
    def Ebackspace(event):
        global v
        if v=="" or v=="0":
            v="0"
        else:
            v=v[:-2]
        displaychar1.set(v)
    def defocus(event):
        Ealf.focus_set()  
    Ealf.tkraise()
    Ealf.focus_set()
    Ealf.bind('0',click)
    Ealf.bind('<Return>',solve)
    Ealf.bind('1',click)
    Ealf.bind('2',click)
    Ealf.bind('3',click)
    Ealf.bind('4',click)
    Ealf.bind('5',click)
    Ealf.bind('6',click)
    Ealf.bind('7',click)
    Ealf.bind('8',click)
    Ealf.bind('9',click)
    Ealf.bind('9',click)
    Ealf.bind('.',click)
    Ealf.bind('<Delete>',Eclear)
    Ealf.bind('<BackSpace>',Ebackspace) 
    URL="https://www.x-rates.com/table/?from=INR&amount=1"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.163 Safari/537.36"}
    
    whole_list={}
    try:
        page=requests.get(URL,headers = headers)
        soup=BeautifulSoup(page.content,"html.parser")
        table=soup.find("table",attrs = {"class":"ratesTable"})
        for row in table.tbody.findAll("tr"):
            
            cells=row.findAll("td")
            rowa=[i.text for i in cells]
            whole_list[rowa[0]]=rowa[2]
        writing_data(whole_list)
        final_data=getting_data()
            
    except:
        final_data=getting_data()

    mainmenu1 = Menubutton(Ealf, image=image ,background=DBR,activebackground=HBR)
    mainmenu1.grid(row=0,column=0,sticky=W+N)
    submenu1 = Menu(mainmenu1,tearoff = 0,background=DBR,
    foreground=FR, activebackground=HBR,activeforeground=HFR)
    mainmenu1.config(menu=submenu1,)
    submenu1.add_command(label="DAY/NIGHT",command=change)
    submenu1.add_command(label="About",command=about_me)
    submenu1.add_command(label="Basic",command=basic)
    submenu1.add_separator()
    submenu1.add_command(label="Quit",command=destroy)
    option=["Rupee","US Dollar","Euro","British Pound","Australian Dollar","Canadian Dollar",
    "Singapore Dollar","Swiss Franc","Malaysian Ringgit","Japanese Yen","Chinese Yuan Renminbi"]
    clicked=StringVar()
    clicked.set(option[0])
    clicked1=StringVar()
    clicked1.set(option[0])
    displaychar=StringVar()
    displaychar1=StringVar()
    displaychar1.set(v)    
    drop=ttk.Combobox(frame_E1,state="readonly",textvariable=clicked,width=37)
    drop['values']=option
    drop.grid()
    drop.bind("<FocusIn>", defocus)
    labelE1=Label(frame_E2,font=('Verdana',20),textvariable = displaychar1,)
    labelE1.grid()
    drop2=ttk.Combobox(frame_E3,state="readonly",textvariable=clicked1,width=37)
    drop2['values']=option 
    drop2.grid()
    drop2.bind("<FocusIn>", defocus)
    labelE2=Label(frame_E4,font=('Verdana',20),textvariable = displaychar)
    labelE2.grid()
    button_1=Button(frame_E5,text="Convert",command=solve)
    button_1.grid()
    button_3=Button(frame_E5,text="clear",relief='raised',command=Eclear)
    button_3.grid()


    
def basic():
    calf.tkraise()
    calf.focus_set()
def about_me():
    st='''it is developed by Aditya Pandey
    ir fjkjkaadvjknsv
    njsvnv avivn'''
    aalf.tkraise()
    aalf.focus_set()
    imgvar1 = PhotoImage(file='menu.png')
    image = imgvar1.subsample(15,20)
    mainmenu1 = Menubutton(aalf, image=image ,background=DBR,activebackground=HBR)
    mainmenu1.grid(row=0,column=0,sticky=W+N)
    submenu1 = Menu(mainmenu1,tearoff = 0,background=DBR,
    foreground=FR, activebackground=HBR,activeforeground=HFR)
    mainmenu1.config(menu=submenu1,)
    submenu1.add_command(label="DAY/NIGHT",command=change)
    submenu1.add_command(label="basic",command=basic)
    submenu1.add_command(label="Currency",command=exchange)
    submenu1.add_separator()
    submenu1.add_command(label="Quit",command=destroy)
    label_t=Label(aalf,background=DBR,text="About",font = ('verdana',10,'bold'))
    label_t.grid(row=0,column=1)
    label_about=Label(aalf, text = st, font =('Verdana', 13))
    label_about.grid()
    pt = PhotoImage(file = "A.png")
    pe = pt.subsample(1,1)
    b_2=Button(aalf, text = 'Linkedin', relief='groove',compound = LEFT,command=openlinkedin,font = ('verdana',22))
    b_2.grid(row=1,column=0)
    b_3=Button(aalf, text = 'Github',  relief='groove',compound = LEFT,command=github,font = ('verdana',22))
    b_3.grid(row=2,column=0)
    b_1=Button(aalf, width=50,image = pe,compound = LEFT,command=openlinkedin)
    b_1.grid(row=4,column=0)
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
        HBR="#849ae3"
        HFR="#ffffff"
        invert_colours()
        flag=False
    else:
        BR="#000000"
        FR="#b5b3b3"
        DBR="#383737"
        DFR="#808080"
        HBR="#c7c1c1"
        HFR="#ffffff"
        invert_colours()
        flag=True
def invert_colours():
    (
        aalf.config(bg=DBR)        
    )
    root.config(bg=DBR)
    frame_t.config(bg=DBR)
    mainmenu1.config(background=DBR,activebackground=HBR) 
    submenu1.config(background=DBR,foreground=FR, activebackground=HBR,activeforeground=HFR)   
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
    image=img1,
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
    label_t.config(
    background = DBR,
    fg = DFR,)
    label.config(
    background = DBR,
    fg = DFR,)
def destroy():
    root.destroy()
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
        if (var[-1] == "." or var[-1] == ")" or var[-1] == "*" or var[-1] == "-" or var[-1] == "/" or var[-1] == "+" or var[-1] == "**" or var[-1] == "**2" or var[-1] == "**0.5") and v == '.':
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
        if (var[-1] == "." or var[-1] == ")" or var[-1] == "*" or var[-1] == "-" or var[-1] == "/" or var[-1] == "+" or var[-1] == "**" or var[-1] == "**2" or var[-1] == "**0.5") and v == '.':
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
    elif (var[0:2] == '-(' or var [0:2]=='(-')and var[-1] == ')':
        var=var[2:]
        var=var[:-1]
    else:
        var="-(" + var + ")"
    data.set(var)   
def delete():
    global var
    try:
        if var[-1]==')':
            for i,j in enumerate(var):
                if j=='(':
                    var=var[:i]+var[i+1:]


        var=var[:-1]
        data.set(var)
    except:
        pass      
def c():
    global var
    global hist
    try:
        if var=='':
            hist=''
            label.config(text=hist)
        else:
            var=""
            data.set(var)
    except:
        pass
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
def clicked_history(event):
    global hist
    global var
    data.set(hist)
    var=hist
    hist=""
    label.config(text=hist)
root.geometry("300x520")
root.resizable(1,1)
root.title("Calculator")
icon=PhotoImage(file = "calculator.png")
root.tk.call('wm','iconphoto',root._w,icon)
root.config(bg=DBR)
calf=Frame(root,bg=DBR)
calf.grid(row=0,column=0,sticky = N+S+W+E)
Ealf=Frame(root,bg=DBR)
Ealf.grid(row=0,column=0,sticky = N+S+W+E)
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

frame_t=Frame(calf,bg=DBR)
frame_t.pack(expand = True,fill = 'both')
imgvar1 = PhotoImage(file='menu.png')
image = imgvar1.subsample(15,20)
mainmenu1 = Menubutton(frame_t, image=image ,background=DBR,activebackground=HBR)
mainmenu1.grid(row=0,column=0,sticky=W+N)
submenu1 = Menu(mainmenu1,tearoff = 0,background=DBR,
foreground=FR, activebackground=HBR,activeforeground=HFR)
mainmenu1.config(menu=submenu1,)
submenu1.add_command(label="DAY/NIGHT",command=change)
submenu1.add_command(label="About",command=about_me)
submenu1.add_command(label="Currency",command=exchange)
submenu1.add_separator()
submenu1.add_command(label="Quit",command=destroy)
data=StringVar()
data.set(var)
frame_x=Frame(calf)
frame_x.pack(side="top",expand=True,fill='both')
frame_1=Frame(calf)
frame_1.pack(expand = True,fill = 'both')
frame_2=Frame(calf)
frame_2.pack(expand = True,fill = 'both')
frame_3=Frame(calf)
frame_3.pack(expand = True,fill = 'both')
frame_4=Frame(calf)
frame_4.pack(expand = True,fill = 'both')
frame_5=Frame(calf)
frame_5.pack(expand = True,fill = 'both')
frame_6=Frame(calf)
frame_6.pack(expand = True,fill = 'both')
frame_7=Frame(calf)
frame_7.pack(expand = True,fill = 'both')
label_t=Label(frame_t,background=DBR,text="BASIC",font = ('verdana',10,'bold'))
label_t.grid(row=0,column=1)
label_2=Label(frame_1,background=DBR)
label_2.pack(expand = True,fill = 'both')
label=Label(frame_x,background=DBR,text = hist,font = ('verdana',20),anchor = 'se')
label.bind('<Button-1>',clicked_history)
label.pack(expand = True,fill = 'both')
entry_1=Label(frame_1,
              textvariable = data,
              font = ('verdana',22),
              background = DBR,
              anchor = 'se',
              width=4,
              border = 0,
              fg = DFR)
entry_1.pack(expand = True,fill = 'both')
button_1=Button(
    frame_2,
    command = lambda:clicked("1"),
    text = '1',
    border = B,
    width=3,
    relief = 'groove',
    background = BR,
    fg = FR,
    font = ('verdana',22))
button_1.pack(side = 'left',expand = True,fill = 'both')
button_1.bind('<Enter>',entered1)
button_1.bind('<Leave>',leave1)
button_2=Button(
    frame_2,
    command = lambda:clicked("2"),
    border = B,
    background = BR,
    fg = FR,
    width=3,
    text = '2',
    relief = 'groove',
    font = ('verdana',22))
button_2.pack(side = 'left',expand = True,fill = 'both')
button_2.bind('<Enter>',entered2)
button_2.bind('<Leave>',leave2)
button_3=Button(
    frame_2,
    command = lambda:clicked("3"),
    border = B,
    background = BR,
    fg = FR,
    width=3,
    text = '3',
    relief = 'groove',
    font = ('verdana',22))
button_3.pack(side = 'left',expand = True,fill = 'both')
button_3.bind('<Enter>',entered3)
button_3.bind('<Leave>',leave3)
button_4=Button(
    frame_2,
    command = lambda:clicked("4"),
    border = B,
    background = BR,
    fg = FR,
    width=3,
    text = '4',
    relief = 'groove',
    font = ('verdana',22))
button_4.pack(side = 'left',expand = True,fill = 'both')
button_4.bind('<Enter>',entered4)
button_4.bind('<Leave>',leave4)
button_5=Button(
    frame_3,
    command = lambda:clicked("5"),
    border = B,
    background = BR,
    fg = FR,
    width=3,
    text = '5',
    relief = 'groove',
    font = ('verdana',22))
button_5.pack(side = 'left',expand = True,fill = 'both')
button_5.bind('<Enter>',entered5)
button_5.bind('<Leave>',leave5)
button_6=Button(
    frame_3,
    command = lambda:clicked("6"),
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    text = '6',
    font = ('verdana',22))
button_6.pack(side = 'left',expand = True,fill = 'both')
button_6.bind('<Enter>',entered6)
button_6.bind('<Leave>',leave6)
button_7=Button(
    frame_3,
    command = lambda:clicked("7"),
    relief = 'groove',
    text = '7',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    font = ('verdana',22))
button_7.pack(side = 'left',expand = True,fill = 'both')
button_7.bind('<Enter>',entered7)
button_7.bind('<Leave>',leave7)
button_8=Button(
    frame_3,
    command = lambda:clicked("8"),
    relief = 'groove',
    text = '8',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    font = ('verdana',22))
button_8.pack(side = 'left',expand = True,fill = 'both')
button_8.bind('<Enter>',entered8)
button_8.bind('<Leave>',leave8)
button_9=Button(
    frame_4,
    command = lambda:clicked("9"),
    text = '9',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',

    font = ('verdana',22))
button_9.pack(side = 'left',expand = True,fill = 'both')
button_9.bind('<Enter>',entered9)
button_9.bind('<Leave>',leave9)
button_0=Button(
    frame_4,
    command = lambda:clicked("0"),
    text = '0',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_0.pack(side = 'left',expand = True,fill = 'both')
button_0.bind('<Enter>',entered0)
button_0.bind('<Leave>',leave0)
button_=Button(
    frame_4,
    command = lambda:clicked("."),
    text = '.',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_.pack(side = 'left',expand = True,fill = 'both')
button_.bind('<Enter>',entered_)
button_.bind('<Leave>',leave_)
button_pm=Button(
    frame_4,
    command = lambda:pm(),
    text = '±',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_pm.pack(side = 'left',expand = True,fill = 'both')
button_pm.bind('<Enter>',enteredpm)
button_pm.bind('<Leave>',leavepm)
button_p=Button(
    frame_6,
    command = lambda:clicked("**"),
    border = B, 
    background = BR,
    fg = FR,
    width=3,
    text = '^',
    relief = 'groove',
    font = ('verdana',22))
button_p.pack(side = 'left',expand = True,fill = 'both')
button_p.bind('<Enter>',enteredp)
button_p.bind('<Leave>',leavep)
button_u=Button(
    frame_6,
    command = lambda:clicked("**0.5"),
    text = '√x',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_u.pack(side = 'left',expand = True,fill = 'both')
button_u.bind('<Enter>',enteredu)
button_u.bind('<Leave>',leaveu)
button_square=Button(
    frame_6,
    command = lambda:clicked("**2"),
    text = 'x²',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_square.pack(side = 'left',expand = True,fill = 'both')
button_square.bind('<Enter>',enteredsquare)
button_square.bind('<Leave>',leavesquare)
button_photo=Button(
    frame_6,
    border = B,
    background = BR,
    fg = FR,
    command = delete,
    image = img1,
    
    relief = 'groove',
    font = ('verdana',22),
    width = 58)
button_photo.pack(side = 'left',expand = True,fill = 'both')
button_photo.bind('<Enter>',enteredphoto)
button_photo.bind('<Leave>',leavephoto)
button_plus=Button(
    frame_5,
    command = lambda:clicked("+"),
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    text = '+',
    font = ('verdana',22))
button_plus.pack(side = 'left',expand = True,fill = 'both')
button_plus.bind('<Enter>',enteredplus)
button_plus.bind('<Leave>',leaveplus)
button_minus=Button(
    frame_5,
    command = lambda:clicked("-"),
    text = '-',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_minus.pack(side = 'left',expand = True,fill = 'both')
button_minus.bind('<Enter>',enteredminus)
button_minus.bind('<Leave>',leaveminus)
button_mul=Button(
    frame_5,
    command = lambda:clicked("*"),
    text = '*',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_mul.pack(side = 'left',expand = True,fill = 'both')
button_mul.bind('<Enter>',enteredmul)
button_mul.bind('<Leave>',leavemul)
button_div=Button(
    frame_5,
    command = lambda:clicked("/"),
    text = '/',
    border = B,
    background = BR,
    fg = FR,
    width=3,
    relief = 'groove',
    font = ('verdana',22))
button_div.pack(side = 'left',expand = True,fill = 'both')
button_div.bind('<Enter>',entereddiv)
button_div.bind('<Leave>',leavediv)
button_e=Button(
    frame_7,
    command = lambda:solve(),
    text = '=',
    font = ('verdana',22),
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    width = 10)
button_e.pack(side = 'left',expand = True,fill = 'both')
button_e.bind('<Enter>',enterede)
button_e.bind('<Leave>',leavee)
button_c=Button(
    frame_7,
    command = lambda:c(),
    text = 'C',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    width=3,
    font = ('verdana',22))
button_c.pack(side = 'left',expand = True,fill = 'both')
button_c.bind('<Enter>',enteredc)
button_c.bind('<Leave>',leavec)
root.mainloop()

    
