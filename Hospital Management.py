from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hospital Management System")
        self.geometry("1540x800+0+0")
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        
        
        
        

        # Creating and packing the label
        lbtitle = tk.Label(self, bd=20, relief=tk.RIDGE, text="Hospital Management System", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbtitle.pack(side=tk.TOP, fill='x')
        
        # =============Dataframe=========
        # Access self instead of self.root
        Dataframe = tk.Frame(self, bd=20, relief=tk.RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)
        
        DataframeLeft= tk.LabelFrame(Dataframe,bd=10,padx=20,relief=tk.RIDGE,font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight= tk.LabelFrame(Dataframe,bd=10,padx=20,relief=tk.RIDGE,font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        #=====================Buttons frame===========================
        Buttonframe=tk.Frame(self,bd=20,relief=tk.RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        Detailsframe=tk.Frame(self,bd=20,relief=tk.RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #==================DataframeLeft=======================
        
        lbNameTablet=tk.Label(DataframeLeft,text="Name OF Tablets",font=("arial",12,"bold"),padx=2,pady=6)
        lbNameTablet.grid(row=0,column=0,sticky=W)
        
        
        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=33)
        comNameTablet["values"]=("Nice","Corona vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)
        
        lbref=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Reference no:",padx=2)
        lbref.grid(row=1,column=0,sticky=W)
        txtref=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        #============dose=============
        
        lbdose=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lbdose.grid(row=2,column=0,sticky=W)
        txtdose=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtdose.grid(row=2,column=1)
        #================count of tablets=============
        
        lb1NoOftablets=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lb1NoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lb1Lot=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lb1Lot.grid(row=4,column=0,sticky=W)
        txtLot=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        #==============issue date================
        lb1issueDate=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lb1issueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)
        #=======expire date=======================
        lb1ExpDate=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lb1ExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)
        #=============DailyDose==================
        lb1DailyDose=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lb1DailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
        #==============Side effects==============
        lb1SideEffect=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6)
        lb1SideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8,column=1)
        #=============Extra info=============
        lb1Furtherinfo=tk.Label(DataframeLeft,font=("arial",12,"bold"),text=" Further info:",padx=2,pady=6)
        lb1Furtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)
        #=============blood pressure===========
        lb1DrivingMachine=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lb1DrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtDrivingMachine.grid(row=1,column=3)
        
        #=============Storage============
        lb1Storage=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lb1Storage.grid(row=2,column=2,sticky=W)
        txtStorage=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)
        #=============Medicines===========
        lb1Medicine=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lb1Medicine.grid(row=3,column=2,sticky=W)
        txtMedicine=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)
        #================PatientId==========
        lb1PatientId=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lb1PatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        #=============Nhsnumber==============
        lb1NhsNumber=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lb1NhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)
        #=============patient name===========
        lb1PatientName=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lb1PatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)
        #==============DOB====================
        lb1DateOfBirth=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lb1DateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)
        #============patient Address============
        lb1PatientAddress=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
        lb1PatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        #========DataFrameRight==============
        self.txtPrescription=tk.Text(DataframeRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)   
        #==============button=================================
        btnPrescription = Button(Buttonframe,command=self.iPrescription, bg="green", fg="white", font=("arial", 12, "bold"), text="Prescription", width=23, height=2, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)
        
        btnPrescriptionData = Button(Buttonframe,command=self.iPrescriptionData, bg="green", fg="white", font=("arial", 12, "bold"), text="Prescription Data", width=23, height=2, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)
        
        btnUpdate = Button(Buttonframe,command=self.update_data, bg="green", fg="white", font=("arial", 12, "bold"), text="Update", width=23, height=2, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)
        
        btnDelete = Button(Buttonframe, command=self.idelete,bg="green", fg="white", font=("arial", 12, "bold"), text="Delete", width=23, height=2, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)
        
        btnclear = Button(Buttonframe,command=self.clear, bg="green", fg="white", font=("arial", 12, "bold"), text="clear", width=23, height=2, padx=2, pady=6)
        btnclear.grid(row=0, column=4)
        
        btnExit = Button(Buttonframe,command=self.iExit, bg="green", fg="white", font=("arial", 12, "bold"), text="Exit", width=23, height=2, padx=2, pady=6)
        btnExit.grid(row=0, column=5)
        
        # ===============Table===============
        # ===========scrollbar===============
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe, columns=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pnamer", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        

        self.hospital_table.heading("nameoftable", text="Name of tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pnamer", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"
        

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pnamer", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease -1>", self.get_cursor)

        self.fetch_data()
        
    #======Functionality Declareation=====
    def iPrescriptionData(self):
      if self.Nameoftablets.get() == "" or self.ref.get() == "":
        messagebox.showerror("Error", "All fields are required")
      else:
        conn = mysql.connector.connect(host="localhost", user="root", password="arunmano@2002", database="sys")
        my_cursor = conn.cursor()
        query = "INSERT INTO hospital1 (Name_of_tablets, reference_No, dose, Numbersoftablets, lot, issuedate, expdate, dailydose, storage, nhsnumber, patientname, DOB, patientaddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.Nameoftablets.get(), self.ref.get(), self.Dose.get(), self.NumberofTablets.get(), self.Lot.get(), self.Issuedate.get(), self.ExpDate.get(), self.DailyDose.get(), self.StorageAdvice.get(), self.nhsNumber.get(), self.PatientName.get(), self.DateOfBirth.get(), self.PatientAddress.get())

        my_cursor.execute(query, values)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been inserted")
            
    def update_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="arunmano@2002", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE hospital1 SET Name_of_tablets=%s, reference_No=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s",
                      (self.Nameoftablets.get(), self.ref.get(), self.Dose.get(),
                       self.NumberofTablets.get(), self.Lot.get(), self.Issuedate.get(),
                       self.ExpDate.get(), self.DailyDose.get(), self.StorageAdvice.get(),
                       self.nhsNumber.get(), self.PatientName.get(),
                       self.DateOfBirth.get(), self.PatientAddress.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Record has been updated Successfully")
    def fetch_data(self):
           conn = mysql.connector.connect(host="localhost", user="root", password="arunmano@2002", database="sys")
           my_cursor = conn.cursor()
           my_cursor.execute("SELECT * FROM hospital1")
           rows = my_cursor.fetchall()
           if len(rows) != 0:
                  self.hospital_table.delete(*self.hospital_table.get_children())
                  for row in rows:
                          self.hospital_table.insert("", "end", values=row)
                  conn.commit()
           conn.close()
    def get_cursor(self, event=""):
           cursor_row = self.hospital_table.focus()
           content = self.hospital_table.item(cursor_row)
           row = content["values"]
           self.Nameoftablets.set(row[0])
           self.ref.set(row[1])
           self.Dose.set(row[2])
           self.NumberofTablets.set(row[3])
           self.Lot.set(row[4])
           self.Issuedate.set(row[5])
           self.ExpDate.set(row[6])
           self.DailyDose.set(row[7])
           self.StorageAdvice.set(row[8])
           self.nhsNumber.set(row[9])
           self.PatientName.set(row[10])
           self.DateOfBirth.set(row[11])
           self.PatientAddress.set(row[12])
    
    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets: \t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot: \t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date: \t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date: \t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose: \t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect: \t\t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice: \t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Driving Using Machine: \t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "PatientId: \t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number: \t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name: \t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birthday: \t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address: \t\t\t" + self.PatientAddress.get() + "\n")
        
    def idelete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="arunmano@2002", database="sys")
        my_cursor = conn.cursor()
        query = "DELETE FROM hospital1 WHERE Reference_No = %s"
        value = (self.ref.get(),)  
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()  
        messagebox.showinfo("Delete", "Patient has been deleted successfully")
        
    def clear(self):
       self.Nameoftablets.set("")
       self.ref.set("")
       self.Dose.set("")
       self.NumberofTablets.set("")
       self.Lot.set("")
       self.Issuedate.set("")
       self.ExpDate.set("")
       self.DailyDose.set("")
       self.sideEfect.set("")
       self.FurtherInformation.set("")  
       self.StorageAdvice.set("")
       self.DrivingUsingMachine.set("")  
       self.HowToUseMedication.set("")  
       self.PatientId.set("")
       self.nhsNumber.set("")
       self.PatientName.set("")
       self.DateOfBirth.set("")
       self.PatientAddress.set("")
       self.txtPrescription.delete("1.0", END)
       
    def iExit(self):
        iExit = messagebox.askyesno("Hospital management system", "Confirm you want to exit")
        if iExit > 0:
           root.destroy()
           return
       

if __name__ == "__main__":
    root = Hospital()
    root.mainloop()