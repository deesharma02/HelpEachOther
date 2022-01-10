from logging import exception
from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import mysql.connector
from getpass import getpass

mydb=mysql.connector.connect(host="localhost",user="root",password="Deesharma078",database="practice")
print(mydb.connection_id)

root=Tk()
root.geometry("1366x700") #width x height
root.resizable(width=None,height=None)
root.title("Help Each Other's")
root.iconbitmap("icon.ico")

img1=Image.open("images/first.jpg")
img1=img1.resize((455,150),Image.ANTIALIAS)
pict1=ImageTk.PhotoImage(img1)
Label(root,image=pict1).place(x=0,y=0,width=455,height=150)

img2=Image.open("images/middle.jpg")
img2=img2.resize((455,150),Image.ANTIALIAS)
pict2=ImageTk.PhotoImage(img2)
Label(root,image=pict2).place(x=455,y=0,width=455,height=150)

img3=Image.open("images/last.jpg")
img3=img3.resize((455,150),Image.ANTIALIAS)
pict3=ImageTk.PhotoImage(img3)
Label(root,image=pict3).place(x=910,y=0,width=455,height=150)

Label(root,text="HELP EACH OTHER",fg="white",background="black",font=("Constantia",30 ,"bold")).place(x=0,y=150,width=1366,height=50)

# creating application form label frame

lf1=LabelFrame(root,text="Personal Information",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
lf1.place(x=10,y=215,width=750,height=440)

# creating entry widgets

fname=Label(lf1,text="First Name:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
fname.grid(row=0,column=0,sticky=W,pady=10,padx=10)
fval=StringVar()
fn=Entry(lf1,textvariable=fval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
fn.grid(row=0,column=1)

mname=Label(lf1,text="Middle Name: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
mname.grid(row=1,column=0,sticky=W,pady=10,padx=10)
mval=StringVar()
mn=Entry(lf1,textvariable=mval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
mn.grid(row=1,column=1)

lname=Label(lf1,text="Last Name:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
lname.grid(row=2,column=0,sticky=W,pady=10,padx=10)
lval=StringVar()
ln=Entry(lf1,textvariable=lval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
ln.grid(row=2,column=1)

mob=Label(lf1,text="Mobile No:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
mob.grid(row=3,column=0,sticky=W,pady=10,padx=10)
mobval=StringVar()
moval=Entry(lf1,textvariable=mobval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
moval.grid(row=3,column=1,columnspan=2,sticky=W)

add=Label(lf1,text="Address:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
add.grid(row=4,column=0,sticky=W,pady=10,padx=10)
addval=StringVar()
aval=Entry(lf1,textvariable=addval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
aval.grid(row=4,column=1,columnspan=2,sticky=W)

city=Label(lf1,text="City:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
city.grid(row=5,column=0,sticky=W,pady=10,padx=10)
cityval=StringVar()
cval=Entry(lf1,textvariable=cityval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
cval.grid(row=5,column=1,columnspan=2,sticky=W)

state=Label(lf1,text="State:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
state.grid(row=6,column=0,sticky=W,pady=10,padx=10)
stateval=StringVar()
stval=Entry(lf1,textvariable=stateval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
stval.grid(row=6,column=1,columnspan=2,sticky=W)

pin=Label(lf1,text="Pincode: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
pin.grid(row=0,column=3,sticky=W,pady=10,padx=10)
pinval=StringVar()
pnval=Entry(lf1,textvariable=pinval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
pnval.grid(row=0,column=4,columnspan=2,sticky=W)

adhar=Label(lf1,text="Adhaar Card No:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
adhar.grid(row=1,column=3,sticky=W,pady=10,padx=10)
adharval=StringVar()
adhval=Entry(lf1,textvariable=adharval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"),show="*")
adhval.grid(row=1,column=4,sticky=W,columnspan=2)

# gender=Label(lf1,text="Gender: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
# gender.grid(row=2,column=3,sticky=W,pady=10,padx=10)
# genderval=StringVar()
# genval=Entry(lf1,textvariable=genderval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
# genval.grid(row=2,column=4,sticky=W,columnspan=2)
gender=Label(lf1,text="Gender: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
gender.grid(row=2,column=3,sticky=W,pady=10,padx=10)
genderval=StringVar()
genval=ttk.Combobox(lf1,values=('Male','Female','Other'),textvariable=genderval,width=18,height=50,font=("Constantia",12,"bold"),state="readonly",foreground="brown")
genval.grid(row=2,column=4,pady=5)
genval.current()

dob=Label(lf1,text="Date Of Birth: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
dob.grid(row=3,column=3,sticky=W,pady=10,padx=10)
dobval=StringVar()
dbval=Entry(lf1,textvariable=dobval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
dbval.grid(row=3,column=4,sticky=W,columnspan=2)

lf2=LabelFrame(root,text="Your Problem Here",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
lf2.place(x=770,y=215,width=585,height=300)
pbl=Text(lf2,bd=4,height=9,width=51,wrap=WORD,relief=GROOVE,font=("Arial",13,"bold"))
pbl.place(x=50,y=30)

lf3=Label(root,text="Designed And Developed by DEEPAK SHARMA © 2021 All Rights Reserved",font=("Comic Sans MS",18,"bold"),fg="white",background="black")
lf3.place(x=0,y=660,width=1366,height=40)

lf4=Frame(root)
lf4.place(x=770,y=520,width=580,height=130)

def dbase():
    # if mval.get()!="":
    prob=pbl.get(1.0,"end-1c")
    if fval.get()=="" or lval.get()=="" or mobval.get()=="" or addval.get()=="" or addval.get()=="" or stateval.get()=="" or cityval.get()=="" or adharval.get()=="" or prob=="":
        messagebox.showerror("Error","Please Fill All The * Marked Field",parent=root)
    else:
        try:
            cur=mydb.cursor()
            cur.execute("insert into user_registeration (firstname, middlename, lastname, mobileno, address, city, state, pincode, aadharcard, gender,dob,problem) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fval.get(),mval.get(),lval.get(),mobval.get(),addval.get(),cityval.get(),stateval.get(),pinval.get(),adharval.get(),genderval.get(),dobval.get(),prob))
            mydb.commit()
            messagebox.showinfo("Success","User Registered Successfully ")

            mydb.close()
        except exception as e:
            messagebox.showerror("Error","Failed To Store Entry In Database",parent=root)
   
b1=Button(lf4,text="Submit Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4,command=dbase).place(x=120,y=40,width=140,height=40)

def reset():
    fn.delete(0,'end')
    mn.delete(0,'end')
    ln.delete(0,'end')
    moval.delete(0,'end')
    aval.delete(0,'end')
    cval.delete(0,'end')
    stval.delete(0,'end')
    pnval.delete(0,'end')
    adhval.delete(0,'end')
    # ttk.Combobox.index()
    genval.set('')
    
    dbval.delete(0,'end')
    pbl.delete(1.0,'end')

b2=Button(lf4,text="Reset Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4,command=reset).place(x=340,y=40,width=140,height=40)

root.mainloop()