from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
from NeedHelp import First
from WantToHelp import Second

class Front:
    def __init__(self,root):
        self.root=root
        self.root.state("zoomed")
        # self.root.geometry("1366x700") #width x height
        # self.root.resizable(width=None,height=None)
        self.root.title("Help Each Other's")
        self.root.iconbitmap("icon.ico")

        bimg1=Image.open("images/front1.jpg")
        bimg1=bimg1.resize((683,700),Image.ANTIALIAS)
        self.bpict1=ImageTk.PhotoImage(bimg1)
        Label(self.root,image=self.bpict1).place(x=0,y=0,width=683,height=700)

        bimg=Image.open("images/front2.png")
        bimg=bimg.resize((683,700),Image.ANTIALIAS)
        self.bpict=ImageTk.PhotoImage(bimg)
        Label(self.root,image=self.bpict).place(x=683,y=0,width=683,height=700)


        Button(self.root,text="If you need help click here",bg="skyblue",fg="black",font=("Times New Roman",20,"bold"),relief=RAISED,bd=4,width=22,command=self.func1).place(x=860,y=280)

        Button(self.root,text="If you want to help click here",bg="lightgreen",fg="black",font=("Times New Roman",20,"bold"),relief=RAISED,bd=4,command=self.func2).place(x=860,y=400)

    def func1(self):
        self.user=Toplevel(self.root)
        self.app=First(self.user)
    
    def func2(self):
        self.helper=Toplevel(self.root)
        self.app1=Second(self.helper)



if __name__=="__main__":
    root=Tk()
    obj=Front(root)
    root.mainloop()