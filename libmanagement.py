from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")  
        self.root.geometry("1550x800+0+0")

        #=================================================== VARIABLE ========================================================

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="light green",fg="red",bd=20,relief=RIDGE,font=("times new roman",50,"italic"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light green")
        frame.place(x=0,y=130,width=1530,height=400)

        #============================================= DATA FRAME LEFT ===================================================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="light green",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="light green",text="Member Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state= "readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,text="PRN No",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,text="ID No:",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,text="FirstName",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,text="LastName",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,text="Address1",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,text="Address2",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostalCode=Label(DataFrameLeft,text="PostalCode",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostalCode.grid(row=7,column=0,sticky=W)
        txtPostalCode=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.postcode_var,width=29)
        txtPostalCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,text="BookId",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,text="BookTitle",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,text="Author",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,text="DateBorrowed",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,text="Date Due",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDaysonbook=Label(DataFrameLeft,text="Days On Book",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysonbook.grid(row=5,column=2,sticky=W)
        txtDaysonbook=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysonbook.grid(row=5,column=3)

        lblLatereturnfine=Label(DataFrameLeft,text="Late Return Fine",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLatereturnfine.grid(row=6,column=2,sticky=W)
        txtLatereturnfine=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLatereturnfine.grid(row=6,column=3)

        lblOverDate=Label(DataFrameLeft,text="Date Over Due",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblOverDate.grid(row=7,column=2,sticky=W)
        txtOverDate=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtOverDate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,text="ActualPrice",bg="light green",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

        #============================================ DATAFRAME RIGHT ==========================================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="light green",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtbox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listbook=["Python Crash Course",
"Automate the Boring Stuff with Python",
"Learning Python",
"Python Cookbook",
"Fluent Python",
"Python for Data Analysis",
"Effective Python",
"Think Python",
"Python Pocket Reference",
"Python Tricks",
"Python Programming",
"Python Data Science Handbook",
"Introduction to Machine Learning with Python",
"Python Machine Learning",
"Deep Learning with Python",
"Python for Kids",
"Head First Python",
"Python Testing with pytest",
"Python in a Nutshe",
"Serious Python"]

        
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if x=="Python Crash Course":
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Barry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.800")

            elif x=="Automate the Boring Stuff with Python":
                self.bookid_var.set("BKID5678")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Barry")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")
            
            elif x=="Learning Python":
                self.bookid_var.set("BKID5679")
                self.booktitle_var.set("Learning Python")
                self.author_var.set("Mark Lutz")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.920")

            elif x=="Python Cookbook":
                self.bookid_var.set("BKID5680")
                self.booktitle_var.set("Python Cookbook")
                self.author_var.set("David Beazley")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.950")

            elif x=="Fluent Python":
                self.bookid_var.set("BKID5681")
                self.booktitle_var.set("Fluent Python")
                self.author_var.set("Luciano Ramalho")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1050")

            elif x=="Python for Data Analysis":
                self.bookid_var.set("BKID5682")
                self.booktitle_var.set("Python for Data Analysis")
                self.author_var.set("Wes McKinney")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1100")

            elif x=="Effective Python":
                self.bookid_var.set("BKID5683")
                self.booktitle_var.set("Effective Python")
                self.author_var.set("Brett Slatkin")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")

            elif x=="Think Python":
                self.bookid_var.set("BKID5684")
                self.booktitle_var.set("Think Python")
                self.author_var.set("Allen B. Downey")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.850")

            elif x=="Python Pocket Reference":
                self.bookid_var.set("BKID5685")
                self.booktitle_var.set("Python Pocket Reference")
                self.author_var.set("Mark Lutz")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif x=="Python Tricks":
                self.bookid_var.set("BKID5686")
                self.booktitle_var.set("Python Tricks")
                self.author_var.set("Dan Bader")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")

            elif x=="Python Programming":
                self.bookid_var.set("BKID5687")
                self.booktitle_var.set("Python Programming")
                self.author_var.set("John Zelle")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.600")

            elif x=="Python Data Science Handbook":
                self.bookid_var.set("BKID5688")
                self.booktitle_var.set("Python Data Science Handbook")
                self.author_var.set("Jake VanderPlas")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1200")

            elif x=="Introduction to Machine Learning with Python":
                self.bookid_var.set("BKID5689")
                self.booktitle_var.set("Introduction to Machine Learning with Python")
                self.author_var.set("Andreas C. Müller")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1000")

            elif x=="Python Machine Learning":
                self.bookid_var.set("BKID5690")
                self.booktitle_var.set("Python Machine Learning")
                self.author_var.set("Sebastian Raschka")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1300")

            elif x=="Deep Learning with Python":
                self.bookid_var.set("BKID5691")
                self.booktitle_var.set("Deep Learning with Python")
                self.author_var.set("Francois Chollet")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1500")

            elif x=="Python for Kids":
                self.bookid_var.set("BKID5692")
                self.booktitle_var.set("Python for Kids")
                self.author_var.set("Jason R. Briggs")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.800")
            
            elif x=="Head First Python":
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("Python Introduction")
                self.author_var.set("Paul Barry")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.650")

            elif x=="Python Testing with pytest":
                self.bookid_var.set("BKID2345")
                self.booktitle_var.set("Testing with pytest")
                self.author_var.set("Brian Okken")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")

            elif x=="Python in a Nutshell":
                self.bookid_var.set("BKID3456")
                self.booktitle_var.set("Python Reference")
                self.author_var.set("Alex Martelli")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.850")

            elif x=="Serious Python":
                self.bookid_var.set("BKID4567")
                self.booktitle_var.set("Advanced Python")
                self.author_var.set("Julien Danjou")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.780")


        listbox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=16) #yscrollcommand=listScrollbar.set
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0, column=0, padx=8)
        listScrollbar.config(command=listbox.yview)

   


        for item in listbook:
            listbox.insert(END, item)


        #=================================================== BUTTON FRAME =============================================================


        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light green")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAdddata=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="black",fg="white")
        btnAdddata.grid(row=0,column=0)

        btnShowdata=Button(Framebutton,command=self.showData,text="SHOW DATA", font=("times new roman", 12, "bold"),width=27,bg="black",fg="white")
        btnShowdata.grid(row=0,column=1)

        btnUpdatedata=Button(Framebutton,command=self.update,text="UPDATE DATA", font=("times new roman", 12, "bold"),width=27,bg="black",fg="white")
        btnUpdatedata.grid(row=0,column=2)

        btnDeletedata=Button(Framebutton,command=self.delete,text="DELETE DATA", font=("times new roman", 12, "bold"),width=27,bg="black",fg="white")
        btnDeletedata.grid(row=0,column=3)

        btnResetdata=Button(Framebutton,command=self.reset,text="RESET DATA", font=("times new roman", 12, "bold"),width=27,bg="black",fg="white")
        btnResetdata.grid(row=0,column=4)

        btnExitdata=Button(Framebutton,command=self.Exit,text="EXIT DATA", font=("times new roman", 12, "bold"),width=23,bg="black",fg="white")
        btnExitdata.grid(row=0,column=5)

        #-----------------------------------------------INFORMATION FRAME-----------------------------------------------------------------

        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light green")
        Framedetails.place(x=0,y=600,width=1550,height=190)

        Table_frame=Frame(Framedetails, bd=6, relief=RIDGE, bg="light green")
        Table_frame.place(x=0, y=2, width=1490, height=170)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.librarary_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1",
        "address2","postid","mobile","bookid","booktitle","author",
        "dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
         
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.librarary_table.xview)
        yscroll.config(command=self.librarary_table.yview)

        
        self.librarary_table.heading("membertype",text="Member Type")
        self.librarary_table.heading("prnno",text="Refrence No.")
        self.librarary_table.heading("title",text="Title")
        self.librarary_table.heading("firstname",text="First Name")
        self.librarary_table.heading("lastname",text="Last Name")
        self.librarary_table.heading("address1",text="Address1")
        self.librarary_table.heading("address2",text="Address2")
        self.librarary_table.heading("postid",text="Post ID")
        self.librarary_table.heading("mobile",text="Mobile")
        self.librarary_table.heading("bookid",text="Book ID")
        self.librarary_table.heading("booktitle",text="Book Title")
        self.librarary_table.heading("author",text="Author")
        self.librarary_table.heading("dateborrowed",text="Date of Borrowed")
        self.librarary_table.heading("datedue",text="Datedue")
        self.librarary_table.heading("days",text="Days On Book")
        self.librarary_table.heading("latereturnfine",text="LatereturnFine")
        self.librarary_table.heading("dateoverdue",text="DateOverDue")
        self.librarary_table.heading("finalprice",text="FinalPrice")

        self.librarary_table["show"]="headings"

        
        self.librarary_table.column("membertype",width=100)
        self.librarary_table.column("prnno",width=100)
        self.librarary_table.column("title",width=100)
        self.librarary_table.column("firstname",width=100)
        self.librarary_table.column("lastname",width=100)
        self.librarary_table.column("address1",width=100)
        self.librarary_table.column("address2",width=100)
        self.librarary_table.column("postid",width=100)
        self.librarary_table.column("mobile",width=100)
        self.librarary_table.column("bookid",width=100)
        self.librarary_table.column("booktitle",width=100)
        self.librarary_table.column("author",width=100)
        self.librarary_table.column("dateborrowed",width=100)
        self.librarary_table.column("datedue",width=100)
        self.librarary_table.column("days",width=100)
        self.librarary_table.column("latereturnfine",width=100)
        self.librarary_table.column("dateoverdue",width=100)
        self.librarary_table.column("finalprice",width=100)

        self.librarary_table.pack(fill=BOTH,expand=1)

        self.fetch_data()
        self.librarary_table.bind("<ButtonRelease-1>",self.get_cursor)

        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priyansu@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.member_var.get(),
                                        self.prn_var.get(),
                                        self.id_var.get(),
                                        self.firstname_var.get(),
                                        self.lastname_var.get(),
                                        self.address1_var.get(),
                                        self.address2_var.get(),
                                        self.postcode_var.get(),
                                        self.mobile_var.get(),
                                        self.bookid_var.get(),
                                        self.booktitle_var.get(),
                                        self.author_var.get(),
                                        self.dateborrowed_var.get(),
                                        self.datedue_var.get(),
                                        self.daysonbook_var.get(),
                                        self.latereturnfine_var.get(),
                                        self.dateoverdue_var.get(),
                                        self.finalprice_var.get()
                                                                                                              ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priyansu@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Author=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                        self.member_var.get(),
                                        self.id_var.get(),
                                        self.firstname_var.get(),
                                        self.lastname_var.get(),
                                        self.address1_var.get(),
                                        self.address2_var.get(),
                                        self.postcode_var.get(),
                                        self.mobile_var.get(),
                                        self.bookid_var.get(),
                                        self.booktitle_var.get(),
                                        self.author_var.get(),
                                        self.dateborrowed_var.get(),
                                        self.datedue_var.get(),
                                        self.daysonbook_var.get(),
                                        self.latereturnfine_var.get(),
                                        self.dateoverdue_var.get(),
                                        self.finalprice_var.get(),
                                        self.prn_var.get(),

                                ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member Has Been Updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priyansu@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.librarary_table.delete(*self.librarary_table.get_children())
            for i in  rows:
                self.librarary_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    
    def get_cursor(self,event=""):
        cursor_row=self.librarary_table.focus()
        content=self.librarary_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtbox.insert(END,"Member Type:\t\t"+ self.member_var.get()+"\n")
        self.txtbox.insert(END,"PRN no:\t\t"+ self.prn_var.get()+"\n")
        self.txtbox.insert(END,"ID no:\t\t"+ self.id_var.get()+"\n")
        self.txtbox.insert(END,"First Name:\t\t"+ self.firstname_var.get()+"\n")
        self.txtbox.insert(END,"Last name:\t\t"+ self.lastname_var.get()+"\n")
        self.txtbox.insert(END,"Address1:\t\t"+ self.address1_var.get()+"\n")
        self.txtbox.insert(END,"Address2:\t\t"+ self.address2_var.get()+"\n")
        self.txtbox.insert(END,"Post Code:\t\t"+ self.postcode_var.get()+"\n")
        self.txtbox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get()+"\n")
        self.txtbox.insert(END,"Book Id:\t\t"+ self.bookid_var.get()+"\n")
        self.txtbox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get()+"\n")
        self.txtbox.insert(END,"Author:\t\t"+ self.author_var.get()+"\n")
        self.txtbox.insert(END,"Date Borrowed:\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtbox.insert(END,"Date Due:\t\t"+ self.datedue_var.get()+"\n")
        self.txtbox.insert(END,"Days on Book:\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtbox.insert(END,"Late Return Fine:\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtbox.insert(END,"Date Over Due:\t\t"+ self.dateoverdue_var.get()+"\n")
        self.txtbox.insert(END,"Final Price:\t\t"+ self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtbox.delete("1.0",END)

    def Exit(self):
        Exit=tkinter.messagebox.askyesno("LIBRARY MANAGEMENT SYSTEM","Do You Want To Exit ?")
        if Exit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Priyansu@123",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")

                      
    
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
            


