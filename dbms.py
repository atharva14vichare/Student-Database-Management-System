#frontend
from tkinter import *
import tkinter.messagebox

import stdDatabaseBackend

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")
        stdid=StringVar()
        firstname=StringVar()
        surname=StringVar()
        dob=StringVar()
        age=StringVar()
        gender=StringVar()
        address=StringVar()
        mobile=StringVar()

        #.............................Functions.........................................
        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def clearData():
            self.txtstdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsuna.delete(0,END)
            self.txtdob.delete(0,END)
            self.txtage.delete(0,END)
            self.txtgen.delete(0,END)
            self.txtadd.delete(0,END)
            self.txtmobile.delete(0,END)

        def addData():
            if len(stdid.get())!=0:
                stdDatabaseBackend.addStudentRecord(stdid.get(), firstname.get(), surname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get())
                stdlist.delete(0,END)
                stdlist.insert(END,(stdid.get(), firstname.get(), surname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))

        def DisplayData():
            stdlist.delete(0,END)
            for row in stdDatabaseBackend.ViewData():
                stdlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd=stdlist.curselection()[0]
            sd=stdlist.get(searchStd)

            self.txtstdID.delete(0,END)
            self.txtstdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtsuna.delete(0,END)
            self.txtsuna.insert(END,sd[3])
            self.txtdob.delete(0,END)
            self.txtdob.insert(END,sd[4])
            self.txtage.delete(0,END)
            self.txtage.insert(END,sd[5])
            self.txtgen.delete(0,END)
            self.txtgen.insert(END,sd[6])
            self.txtadd.delete(0,END)
            self.txtadd.insert(END,sd[7])
            self.txtmobile.delete(0,END)
            self.txtmobile.insert(END,sd[8])

        def DeleteData():
            if len(stdid.get())!=0:
                stdDatabaseBackend.DeleteRec(sd[0])
                clearData()
                DisplayData()

        def SearchData():
            stdlist.delete(0,END)
            for row in stdDatabaseBackend.SearchRec(stdid.get(), firstname.get(), surname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()):
                stdlist.insert(END,row,str(""))
        
        def update():
            if(len(stdid.get())!=0):
                stdDatabaseBackend.DeleteRec(sd[0])
            if(len(stdid.get())!=0):
                stdDatabaseBackend.addStudentRecord(stdid.get(), firstname.get(), surname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get())
                stdlist.delete(0,END)
                stdlist.insert(END,(stdid.get(), firstname.get(), surname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))

        #...............................Frames..............................................
        Mainframe=Frame(self.root,bg="cadet blue")
        Mainframe.grid()

        Titleframe=Frame(Mainframe,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
        Titleframe.pack(side="top")

        self.Title=Label(Titleframe,font=('calibri',47,'bold'),text="Student Database Management Systems",bg="Ghost White")
        self.Title.grid(sticky=W)

        Buttonframe=Frame(Mainframe,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
        Buttonframe.pack(side="bottom")

        Dataframe=Frame(Mainframe,bd=1,width=1300,height=400,padx=20,pady=20,bg="cadet blue",relief=RIDGE)
        Dataframe.pack(side="bottom")

        Dataframeleft=LabelFrame(Dataframe,bd=1,width=1000,height=600,padx=20,bg="Ghost White",relief=RIDGE,font=('calibri',20,'bold'),text="Student Info\n")
        Dataframeleft.pack(side="left")

        Dataframeright=LabelFrame(Dataframe,bd=1,width=450,height=300,padx=31,pady=3,bg="Ghost White",relief=RIDGE,font=('calibri',20,'bold'),text="Student Details\n")
        Dataframeright.pack(side="right")

        #..............................Labels and Entry........................................
        self.lblstdID=Label(Dataframeleft,font=('calibri',20,'bold'),text="Student ID:",padx=2,pady=2,bg="Ghost White")
        self.lblstdID.grid(row=0,column=0, sticky=W)
        self.txtstdID=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=stdid,width=39)
        self.txtstdID.grid(row=0,column=1)

        self.lblfna=Label(Dataframeleft,font=('calibri',20,'bold'),text="Firstname:",padx=2,pady=2,bg="Ghost White")
        self.lblfna.grid(row=1,column=0, sticky=W)
        self.txtfna=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=firstname,width=39)
        self.txtfna.grid(row=1,column=1)

        self.lblsuna=Label(Dataframeleft,font=('calibri',20,'bold'),text="Surname:",padx=2,pady=2,bg="Ghost White")
        self.lblsuna.grid(row=2,column=0, sticky=W)
        self.txtsuna=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=surname,width=39)
        self.txtsuna.grid(row=2,column=1)

        self.lbldob=Label(Dataframeleft,font=('calibri',20,'bold'),text="Date of Birth:",padx=2,pady=3,bg="Ghost White")
        self.lbldob.grid(row=3,column=0, sticky=W)
        self.txtdob=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=dob,width=39)
        self.txtdob.grid(row=3,column=1)

        self.lblage=Label(Dataframeleft,font=('calibri',20,'bold'),text="Age:",padx=2,pady=3,bg="Ghost White")
        self.lblage.grid(row=4,column=0, sticky=W)
        self.txtage=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=age,width=39)
        self.txtage.grid(row=4,column=1)

        self.lblgen=Label(Dataframeleft,font=('calibri',20,'bold'),text="Gender:",padx=2,pady=3,bg="Ghost White")
        self.lblgen.grid(row=5,column=0, sticky=W)
        self.txtgen=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=gender,width=39)
        self.txtgen.grid(row=5,column=1)

        self.lbladd=Label(Dataframeleft,font=('calibri',20,'bold'),text="Address:",padx=2,pady=3,bg="Ghost White")
        self.lbladd.grid(row=6,column=0, sticky=W)
        self.txtadd=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=address,width=39)
        self.txtadd.grid(row=6,column=1)

        self.lblmobile=Label(Dataframeleft,font=('calibri',20,'bold'),text="Mobile:",padx=2,pady=3,bg="Ghost White")
        self.lblmobile.grid(row=7,column=0, sticky=W)
        self.txtmobile=Entry(Dataframeleft,font=('calibri',20,'bold'),textvariable=mobile,width=39)
        self.txtmobile.grid(row=7,column=1)

        #........................................listbox and scroll bar...................
        scrollbar=Scrollbar(Dataframeright)
        scrollbar.grid(row=0,column=1,sticky='ns')

        stdlist=Listbox(Dataframeright,width=41,height=16,font=('calibri',12,'bold'), yscrollcommand=scrollbar.set)
        stdlist.bind('<<ListboxSelect>>',StudentRec)
        stdlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=stdlist.yview)

        #......................................Button.........................................
        self.btnadddata=Button(Buttonframe,text='Add New',font=('calibri',20,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnadddata.grid(row=0,column=0)

        self.btndispdata=Button(Buttonframe,text='Display',font=('calibri',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btndispdata.grid(row=0,column=1)

        self.btnclear=Button(Buttonframe,text='Clear',font=('calibri',20,'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnclear.grid(row=0,column=2)

        self.btndelete=Button(Buttonframe,text='Delete',font=('calibri',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btndelete.grid(row=0,column=3)

        self.btnsearch=Button(Buttonframe,text='Search',font=('calibri',20,'bold'),height=1,width=10,bd=4,command=SearchData)
        self.btnsearch.grid(row=0,column=4)

        self.btnupdate=Button(Buttonframe,text='Update',font=('calibri',20,'bold'),height=1,width=10,bd=4,command=update)
        self.btnupdate.grid(row=0,column=5)

        self.btnexit=Button(Buttonframe,text='Exit',font=('calibri',20,'bold'),height=1,width=10,bd=4, command=iExit)
        self.btnexit.grid(row=0,column=6)

                
#main function
root=Tk()
application=Student(root)
root.mainloop()
