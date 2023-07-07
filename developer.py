from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title=Label(self.root,text="DEVELOPER INFORMATION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title.place(x=0,y=(-1),width=1550,height=45)

        # Manage_std_frame=Frame(self.root,bd=2,relief=RIDGE,bg="skyblue")
        # Manage_std_frame.place(x=15,y=65,width=1500,height=700)

        img11 = Image.open(r"images\developer_img.jpg")
        img11 = img11.resize((1530,700), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl=Label(self.root,image=self.photoImg11)
        bg_lbl.place(x=10,y=65,width=1530,height=700)

        Manage_std_frame1=Frame(bg_lbl,bd=2,relief=RIDGE,bg="black")
        Manage_std_frame1.place(x=1000,y=5,width=500,height=660)

        img1 = Image.open(r"images\sona2.jpg")
        img1 = img1.resize((230,220), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(Manage_std_frame1,image=self.photoImg1,bg="white")
        bg_lbl.place(x=345,y=0,width=230,height=220)

        img111 = Image.open(r"images\graphic.jpg")
        img111 = img111.resize((550,550), Image.ANTIALIAS)
        self.photoImg111 = ImageTk.PhotoImage(img111)
        bg_lbl=Label(Manage_std_frame1,image=self.photoImg111,bg="white")
        bg_lbl.place(x=0,y=180,width=550,height=550)

        support=Label(Manage_std_frame1,bg="black",fg="white",text="Hello,my name is",font=("times new roman",17,"bold"))
        support.place(x=10,y=10)

        support=Label(Manage_std_frame1,bg="black",fg="blue",text="Sona Verma",font=("times new roman",22,"bold"))
        support.place(x=10,y=45)

        support=Label(Manage_std_frame1,bg="black",fg="white",text="I am student of Graphic Era University",font=("arial",12,"bold"))
        support.place(x=10,y=110)

        support=Label(Manage_std_frame1,bg="black",fg="white",text="This is my 5th sem Project",font=("arial",12,"bold"))
        support.place(x=10,y=140)

        support=Label(Manage_std_frame1,bg="black",fg="white",text="Programming languege used : python",font=("arial",12,"bold"))
        support.place(x=10,y=170)




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()           