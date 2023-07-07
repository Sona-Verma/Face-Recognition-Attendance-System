from tkinter import*
from PIL import Image,ImageTk

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        # self.root.resizable(False,False)
        self.root.title("Face Recognition Attendance System")
       


        title=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title.place(x=0,y=0,width=1530,height=45)

        # Manage_std_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        # Manage_std_frame.place(x=15,y=65,width=1500,height=720)

        img11 = Image.open(r"images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img11 = img11.resize((1530,720), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl=Label(self.root,image=self.photoImg11)
        bg_lbl.place(x=0,y=55,width=1530,height=720)

        support=Label(bg_lbl,bg="white",text="Support : sonaverma553@@gmail.com",fg="blue",font=("times new roman",20,"bold"))
        support.place(x=500,y=200)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()