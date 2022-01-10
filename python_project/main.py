from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.geometry("1366x700") #width x height
root.resizable(width=None,height=None)
root.title("Help Each Other's")
root.iconbitmap("icon.ico")


img1=Image.open("images/first.jpg")
img1=img1.resize((455,150),Image.ANTIALIAS)
self.pict1=ImageTk.PhotoImage(img1)

Label(root,image=self.pict1).place(x=0,y=0,width=455,height=150)

img2=Image.open("images/middle.jpg")
img2=img2.resize((455,150),Image.ANTIALIAS)
self.pict2=ImageTk.PhotoImage(img2)

Label(root,image=self.pict2).place(x=455,y=0,width=455,height=150)

img3=Image.open("images/last.jpg")
img3=img3.resize((455,150),Image.ANTIALIAS)
self.pict3=ImageTk.PhotoImage(img3)

Label(root,image=self.pict3).place(x=910,y=0,width=455,height=150)

Label(root,text="HELP EACH OTHER",fg="white",background="black",font=("Constantia",30 ,"bold")).place(x=0,y=150,width=1366,height=50)

# mymenu=Menu(root)
# mymenu.add_command(label="Home")
# mymenu.add_command(label="Registered")
# mymenu.add_command(label="About")

# root.config(menu=mymenu)

# creating application form label frame

lf1=LabelFrame(root,text="Personal Information",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
lf1.place(x=10,y=215,width=750,height=440)


# creating entry widgets

fname=Label(lf1,text="First Name: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
fname.grid(row=0,column=0,sticky=W,pady=10,padx=10)
fval=StringVar()
fn=Entry(lf1,textvariable=fval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
fn.grid(row=0,column=1)

mname=Label(lf1,text="Middle Name: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
mname.grid(row=1,column=0,sticky=W,pady=10,padx=10)
mval=StringVar()
mn=Entry(lf1,textvariable=mval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
mn.grid(row=1,column=1)

lname=Label(lf1,text="Last Name: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
lname.grid(row=2,column=0,sticky=W,pady=10,padx=10)
lval=StringVar()
ln=Entry(lf1,textvariable=lval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
ln.grid(row=2,column=1)

mob=Label(lf1,text="Mobile No: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
mob.grid(row=3,column=0,sticky=W,pady=10,padx=10)
mobval=StringVar()
mval=Entry(lf1,textvariable=mobval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
mval.grid(row=3,column=1,columnspan=2,sticky=W)

add=Label(lf1,text="Address: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
add.grid(row=4,column=0,sticky=W,pady=10,padx=10)
addval=StringVar()
aval=Entry(lf1,textvariable=addval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
aval.grid(row=4,column=1,columnspan=2,sticky=W)

city=Label(lf1,text="City: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
city.grid(row=5,column=0,sticky=W,pady=10,padx=10)
cityval=StringVar()
cval=Entry(lf1,textvariable=cityval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
cval.grid(row=5,column=1,columnspan=2,sticky=W)

state=Label(lf1,text="State: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
state.grid(row=6,column=0,sticky=W,pady=10,padx=10)
stateval=StringVar()
stval=Entry(lf1,textvariable=stateval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
stval.grid(row=6,column=1,columnspan=2,sticky=W)

pin=Label(lf1,text="Pincode: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
pin.grid(row=0,column=3,sticky=W,pady=10,padx=10)
pinval=StringVar()
pnval=Entry(lf1,textvariable=pinval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"))
pnval.grid(row=0,column=4,columnspan=2,sticky=W)

adhar=Label(lf1,text="Adhaar Card No: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
adhar.grid(row=1,column=3,sticky=W,pady=10,padx=10)
adharval=StringVar()
adhval=Entry(lf1,textvariable=adharval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"),show="*")
adhval.grid(row=1,column=4,sticky=W,columnspan=2)

# gender=Label(lf1,text="Gender: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
# gender.grid(row=2,column=3,sticky=W,pady=10,padx=10)
# genderval=StringVar()
# genval=Entry(lf1,textvariable=genderval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"),show="*")
# genval.grid(row=2,column=4,sticky=W,columnspan=2)
# genderval=StringVar()
# gframe=Frame(lf1,bd=2,relief=SUNKEN,width=200,height=30).place(x=500,y=56)
# genval=Checkbutton(gframe,text="Male",command=gen,variable=genderval,bg="white",fg="red")
# genval.grid(row=1,column=2,sticky=W)

dob=Label(lf1,text="Date Of Birth: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
dob.grid(row=3,column=3,sticky=W,pady=10,padx=10)
dobval=StringVar()
dbval=Entry(lf1,textvariable=dobval,relief=GROOVE,width=20,bd=3,font=("Constantia",12,"bold"),show="*")
dbval.grid(row=3,column=4,sticky=W,columnspan=2)


dob=Label(lf1,text="Gender: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
dob.grid(row=2,column=3,sticky=W,pady=10,padx=10)
gen=StringVar()
genv=ttk.Combobox(lf1,values=('Male','Female','Other'),textvariable=gen,width=18,height=50,font=("Constantia",12,"bold"),state="readonly",foreground="brown",cursor="arrow")
genv.grid(row=2,column=4,pady=5)
genv.current()
# pbl=Frame(lf1,bd=2,relief=GROOVE).place(x=750,y=17,width=350,height=350)
# pb=Label(pbl,text="Enter The Problem: ",fg="black",font=("Times New Roman",15,"bold"),bg="skyblue")
# dob.grid(row=0,column=5,sticky=W,pady=10,padx=10)
# pbl=Text(pbl,bd=2,width=50,height=10).grid(row=0,column=6)
# pbl=Frame(lf1,bd=2,relief=GROOVE).place(x=750,y=17,width=350,height=350)

lf2=LabelFrame(root,text="Your Problem",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
lf2.place(x=770,y=215,width=585,height=300)
# pblval=StringVar()
pbl=Text(lf2,bd=4,height=8,width=47,wrap=WORD,relief=GROOVE,font=("Times New Roman",15)).place(x=50,y=30)


lf3=Label(root,text="Designed And Developed by DEEPAK SHARMA © 2021 All Rights Reserved",font=("Comic Sans MS",18,"bold"),fg="white",background="black")
lf3.place(x=0,y=660,width=1366,height=40)

lf4=Frame(root)
lf4.place(x=770,y=520,width=580,height=130)

b1=Button(lf4,text="Submit Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4).place(x=120,y=40,width=140,height=40)

b2=Button(lf4,text="Reset Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4).place(x=340,y=40,width=140,height=40)


if __name__=="__main__":
    root=Tk()

    root.mainloop()