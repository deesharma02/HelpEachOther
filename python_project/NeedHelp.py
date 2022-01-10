from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
from logging import exception
import mysql.connector

class First:
    def __init__(self,root):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="Deesharma078",database="practice")
        print(self.mydb.connection_id)
        self.root=root;
        self.root.state("zoomed")
        self.root.title("Help Each Other's")
        self.root.iconbitmap("icon.ico")

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

        Label(self.root,text="HELP EACH OTHER",fg="gold",background="black",font=("Constantia",30 ,"bold")).place(x=0,y=150,width=1366,height=50)

        lf1=LabelFrame(self.root,text="Personal Information",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
        lf1.place(x=10,y=215,width=750,height=440)

        fname=Label(lf1,text="First Name:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        fname.grid(row=0,column=0,sticky=W,pady=10,padx=10)
        self.fval=StringVar()
        self.fn=Entry(lf1,textvariable=self.fval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.fn.grid(row=0,column=1)

        mname=Label(lf1,text="Middle Name: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        mname.grid(row=1,column=0,sticky=W,pady=10,padx=10)
        self.mval=StringVar()
        self.mn=Entry(lf1,textvariable=self.mval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.mn.grid(row=1,column=1)

        lname=Label(lf1,text="Last Name:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        lname.grid(row=2,column=0,sticky=W,pady=10,padx=10)
        self.lval=StringVar()
        self.ln=Entry(lf1,textvariable=self.lval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.ln.grid(row=2,column=1)

        mob=Label(lf1,text="Mobile No:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        mob.grid(row=3,column=0,sticky=W,pady=10,padx=10)
        self.mobval=StringVar()
        self.moval=Entry(lf1,textvariable=self.mobval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.moval.grid(row=3,column=1,columnspan=2,sticky=W)

        add=Label(lf1,text="Address:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        add.grid(row=4,column=0,sticky=W,pady=10,padx=10)
        self.addval=StringVar()
        self.aval=Entry(lf1,textvariable=self.addval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.aval.grid(row=4,column=1,columnspan=2,sticky=W)

        city=Label(lf1,text="City:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        city.grid(row=5,column=0,sticky=W,pady=10,padx=10)
        self.cityval=StringVar()
        self.cval=Entry(lf1,textvariable=self.cityval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.cval.grid(row=5,column=1,columnspan=2,sticky=W)

        state=Label(lf1,text="State:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        state.grid(row=6,column=0,sticky=W,pady=10,padx=10)
        self.stateval=StringVar()
        self.stval=Entry(lf1,textvariable=self.stateval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.stval.grid(row=6,column=1,columnspan=2,sticky=W)

        pin=Label(lf1,text="Pincode: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        pin.grid(row=0,column=3,sticky=W,pady=10,padx=10)
        self.pinval=StringVar()
        self.pnval=Entry(lf1,textvariable=self.pinval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.pnval.grid(row=0,column=4,columnspan=2,sticky=W)

        adhar=Label(lf1,text="Adhaar Card No:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        adhar.grid(row=1,column=3,sticky=W,pady=10,padx=10)
        self.adharval=StringVar()
        self.adhval=Entry(lf1,textvariable=self.adharval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"),show="*")
        self.adhval.grid(row=1,column=4,sticky=W,columnspan=2)
        
        dob=Label(lf1,text="Date Of Birth: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        dob.grid(row=3,column=3,sticky=W,pady=10,padx=10)
        self.dobval=StringVar()
        self.dbval=Entry(lf1,textvariable=self.dobval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.dbval.grid(row=3,column=4,sticky=W,columnspan=2)


        gender=Label(lf1,text="Gender: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        gender.grid(row=2,column=3,sticky=W,pady=10,padx=10)
        self.genderval=StringVar()
        self.genval=ttk.Combobox(lf1,values=('Male','Female','Other'),textvariable=self.genderval,width=18,height=50,font=("Arial",12,"bold"),state="readonly",foreground="brown",cursor="arrow")
        self.genval.grid(row=2,column=4,pady=5)
        self.genval.current()

        lf2=LabelFrame(self.root,text="Your Problem",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
        lf2.place(x=770,y=215,width=585,height=300)
        # pblval=StringVar()
        self.pbl=Text(lf2,bd=4,height=9,width=50,wrap=WORD,relief=GROOVE,font=("Arial",13,"bold"))
        self.pbl.place(x=50,y=30)


        lf3=Label(self.root,text="Designed And Developed by DEEPAK SHARMA © 2021 All Rights Reserved",font=("Comic Sans MS",18,"bold"),fg="gold",background="black")
        lf3.place(x=0,y=660,width=1366,height=40)

        lf4=Frame(self.root)
        lf4.place(x=770,y=520,width=580,height=130)

        Button(lf4,text="Submit Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4,command=self.database).place(x=120,y=40,width=140,height=40)

        Button(lf4,text="Reset Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4,command=self.reset).place(x=340,y=40,width=140,height=40)

    def database(self):
        prob=self.pbl.get(1.0,"end-1c")
        if self.fval.get()=="" or self.lval.get()=="" or self.mobval.get()=="" or self.addval.get()=="" or self.stateval.get()=="" or self.cityval.get()=="" or self.adharval.get()=="" or prob=="":
            messagebox.showerror("Error","Please Fill All The * Marked Field",parent=self.root)
        else:
            try:
                cur1=self.mydb.cursor()
                cur1.execute("insert into user_registeration (firstname, middlename, lastname, mobileno, address, city, state, pincode, aadharcard, gender,dob,problem) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.fval.get(),self.mval.get(),self.lval.get(),self.mobval.get(),self.addval.get(),self.cityval.get(),self.stateval.get(),self.pinval.get(),self.adharval.get(),self.genderval.get(),self.dobval.get(),prob))
                self.mydb.commit()
                messagebox.showinfo("Success","User Registered Successfully ",parent=self.root)

                self.mydb.close()
            except exception as e:
                messagebox.showerror("Error","Failed To Store Entry In Database",parent=self.root)

    def reset(self):
        self.fn.delete(0,'end')
        self.mn.delete(0,'end')
        self.ln.delete(0,'end')
        self.moval.delete(0,'end')
        self.aval.delete(0,'end')
        self.cval.delete(0,'end')
        self.stval.delete(0,'end')
        self.pnval.delete(0,'end')
        self.adhval.delete(0,'end')
        self.genval.set('')
        self.dbval.delete(0,'end')
        self.pbl.delete(1.0,'end')

if __name__=="__main__":
    root=Tk()
    obj=First(root)
    root.mainloop()