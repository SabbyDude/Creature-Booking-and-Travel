from tkinter import *
try:
    from tkinter import messagebox
except ImportError:
    # Python 2
    from tkinter import tkMessageBox as messagebox
from tkinter import ttk
import string
import random
rootp = Tk()
rootp.title("SABBYDOOF INC. LIMITED")
rootp.geometry('600x300')
rootp.configure(background = "grey");
Label(rootp,text="Welcome to SabbyDoof Booking and Travel",font="Ubuntu 20",bg="light green",fg="dark green",pady=20,relief="ridge").pack()
def createacc():
    root=Tk()
    root.title('Flight search And booking')
    Label(root,text='BOOKING PAGE',font=('bold',20)).grid(row=0,column=0)
    Label(root,text='Enter your name').grid(row=1,column=0)
    nm=Entry(root,width=20)
    nm.grid(row=1,column=1)
    Label(root,text='Enter your Phone Number').grid(row=2,column=0)
    ph=Entry(root,width=20)
    ph.grid(row=2,column=1)
    Label(root,text='Enter your E-mail').grid(row=3,column=0)
    em=Entry(root,width=20)
    em.grid(row=3,column=1)
    Label(root,text='Travelling From').grid(row=4,column=0)
    tfrom=Entry(root,width=20)
    tfrom.grid(row=4,column=1)
    Label(root,text='Travelling To').grid(row=5,column=0)
    tto=Entry(root,width=20)
    tto.grid(row=5,column=1)
    Label(root,text='Day of Travel DD/MM/YYYY').grid(row=6,column=0)
    date=Entry(root,width=20)
    date.grid(row=6,column=1)
    Label(root,text='Time of Travel HH:MM (24 hrs)').grid(row=7,column=0)
    time=Entry(root,width=20)
    time.grid(row=7,column=1)
    Label(root,text="Choose your Creature").grid(row=8,column=0)
    crt=ttk.Combobox(root,height=5,width=20,values=["Bigfoot Rs.45000","Kraken Rs.80000","Vampire Rs.40000","Zombie Horde Rs.20000","Mermaid Rs.40000","Werewolf Rs.45000","Centaur Rs.45000","Dragon Rs.100000"])
    crt.grid(row=8,column=1)
    def regis():
        jnm=str(nm.get())
        jph=str(ph.get())
        jem=str(em.get())
        jto=str(tto.get())
        jfrom=str(tfrom.get())
        jdt=str(date.get())
        jtm=str(time.get())
        jcr=str(crt.get())
        if jnm=='' or jph=='' or jem=='' or jto=='' or jfrom=='' or jdt=='' or jtm=='' or jcr=='':
            messagebox.showerror("Error C09: Empty Field","You can't leave any field empty")
        else:
            randt1=random.randrange(1000,9999)
            randt2=random.randrange(1000,9999)
            randr=random.randrange(100000,999999)
            randtc1=random.choice(string.ascii_letters)
            randtc2=random.choice(string.ascii_letters)
            randrc=random.choice(string.ascii_letters)
            ticket=str(randt1)+randtc1.upper()+randtc2.upper()+str(randt2)
            crtnum=randrc.upper()+str(randr)
            with open("openbook.txt","a") as f:
                f.write('\n')
                f.write(str(nm.get()))
                f.write('\t')
                f.write(ticket)
                f.write('\t')
                f.write(str(ph.get()))
                f.write('\t')
                f.write(str(em.get()))
                f.write('\t')
                f.write(str(tfrom.get()))
                f.write('\t')
                f.write(str(tto.get()))
                f.write('\t')
                f.write(str(date.get()))
                f.write('\t')
                f.write(str(time.get()))
                f.write('\t')
                f.write(str(crt.get()))
                f.write('\t')
                f.write(crtnum)
                f.write('\n')
            msg=("Dear",jnm)
            messagebox.showinfo("Travel and Creature Details",msg)
            messagebox.showinfo("Ticket Number",ticket)
            messagebox.showinfo("Creature Number",crtnum)
            root.destroy()
    Bi=Button(root,text="Insert",command=regis).grid(row=10,column=1)
    root.mainloop()
def ree():
    root=Tk()
    root.title('Check your detials')
    Label(root,text='Enter creature number/ticket number').grid(row=0,column=0)
    qsrch=Entry(root,width=20)
    qsrch.grid(row=0,column=1)
    def dosrch():
        srch=str(qsrch.get())
        def searchacc(file_name, string_to_search):
            line_number = 0
            list_of_results = []
            with open(file_name, 'r') as read_obj:
                for line in read_obj:
                    line_number += 1
                    if string_to_search in line:
                        list_of_results.append((line_number, line.rstrip()))
            numm=list_of_results
            return numm
        def find(numm):  
            lo=str(len(numm))+" Records Found"
            for elem in numm:
                messagebox.showinfo(lo,elem[1])       
        if srch=='':
            messagebox.showerror("Error C09: Empty Field","You can't leave any field empty")
        else:
            numm=searchacc("openbook.txt",srch)
            find(numm)
        root.destroy()
    b1 = Button(root, text='Search', command=dosrch)
    b1.grid(row=1,column=1)
    root.mainloop()

#QBi=Button(root,text="Insert",command=lambda:[searchacc(),find()]
#.grid(row=1,column=1))
def delacc():
    root=Tk()
    root.title('Cancel your booking')
    Label(root,text='Enter creature number/ticket number').grid(row=0,column=0)
    qdel=Entry(root,width=20)
    qdel.grid(row=0,column=1)
    def delall():
        phrase=str(qdel.get())
        
        line_number = 0
        a_file = open("openbook.txt","r+")
        for number, line in enumerate(a_file):
          if phrase in line:
            line_number = number
            break
        a_file = open("openbook.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        del lines[line_number]
        messagebox.showinfo("Deleted Successfully")       
        new_file = open("openbook.txt", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()
        root.destroy()
    b1 = Button(root, text='Search', command=delall)
    b1.grid(row=1,column=1)
    root.mainloop()
B1=Button(rootp,text="Book your Travel",command=createacc,activeforeground="yellow",activebackground="white",font="Ubuntu").pack()
B2=Button(rootp,text="Check Travel Details",command=ree,activeforeground="blue",activebackground="white",font="Ubuntu").pack()
B3=Button(rootp,text="Cancel your Travel",command=delacc,activeforeground="red",activebackground="white",font="Ubuntu").pack()
B4=Button(rootp,text="Close Application",command=rootp.destroy,activeforeground="white",activebackground="red",font="Ubuntu").pack()
rootp.mainloop()

