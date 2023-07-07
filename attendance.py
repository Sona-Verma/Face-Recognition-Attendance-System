from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from csv import DictReader,DictWriter

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img=Image.open(r"images\photos.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        img1=Image.open(r"images\att.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        img3 = Image.open(r"images\background.jpg")
        img3 = img3.resize((1530,710), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        bg_lbl=Label(self.root,image=self.photoImg3)
        bg_lbl.place(x=0,y=200,width=1530,height=710)

        title=Label(bg_lbl,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"images\train.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        DataFrameLeft=LabelFrame(Left_frame,bd=2,relief=RIDGE,fg="crimson",bg="white")
                                               
        DataFrameLeft.place(x=0,y=135,width=720,height=370)

        attendanceId_label=Label(DataFrameLeft,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(DataFrameLeft,width=22,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        roll_no_label=Label(DataFrameLeft,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=4,pady=8)

        roll_no_entry=ttk.Entry(DataFrameLeft,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=0,column=3,pady=8)

        nameLabel=Label(DataFrameLeft,text="Name:",bg="white",font=("times new roman",13,"bold"))
        nameLabel.grid(row=1,column=0)
        atten_date=ttk.Entry(DataFrameLeft,width=22,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_date.grid(row=1,column=1,pady=8)

        depLabel=Label(DataFrameLeft,text="Department:",bg="white",font=("times new roman",13,"bold"))
        depLabel.grid(row=1,column=2)
        atten_date=ttk.Entry(DataFrameLeft,width=22,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        atten_date.grid(row=1,column=3,pady=8)

        timeLabel=Label(DataFrameLeft,text="Time:",bg="white",font=("times new roman",13,"bold"))
        timeLabel.grid(row=2,column=0)
        atten_date=ttk.Entry(DataFrameLeft,width=22,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=1,pady=8)

        dateLabel2=Label(DataFrameLeft,text="Date:",bg="white",font=("times new roman",13,"bold"))
        dateLabel2.grid(row=2,column=2)
        atten_date=ttk.Entry(DataFrameLeft,width=22,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

        attendanceLabel=Label(DataFrameLeft,text="Attendance Status",bg="white",font=("times new roman",13,"bold"))
        attendanceLabel.grid(row=3,column=0)
        self.atten_status=ttk.Combobox(DataFrameLeft,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        ButtonFrame1=Frame(DataFrameLeft,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=300,width=715,height=38)

        btnAddData=Button(ButtonFrame1,command=self.importCsv,text="Import csv",width=19,font=("arial",11,"bold"),bg="blue",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnUpdate=Button(ButtonFrame1,text="Export csv",command=self.export_data,width=19,font=("arial",11,"bold"),bg="blue",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(ButtonFrame1,text="Update",command=self.action,width=19,font=("arial",11,"bold"),bg="blue",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(ButtonFrame1,text="Reset",command=self.clear,width=19,font=("arial",11,"bold"),bg="blue",fg="white")
        btnReset.grid(row=0,column=3,padx=1)

        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        AttendanceFrame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        AttendanceFrame.place(x=5,y=5,width=700,height=455)

        scroll_x=ttk.Scrollbar(AttendanceFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(AttendanceFrame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(AttendanceFrame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
    
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

         

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i) 

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            # mydata=[]
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)  

    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendance=self.var_atten_attendance.get()  

        try:
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendance
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)      


    def export_data(self):
        try:
            if len (mydata) <1:
                messagebox.showerror("No Data","No Data to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open (fln,mode="w",newline="") as myfile:
                exp_writer=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_writer.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  


    def get_cursor(self,event=""):
        cursor_rows=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_rows)
        row=content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6]) 

    def clear(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        self.atten_id.focus()                          





if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()                