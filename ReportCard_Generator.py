#ALL THE MODULES
import ctypes
import mysql.connector as ms
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

#MESSAGE BOX
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0,text,title,style)


#ESTABLISHING CONN. WITH THE DB AND CREATING DATABASE AND TABLE IF NOT EXIST
mydb=ms.connect(host='localhost',user='root',passwd='12345')
mc=mydb.cursor()
mc.execute('CREATE DATABASE IF NOT EXISTS RCS')
mc.execute('USE RCS')
mc.execute("CREATE TABLE IF NOT EXISTS STDETAILS(GRNO VARCHAR(7) PRIMARY KEY, FullName VARCHAR(30), Password VARCHAR(30), Class VARCHAR(2), Division VARCHAR(1), English INT, Maths INT, CS INT, Physics INT, Chemistry INT)")
Mbox('Attention Users! ','Database Connection Successful!',0)


#START-UP PAGE
def mainscreen():
    global screen
    screen=Tk()
    screen.geometry("1000x667")
    screen.title("Report Card Software Generator")
    
    screen.bg=ImageTk.PhotoImage(file='bg.png')
    bg=Label(screen,image=screen.bg).place(x=0,y=0,relwidth=1,relheight=1)
    
    frame1=Frame(screen,bg="gray2")
    frame1.place(x=0,y=55,width=500,height=550)
    
    RN=Label(frame1,text="Register Now!", font=('Calibri',20,'bold'),bg="white",fg='black')
    RN.place(x=155,y=10)
    
    global Namee
    Name=Label(frame1,text="Full Name:", font=('Calibri',15,'bold'),fg="white",bg='black')
    Name.place(x=10,y=90)
    Namee=Entry(frame1,font=('Calibri',15,'normal'),fg="white",bg='black')
    Namee.place(x=200,y=95)

    global Gre
    Gr=Label(frame1,text="G.R No:", font=('Calibri',15,'bold'),fg="white",bg='black')
    Gr.place(x=10,y=150)
    Gre=Entry(frame1,font=('Calibri',15,'normal'),fg="white",bg='black')
    Gre.place(x=200,y=155)

    global Classe
    Class=Label(frame1,text="Class:", font=('Calibri',15,'bold'),fg="white",bg='black')
    Class.place(x=10,y=210)
    Classe=Entry(frame1,font=('Calibri',15,'normal'),fg="white",bg='black')
    Classe.place(x=200,y=215)

    global Dive
    Div=Label(frame1,text="Division:", font=('Calibri',15,'bold'),fg="white",bg='black')
    Div.place(x=10,y=270)
    Dive=Entry(frame1,font=('Calibri',15,'normal'),fg="white",bg='black')
    Dive.place(x=200,y=275)

    global Pe
    P=Label(frame1,text="Password:", font=('Calibri',15,'bold'),fg="white",bg='black')
    P.place(x=10,y=330)
    Pe=Entry(frame1,font=('Calibri',15,'normal'),fg="white",bg='black')
    Pe.place(x=200,y=335)
    global CPe
    CP=Label(frame1,text="Confirm Password:", font=('Calibri',15,'bold'),fg="white",bg='black')
    CP.place(x=10,y=390)
    CPe=Entry(frame1,font=('Calibri',15,'normal'),fg="white",bg='black')
    CPe.place(x=200,y=395)
    
    screen.button=ImageTk.PhotoImage(file='reg.png')
    btn=Button(frame1,image=screen.button,bd=0,bg='gray2',command=register)
    btn.place(x=275,y=500)
    
    h=Label(text="Already a User?",font=('Calibri',30,'bold'),bg='gray2',fg='white')
    h.place(x=575,y=200)

    aa=Label(text="ReportCard Software - Your friendly Result Viewer", font=('Calibri',25,'bold'),bg="blue",fg='white')
    aa.place(x=90,y=1)
    
    screen.button2=ImageTk.PhotoImage(file='signin.png')
    btn2=Button(image=screen.button2,bd=0,bg='blue',command=login)
    btn2.place(x=695,y=400)

    screen.mainloop()


#COMMAND-REGISTER
def register():
    if (Namee.get()=='' or Gre.get()=='' or Classe.get()=='' or Dive.get()=='' or Pe.get()=='' or CPe.get()==''):
        messagebox.showerror("Attention!",'All Fields Are Compulsory')
    elif Pe.get()!= CPe.get():
        messagebox.showerror("Attention!","Passwords are not same")
    else:
        n=Namee.get()
        g=Gre.get()
        c=Classe.get()
        d=Dive.get()
        p=Pe.get()
        
        mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
        mc=mydb.cursor()
        mc.execute('INSERT INTO STDETAILS VALUES(%s,%s,%s,%s,%s,NULL,NULL,NULL,NULL,NULL)',(g,n,p,c,d))
        mydb.commit()
        messagebox.showinfo("Attention","Account Registered")

        
#LOGIN PAGE    
def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x800")
    screen2['bg']="black"
    
    screen.button3=ImageTk.PhotoImage(file='back.png')
    btn3=Button(screen2,image=screen.button3,bd=0,bg='black',command=back)
    btn3.place(x=0,y=0)
    
    screen.button4=ImageTk.PhotoImage(file='loginhead.png')
    l=Label(screen2,image=screen.button4,bd=0,bg='black')
    l.place(x=190,y=200)
    
    global Grle
    Grl=Label(screen2,text="Enter GR.No:", font=('Calibri',15,'bold'),fg="white",bg='black')
    Grl.place(x=20,y=400)
    Grle=Entry(screen2,font=('Calibri',15,'normal'),bg='black',fg='white',)
    Grle.place(x=180,y=403)
    
    global Pwle
    Pwl=Label(screen2,text="Enter Password:", font=('Calibri',15,'bold'),fg="white",bg='black')
    Pwl.place(x=20,y=450)
    Pwle=Entry(screen2,font=('Calibri',15,'normal'),bg='black',fg='white',show="*")
    Pwle.place(x=180,y=452)
    
    screen.button5=ImageTk.PhotoImage(file='signin.png')
    btn5=Button(screen2,image=screen.button5,bd=0,command=loginuser)
    btn5.place(x=195,y=600)
    
    screen2.mainloop()

    
#COMMAND-BACK TO LOGIN(1)    
def back():
    screen2.withdraw()

    
#COMMAND-LOGIN
def loginuser():
    global grno
    grno=Grle.get()
    passw=Pwle.get()
    if grno=='' or passw=='':
        messagebox.showerror("Attention!!","All Fields Are Required",parent=screen2)
    elif grno=='admin' and passw=='admin':
        messagebox.showinfo("Admin Page","Welcome Admin!")
        adminconsole()
    else:
        mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
        mc=mydb.cursor()
        mc.execute("SELECT GRNO,FULLNAME,Password from STDETAILS WHERE GRNO=%s AND PASSWORD=%s",(grno,passw))
        rec=mc.fetchall()
        count=mc.rowcount
        if count==0:
            messagebox.showinfo("Error","Check Your Credentials/No Account Found",parent=screen2)
        else:
            for i in rec:
                g=i[0]
                n=i[1]
                p=i[2]
            if g==grno and p==passw:
                messagebox.showinfo("Attention","Welcome "+n,parent=screen2)
                studentslogin()
                

#ADMIN PAGE
def adminconsole():

    global be_var
    global ce_var
    global de_var
    global ee_var
    global fe_var
    global ge_var
    global he_var
    global ie_var
    global je_var
    global ke_var
    global search

   
    be_var=StringVar()
    ce_var=StringVar()
    de_var=StringVar()
    ee_var=StringVar()
    fe_var=StringVar()
    ge_var=IntVar()
    he_var=IntVar()
    ie_var=IntVar()
    je_var=IntVar()
    ke_var=IntVar()
    search=StringVar()
    
    
    global screen3
    screen3=Toplevel(screen2)
    screen2.withdraw()
    screen3.title("Admin Console")
    screen3.geometry("1366x768")
    screen3['bg']="black"
    l1=Label(screen3,text="Admin Page",font=("Calibri",30,'bold'),fg="black",bg='white')
    l1.pack(side=TOP)
    f1=Frame(screen3,bd=4,bg='white')
    f1.place(x=20,y=70,width=550,height=650)
    f2=Frame(screen3,bd=4,bg='white')
    f2.place(x=600,y=70,width=750,height=650)
    a=Label(screen3,text="ADD/EDIT",font=("Calibri",20,'bold'),fg='white',bg='black')
    a.place(x=50,y=70)
    b=Label(screen3,text="GR.NO*:",font=("Calibri",15,'normal'),fg='black')
    b.place(x=25,y=150)
    
    global be
    be=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=be_var)
    be.place(x=200,y=150)
    c=Label(screen3,text="Name:",font=("Calibri",15,'normal'),fg='black')
    c.place(x=25,y=200)
    global ce
    ce=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=ce_var)
    ce.place(x=200,y=200)
    d=Label(screen3,text="Password:",font=("Calibri",15,'normal'),fg='black')
    d.place(x=25,y=250)
    global de
    de=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=de_var)
    de.place(x=200,y=250)
    e=Label(screen3,text="Class:",font=("Calibri",15,'normal'),fg='black')
    e.place(x=25,y=300)
    global ee
    ee=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=ee_var)
    ee.place(x=200,y=300)
    f=Label(screen3,text="Div:",font=("Calibri",15,'normal'),fg='black')
    f.place(x=25,y=350)
    global fe
    fe=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=fe_var)
    fe.place(x=200,y=350)
    g=Label(screen3,text="Eng:",font=("Calibri",15,'normal'),fg='black')
    g.place(x=25,y=400)
    global ge
    ge=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=ge_var)
    ge.place(x=200,y=400)
    h=Label(screen3,text="Maths:",font=("Calibri",15,'normal'),fg='black')
    h.place(x=25,y=450)
    global he
    he=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=he_var)
    he.place(x=200,y=450)
    i=Label(screen3,text="C.S:",font=("Calibri",15,'normal'),fg='black')
    i.place(x=25,y=500)
    global ie
    ie=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=ie_var)
    ie.place(x=200,y=500)
    j=Label(screen3,text="Phy:",font=("Calibri",15,'normal'),fg='black')
    j.place(x=25,y=550)
    global je
    je=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=je_var)
    je.place(x=200,y=550)
    k=Label(screen3,text="Chem:",font=("Calibri",15,'normal'),fg='black')
    k.place(x=25,y=600)
    global ke
    ke=Entry(screen3,font=("Calibri",15,'bold'),bd=4,textvariable=ke_var)
    ke.place(x=200,y=600)

    updatebtn=Button(screen3,text="Update",font=("Calibri",20,'bold'),fg='white',bg='black',command=update)
    updatebtn.place(x=50,y=650)
    delbtn=Button(screen3,text="Delete",font=("Calibri",20,'bold'),fg='white',bg='black',command=delete)
    delbtn.place(x=300,y=650)

    global se
    global tse
    a1=Label(screen3,text="Search By the Option:",font=("Calibri",15,'normal'),fg='black')
    a1.place(x=600,y=70)
    se=ttk.Combobox(screen3,width=10,font=("Calibri",15,'normal'))
    se['values']=("GRNO",)
    se.place(x=820,y=70)
    tse=Entry(screen3,bd=4,textvariable=search,width=12,font=("Calibri",15,'normal'),fg='black')
    tse.place(x=1000,y=70)
    searchbtn=Button(screen3,text="Search",font=("Calibri",10,'normal'),fg='white',bg='black',command=searchh)
    searchbtn.place(x=1200,y=70)
    shallbtn=Button(screen3,text="ShowAll",font=("Calibri",10,'normal'),fg='white',bg='black',command=getdata)
    shallbtn.place(x=1300,y=70)

    bk=Button(screen3,text='LogOut',font=("Calibri",15,'normal'),fg='black',bg='white',command=backtologin)
    bk.place(x=1200,y=20)

    tabframe=Frame(screen3,bd=3)
    tabframe.place(x=620,y=120,width=700,height=500)
    scrollx=Scrollbar(tabframe,orient=HORIZONTAL)
    scrollx.pack(side=BOTTOM,fill=X)
    global sttable
    sttable=ttk.Treeview(tabframe,columns=("GRNO","FullName","P.W","Class","Div","Eng","Math","C.S","Phy","Chem"),xscrollcommand=scrollx.set)
    scrollx.config(command=sttable.xview)
    sttable.heading("GRNO",text='GRNO')
    sttable.heading("FullName",text='FullName')
    sttable.heading("P.W",text='P.W')
    sttable.heading("Class",text='Class')
    sttable.heading("Div",text='Div')
    sttable.heading("Eng",text='Eng')
    sttable.heading("Math",text='Math')
    sttable.heading("C.S",text='C.S')
    sttable.heading("Phy",text='Phy')
    sttable.heading("Chem",text='Chem')
    sttable['show']='headings'
    sttable.pack(fill=BOTH,expand=1)
    sttable.bind("<ButtonRelease-1>",gettofield)
    
    getdata()

    
#COMMAND-DISPLAYING DATA IN TABLE
def getdata():
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute("SELECT * FROM STDETAILS")
    rows=mc.fetchall()
    if len(rows)>=0:
        sttable.delete(*sttable.get_children())
        for row in rows:
            sttable.insert("",END,values=row)
        

#COMMAND-DISPLAYING DATA IN THE FIELDS
def gettofield(ev):
    r=sttable.focus()
    i=sttable.item(r)
    row=i["values"]
    global be_var
    be_var.set(row[0])
    ce_var.set(row[1])
    de_var.set(row[2])
    ee_var.set(row[3])
    fe_var.set(row[4])
    ge_var.set(row[5])
    he_var.set(row[6])
    ie_var.set(row[7])
    je_var.set(row[8])
    ke_var.set(row[9])
    
    
#COMMAND-UPDATE
def update():
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute('UPDATE STDETAILS SET FullNAME=%s,Password=%s,Class=%s,Division=%s,English=%s,Maths=%s,CS=%s,Physics=%s,Chemistry=%s WHERE GRNO=%s',(ce_var.get(),de_var.get(),ee_var.get(),fe_var.get(),ge_var.get(),he_var.get(),ie_var.get(),je_var.get(),ke_var.get(),be_var.get()))
    mydb.commit()
    getdata()
    
    
#COMMAND-DELETE
def delete():
    a=be_var.get()
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute('DELETE FROM STDETAILS WHERE GRNO = %s',(a,))
    mydb.commit()
    getdata()
    

#COMMAND-SEARCH
def searchh():
    a=search.get()
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute('SELECT * FROM STDETAILS WHERE GRNO=%s',(a,))
    rows=mc.fetchall()
    if len(rows)>0:
        sttable.delete(*sttable.get_children())
        for row in rows:
            sttable.insert("",END,values=row)

            
#COMMAND-BACK TO LOGIN SCREEN(2)       
def backtologin():
    screen3.withdraw()


#STUDENTS PAGE
def studentslogin():
    global screen4
    screen4=Toplevel(screen2)
    screen2.withdraw()
    screen4.title("Student's Login")
    screen4.geometry('1000x500')
    screen4['bg']='black'
    tabframe=Frame(screen4,bd=3)
    tabframe.place(x=0,y=0,width=1000,height=100)
    scrollx=Scrollbar(tabframe,orient=HORIZONTAL)
    scrollx.pack(side=BOTTOM,fill=X)
    global sttable2
    sttable2=ttk.Treeview(tabframe,columns=("GRNO","FullName","Class","Div","Eng","Math","C.S","Phy","Chem"),xscrollcommand=scrollx.set)
    scrollx.config(command=sttable2.xview)
    sttable2.heading("GRNO",text='GRNO')
    sttable2.heading("FullName",text='FullName')
    sttable2.heading("Class",text='Class')
    sttable2.heading("Div",text='Div')
    sttable2.heading("Eng",text='Eng')
    sttable2.heading("Math",text='Math')
    sttable2.heading("C.S",text='C.S')
    sttable2.heading("Phy",text='Phy')
    sttable2.heading("Chem",text='Chem')
    sttable2['show']='headings'
    sttable2.column("GRNO",width=30)
    sttable2.column("FullName",width=100)
    sttable2.column("Class",width=30)
    sttable2.column("Div",width=30)
    sttable2.column("Eng",width=30)
    sttable2.column("Math",width=30)
    sttable2.column("C.S",width=30)
    sttable2.column("Phy",width=30)
    sttable2.column("Chem",width=30)
    sttable2.pack(fill=BOTH,expand=1)

    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute("SELECT GRNO,FullName,Class,Division,English,Maths,CS,Physics,Chemistry FROM STDETAILS WHERE GRNO=%s",(grno,))
    rows=mc.fetchall()
    if len(rows)>0:
        sttable2.delete(*sttable2.get_children())
        for row in rows:
            sttable2.insert("",END,values=row)

    t=Button(screen4,text="Total",font=("Calibri",25,'normal'),fg='white',bg='blue',command=total)
    t.place(x=200,y=200)
    r=Button(screen4,text="Rank",font=("Calibri",25,'normal'),fg='white',bg='blue',command=rank)
    r.place(x=400,y=200)
    a=Button(screen4,text="Average",font=("Calibri",25,'normal'),fg='white',bg='blue',command=average)
    a.place(x=600,y=200)
    bk=Button(screen4,text='LogOut',font=("Calibri",15,'normal'),fg='black',bg='white',command=backtologin2)
    bk.place(x=800,y=400)

    
#COMMAND-TOTAL
def total():
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute("SELECT(English+Maths+CS+Physics+Chemistry)AS TOTALSUM FROM STDETAILS WHERE GRNO=%s",(grno,))
    r=mc.fetchall()
    for i in r:
        messagebox.showinfo("Total","Your Total is "+str(i[0]))

        
#COMMAND-AVERAGE
def average():
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    mc.execute("SELECT(English+Maths+CS+Physics+Chemistry)AS TOTALSUM FROM STDETAILS WHERE GRNO=%s",(grno,))
    r=mc.fetchall()
    for i in r:
        a=(i[0])
        a=str(a/5)
        messagebox.showinfo("Average","Your Average is "+a)


#COMMAND-RANK
def rank():
    mydb=ms.connect(host='localhost',user='root',passwd='12345',database='RCS')
    mc=mydb.cursor()
    try:
        mc.execute("ALTER TABLE STDETAILS DROP COLUMN TOTAL")
    except:
        pass
    mc.execute("ALTER TABLE STDETAILS ADD TOTAL INT")
    mc.execute("UPDATE STDETAILS SET TOTAL=(English+Maths+CS+Physics+Chemistry)")
    mc.execute("SELECT FIND_IN_SET( TOTAL,(SELECT GROUP_CONCAT(TOTAL ORDER BY TOTAL DESC)FROM STDETAILS))AS RANK FROM STDETAILS WHERE GRNO=%s",(grno,))
    r=mc.fetchall()
    for i in r:
        messagebox.showinfo("Rank","Your Rank in Class is "+str(i[0]))
        mc.execute("ALTER TABLE STDETAILS DROP COLUMN TOTAL")


#COMMAND-BACK TO LOGIN SCREEN(3)
def backtologin2():
    screen4.withdraw()


#CALLING THE PARENT SCREEN
mainscreen()


    
