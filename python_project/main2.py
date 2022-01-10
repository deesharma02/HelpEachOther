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

Label(root,text="✌️HELP EACH OTHER ✌️",fg="white",background="black",font=("Constantia",30 ,"bold")).place(x=0,y=155,width=1366,height=50)

lf1=LabelFrame(root,text="Application Form",bg="white",bd=5,relief=GROOVE,font=("Times New Roman",20,"bold"),fg="black")
lf1.place(x=0,y=210,width=1366,height=490)

fname=Label(lf1,text="First Name ",fg="red",font=("Times New Roman",15,"bold"),bg="white")
fname.place(x=20,y=20)