from tkinter import *
from tkinter import ttk
from typing import Counter
from PIL import Image,ImageTk
from tkinter import messagebox
from logging import exception
import mysql.connector

class Second:
    def __init__(self,root):
        self.root=root;
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="Deesharma078",database="practice")
        print(self.mydb.connection_id)
        self.root.state("zoomed")
        self.root.title("Help Each Other's")
        self.root.iconbitmap("icon.ico")

        img1=Image.open("images/first.jpg")
        img1=img1.resize((455,150),Image.ANTIALIAS)
        self.pict1=ImageTk.PhotoImage(img1)
        Label(root,image=self.pict1).place(x=0,y=0,width=455,height=150)

        img2=Image.open("images/thank3.jpg")
        img2=img2.resize((455,150),Image.ANTIALIAS)
        self.pict2=ImageTk.PhotoImage(img2)
        Label(root,image=self.pict2).place(x=455,y=0,width=455,height=150)

        img3=Image.open("images/thanks2.png")
        img3=img3.resize((455,150),Image.ANTIALIAS)
        self.pict3=ImageTk.PhotoImage(img3)
        Label(root,image=self.pict3).place(x=910,y=0,width=455,height=150)

        Label(self.root,text="HELP EACH OTHER",fg="gold",background="black",font=("Constantia",30 ,"bold")).place(x=0,y=150,width=1366,height=50)

        lf1=LabelFrame(self.root,text="Personal Information",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="red",background="skyblue")
        lf1.place(x=10,y=215,width=650,height=440)

        yname=Label(lf1,text="Name:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        yname.grid(row=0,column=0,sticky=W,pady=10,padx=10)
        self.yval=StringVar()
        self.yn=Entry(lf1,textvariable=self.yval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.yn.grid(row=0,column=1)

        mob=Label(lf1,text="Mobile No:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        mob.grid(row=1,column=0,sticky=W,pady=10,padx=10)
        self.mobval=StringVar()
        self.mval=Entry(lf1,textvariable=self.mobval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"))
        self.mval.grid(row=1,column=1,columnspan=2,sticky=W)

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

        adhar=Label(lf1,text="Adhaar Card No:* ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        adhar.grid(row=7,column=0,sticky=W,pady=10,padx=10)
        self.adharval=StringVar()
        self.adhval=Entry(lf1,textvariable=self.adharval,relief=GROOVE,width=20,bd=3,font=("Arial",12,"bold"),show="*")
        self.adhval.grid(row=7,column=1,sticky=W,columnspan=2)

        gender=Label(lf1,text="Gender: ",fg="brown",font=("Times New Roman",15,"bold"),bg="skyblue")
        gender.grid(row=8,column=0,sticky=W,pady=10,padx=10)
        self.genderval=StringVar()
        self.genval=ttk.Combobox(lf1,values=('Male','Female','Other'),textvariable=self.genderval,width=18,height=50,font=("Arial",12,"bold"),state="readonly",foreground="brown",cursor="arrow")
        self.genval.grid(row=8,column=1,pady=5)
        self.genval.current()

        lf3=Label(self.root,text="Designed And Developed by DEEPAK SHARMA © 2021 All Rights Reserved",font=("Comic Sans MS",18,"bold"),fg="gold",background="black")
        lf3.place(x=0,y=660,width=1366,height=40)

        Button(lf1,text="Submit Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4,command=self.helperdbase).place(x=420,y=120,width=140,height=40)

        Button(lf1,text="Reset Form",bg="lime",fg="black",font=("Times New Roman",14,"bold"),relief=RAISED,bd=4,command=self.reset).place(x=420,y=210,width=140,height=40)

    def helperdbase(self):
        if self.yval.get()=="" or self.mobval.get()=="" or self.addval.get()=="" or self.stateval.get()=="" or self.cityval.get()=="" or self.adharval.get()=="" :
            messagebox.showerror("Error","Please Fill All The * Marked Field",parent=self.root)
        else:
            try:
                cur=self.mydb.cursor()
                cur.execute("insert into helper_registration (name, mobile_no, address, city, state, aadharno,gender) values (%s,%s,%s,%s,%s,%s,%s)",(self.yval.get(),self.mobval.get(),self.addval.get(),self.cityval.get(),self.stateval.get(),self.adharval.get(),self.genderval.get()))
                self.mydb.commit()
                messagebox.showinfo("Success","Thanks for registering ",parent=self.root)

                cur.execute("SELECT * FROM user_registeration")
                user=cur.fetchall()

                lf4=Frame(self.root,bd=4,relief=RIDGE,background="grey")
                Label(lf4,text="List Of People Who Need Help",font=("Constantia",25 ,"bold"),fg="white",bg="blue").pack(pady=20,fill=X)
                lf4.place(x=700,y=215,width=650,height=350)
                
                tree=ttk.Treeview(lf4)
                tree['column']=('Name','Mobile-no','Address','Problem')
                tree.column("#0",width=0,stretch=NO)
                tree.column("Name",width=140,minwidth=125)
                tree.column("Mobile-no",width=140,minwidth=125)
                tree.column("Address",width=130,minwidth=125)
                tree.column("Problem",width=140,minwidth=125)
                tree.heading("Name",text="Name",anchor=CENTER)
                tree.heading("Mobile-no",text="Mobile-no",anchor=CENTER)
                tree.heading("Address",text="Address",anchor=CENTER)
                tree.heading("Problem",text="Problem",anchor=CENTER)

                count=0
                for record in user:
                    tree.insert(parent='',index='end',iid=count,values=(record[0]+" "+record[2],record[3],record[4],record[11]))
                    count=count+1
                tree.pack(pady=22,ipady=10,ipadx=5)

                self.mydb.close()
            except exception as e:
                messagebox.showerror("Error","Failed To Store Entry In Database",parent=self.root)

    def reset(self):
        self.yn.delete(0,'end')
        self.mval.delete(0,'end')
        self.aval.delete(0,'end')
        self.cval.delete(0,'end')
        self.stval.delete(0,'end')
        self.adhval.delete(0,'end')
        self.genval.set('')    


if __name__=="__main__":
    root=Tk()
    obj=Second(root)
    root.mainloop()