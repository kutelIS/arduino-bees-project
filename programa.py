from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import linecache
from datetime import date

def Issamusduomenys():
     

    newWindow = Toplevel (window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Bitininko dienoraštis")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="Svarbios žinutės išsamiai").pack()
 

 
# a button widget which will open a
# new window on button click
btn = Button(window,
             text ="Išsamūs duomenys",
             command = Issamusduomenys)


btn.grid(column=2, row=1)



def Ganyklos():

    file1 = open("opcijos.txt", 'r')
    Lines = file1.readlines()

    count = 0

    # Strips the newline character
    for line in Lines:
        count += 1
        z=2
        if (count>1):
            for v in line:
            
                a = line.split(',')
                l1 = [elem.strip().split(',') for elem in a]
            
            for x in l1:
                z+=1
                lbl = Label(window, text=x)
                lbl.grid(column=count-1, row=z)
                
    data=str(linecache.getline("opcijos.txt",1))
    (int(y) for y in data.split(','))
    mylist=data.split(',')
        
    z=0
    for v in mylist:
        z+=1

        v=v.split()
        lbl = Label(window, text=v)
        lbl.grid(column=z, row=2)


                 



new_item.add_command(label='Ganyklos' , command = Ganyklos)

def Nustatymai():
    Nustatymai=Toplevel (window)
    Nustatymai.title ("Nustatymai")
    Nustatymai.geometry('700x800')
    btn = Button(Nustatymai,
             text ="Ganyklų skaičiaus keitimas",
             command = Ganyklusk)
    btn.grid(column=1, row=1)


new_item.add_command(label='Nustatymai' , command = Nustatymai)



    
def Ganyklusk():
    Ganyklusk=Toplevel (window)
    Ganyklusk.title ("Ganyklų skaičiaus keitimas")
    Ganyklusk.geometry('500x200')

    file1 = open("opcijos.txt", 'r')
    Lines = file1.readlines()

    count = 0

    # Strips the newline character
    for line in Lines:
        count += 1
        z=1
        if (count>1):
            for v in line:
            
                a = line.split(',')
                l1 = [elem.strip().split(',') for elem in a]
            
            for x in l1:
                z+=1  
                btn = Button(Ganyklusk, text =x)
                btn.grid(column=count-1, row=z)    

    
    data=str(linecache.getline("opcijos.txt",1))

    (int(y) for y in data.split(','))
    mylist=data.split(',')
    
    

    z=0
    for v in mylist:
        z+=1
        
        

        v=v.split()
        btn = Button(Ganyklusk,
            text =v)
        btn.grid(column=z, row=1)

    
    btn = Button(Ganyklusk,
            text ='Pridėti ganyklą',command=pridettti)
    btn.grid(column=((len(mylist))+1), row=1)





def pridettti():

    root=tk.Tk()
    
    root.geometry("200x200")
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
     
 
    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text = 'Pavadinimas', font=('calibre',10, 'normal'))
    
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    
    # creating a label for password
    passw_label = tk.Label(root, text = 'Avilių skaičius', font = ('calibre',10,'normal'))
    
    # creating a entry for password
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'))
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit')
    
    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    
    #neveikia sitie definai subimt nepaima nieko
    root.mainloop()
     
    def pridetti(entry):
    
        with open("opcijos.txt", "r+") as f:
            old = f.read() 
            f.seek(0) 
            f.write("{},".format(entry) + old)    

    #def submit():
 
        entry=name_var.get()
            
        pridetti(entry)
            
        name_var.set("")
        passw_var.set("")
        
        

today = date.today()
siandienosdata = today.strftime("%Y/%m/%d")


data=str(linecache.getline("test.txt",1))

(int(y) for y in data.split('-'))
a,b,c=(int(x) for x in data.split('-'))
#c=c.rstrip()



aa,bb,cc=(int(x) for x in siandienosdata.split('/'))

if((aa-1)==a and bb==b and cc==c): print('labas') #neveikia int aa blogai kazkas






temperatura=int(linecache.getline("test.txt",2))
temperatura1=int(linecache.getline("test.txt",3))
garsas=int(linecache.getline("test.txt",4))
svoris=int(linecache.getline("test.txt",5))
lietus=int(linecache.getline("test.txt",6))

window = Tk()
window.title("Bitininko dienoraštis")
window.geometry('700x800')
menu = Menu(window)
new_item = Menu(menu)
menu.add_cascade(label='Opcijos', menu=new_item)
window.config(menu=menu)
lbl = Label(window, text="Svarbios šiandienos žinutės:      ")
lbl.grid(column=1, row=1)

window.mainloop()