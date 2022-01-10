from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
root=Tk()

root.geometry("1366x700")
# root.maxsize(1200,1200)
# root.minsize(200,200)

# canva=Canvas(root,height=500,width=500)
# canva.pack()
# canva.create_line(15,15,180,180,fill="red")
# canva.create_rectangle(80,80,200,200)
# canva.create_text(210,210,text="Helping hands",fill="red")
# canva.create_image(300,300,image_names="1.jpg")
# img=Image.open("1.jpg")
# pict=ImageTk.PhotoImage(img)
# dee=Label(image=pict)
# dee.pack()
root.title("Helping Hands")

# username=Label(root,text="User name")
# password=Label(root,text="Password")
# username.grid(row=2,column=2)
# password.grid(row=3,column=2)

# userval=StringVar()
# passval=StringVar()

# e1=Entry(root,textvariable=userval)
# e2=Entry(root,textvariable=passval)
# e1.grid(row=2,column=4)
# e2.grid(row=3,column=4)

# def getval():
#     print(userval.get())
#     print(passval.get())
# Button(root,text="Submit",command=getval).grid(row=4,column=4)

# f1=Frame(root,bg="Grey",bd=5,relief=SUNKEN)
# f1.pack(side=LEFT,anchor="nw")

# f2=Frame(root,bg="Grey",bd=5,relief=SUNKEN)
# f2.pack(side=LEFT,anchor="nw")

# b1=Button(f1,text="Submit Your Form")
# b1.pack(side=LEFT,anchor="nw")

# def check():
#     print("Hello")
# b2=Button(f2,text="Submit Your Form",command=check)
# b2.pack(side=LEFT,anchor="nw")
# dee=Label(f1,text="Helping Hands")
# dee.pack(side=LEFT)

# dee=Label(f2,text="Helping Hands")
# dee.pack()

# lb=Listbox(root).pack()
# mbtn["menu"]=menu

def frame2():
    f=Frame(root,bg="green")
    Label(f,text="frame2").grid(row=0,column=0)
    

Label(root,text="frame1").grid(row=0,column=0)
Button(root,text="frame 2",command=frame2).grid(row=1,column=0)

# valu=('Female','other')
# padd={'padx':5,'pady':2,'width':5,'height':3}
# om=OptionMenu(root,gen,valu[0],*valu).pack()
# print(gen.get())
root.mainloop()