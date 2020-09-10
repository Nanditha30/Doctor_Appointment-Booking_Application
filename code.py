import tkinter as tk
from tkinter import messagebox
class Doctor:
    def __init__(self,firstname,lastname,LicenseID,pwd,confirmpwd,mobile,EmailID,gender,specialization):
        self.firstname=firstname
        self.lastname=lastname
        self.LicenseID=LicenseID
        self.pwd=pwd
        self.confirmpwd=confirmpwd
        self.mobile=mobile
        self.EmailID=EmailID
        self.gender=gender
        self.specialization=specialization
        self.doctor_calender={}
    def isdoctoravailable(self,slot):
        if slot in self.doctor_calender.keys():
            return False
        else:
            return True
    def doctor_calenderupdate(self,patient,slot):
        self.doctor_calender[slot]=patient
        self.pats=list(self.doctor_calender.values())
    def getkey(self,patient):
        for key,value in self.doctor_calender.items():
         if patient==value:
             return key
d1=Doctor('Amit','Kumar','16012',"amit@1","amit@1",'9573467892','amitk1@gmail.com','male','physician')
d2=Doctor('Swetha','Bansal','16013',"swetha@2","swetha@2",'9574912345','swethab2@gmail.com',"female","Gynaec")
d3=Doctor('Ramesh','kumar','16014',"ramesh@3","ramesh@3","9574954321",'rameshk3@gmail.com',"male","cardio")
listofdocs=[d1,d2,d3]
def createdoc(firstname,lastname,LicenseID,pwd,confirmpwd,mobile,EmailID,gender,specialization):
    d=Doctor(firstname,lastname,LicenseID,pwd,confirmpwd,mobile,EmailID,gender,specialization)
    global listofdocs
    listofdocs.append(d)
class Patient:
    def __init__(self,firstname,lastname,age,pwd,confirmpwd,mobile,EmailID,gender,weight):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.pwd=pwd
        self.confirmpwd=confirmpwd
        self.mobile=mobile
        self.EmailID=EmailID
        self.gender=gender
        self.weight=weight
        self.patient_calender={}
    def ispatientavailable(self,slot):
        if slot in self.patient_calender.keys():
            #print("you have no time")
            return False
        else:
            return True
    def patient_calenderupdate(self,doctor,slot):
        self.patient_calender[slot]=doctor
p1=Patient("jake","peralta","35","diehard","diehard","9876543256","jake99@gmail.com","male","55")
p2=Patient("Amy","Sntiago","33","harypotter","harypotter","7658423478","amy1@gmail.com","female","50")
p3=Patient("charles","Boyle","38","nikolaj","nikolaj","6578093451","charlesb@gmail.com","male","55")
p4=Patient("Scully"," ","45","lasagne","lasagne","3456712394","scullyham@gmail.com","male","70")
listofpats=[p1,p2,p3,p4]
def createpat(firstname,lastname,age,pwd,confirmpwd,mobile,EmailID,gender,weight):
    p=Patient(firstname,lastname,age,pwd,confirmpwd,mobile,EmailID,gender,weight)
    global listofpats
    listofpats.append(p)
SLOT_1 = '8:00AM'
SLOT_2 = '8:30AM'
SLOT_3 = '9:00AM'
SLOT_4 = '9:30AM'
SLOT_5 = '10:00AM'
SLOT_6 = '10:30AM'
SLOT_7 = '11:00AM'
SLOT_8 = '11:30AM'
SLOT_9 = '1:00PM'
SLOT_10 = '1:30PM'
SLOT_11 = '2:00PM'
SLOT_12 = '2:30PM'
SLOT_13 = '3:00PM'
SLOT_14 = '3:30PM'
SLOT_15 = '4:00PM'
SLOT_16 = '4:30PM'
listslots = [SLOT_1, SLOT_2, SLOT_3, SLOT_4, SLOT_5, SLOT_6, SLOT_7, SLOT_8, SLOT_9, SLOT_10, SLOT_11, SLOT_12, SLOT_13, SLOT_14, SLOT_15, SLOT_16]
class schedule:
    m=1
    def __init__(self,doctor,patient,slot):
        self.doctor=doctor
        self.patient=patient
        self.slot=slot
        if self.doctor.isdoctoravailable(self.slot) and self.patient.ispatientavailable(self.slot):
                self.doctor.doctor_calenderupdate(self.patient,self.slot)
                self.patient.patient_calenderupdate(self.doctor,self.slot)
                self.m=0
    def availability(self):
        if(self.m==0):
            messagebox.showinfo("showinfo","slot is  booked")
        else:
            messagebox.showinfo("showinfo","slot is already booked")
s1=schedule(d1,p1,SLOT_8)
s2=schedule(d1,p2,SLOT_9)
s3=schedule(d2,p2,SLOT_5)
s4=schedule(d3,p1,SLOT_11)
s5=schedule(d3,p3,SLOT_1)
s6=schedule(d2,p3,SLOT_3)
s7=schedule(d1,p4,SLOT_6)
s8=schedule(d3,p4,SLOT_2)
s9=schedule(d2,p4,SLOT_1)
def createschedule(doct ,pa,slot):
    doc=doct.split()
    global listofdocs
    for i in listofdocs:
        if(i.firstname==doc[0]):
            do=i
    s=schedule(do,pa,slot)
    s.availability()
def displaydetails(patient):
    window14=tk.Tk()
    window14.title("Display")
    window14.geometry("350x100")
    window14.configure(bg="light blue")
    docs=tk.StringVar(window14)
    slots=tk.StringVar(window14)
    tk.Label(window14,text="Doctors",width="20",font=("bold",10),bg="lightblue").grid(row=0,column=0)
    tk.Label(window14,text="Slots",width="20",font=("bold",10),bg="lightblue").grid(row=0,column=1)

    global listofdocs
    global listslots
    list2=[]
    for i in listofdocs:
        list2.append(i.firstname + " " + i.lastname + ": " + i.specialization)

    droplist=tk.OptionMenu(window14,docs,*list2)
    droplist.config(bg="lightblue",width="16")
    docs.set("select")
    droplist.grid(row=1, column=0)

    droplist=tk.OptionMenu(window14,slots,*listslots)
    droplist.config(bg="lightblue",width="16")
    slots.set("select")
    droplist.grid(row=1, column=1)
    tk.Button(window14, text = "Submit", width="20",font=("bold",10),bg="black",fg="white",command=lambda:createschedule(docs.get(),patient,slots.get())).grid(row = 3, column = 1)
    window14.mainloop()
def displaydetailsofpat(doctor):
    window14=tk.Tk()
    window14.title("Display")
    window14.geometry("600x200")
    window14.configure(bg="light blue")
    tk.Label(window14,text="PatientName",width="20",font=("bold",10),bg="lightblue").grid(row=0,column=0)
    tk.Label(window14,text="Gender",width="10",font=("bold",10),bg="lightblue").grid(row=0,column=1)
    tk.Label(window14,text="Age",width="10",font=("bold",10),bg="lightblue").grid(row=0,column=2)
    tk.Label(window14,text="Weight",width="10",font=("bold",10),bg="lightblue").grid(row=0,column=3)
    tk.Label(window14,text="Slot",width="20",font=("bold",10),bg="lightblue").grid(row=0,column=4)
    for i in range(len(doctor.pats)):
        tk.Label(window14,text=doctor.pats[i].firstname,width="10",font=("bold",10),bg="lightblue").grid(row=i+1,column=0)
        tk.Label(window14,text=doctor.pats[i].gender,width="10",font=("bold",10),bg="lightblue").grid(row=i+1,column=1)
        tk.Label(window14,text=doctor.pats[i].age,width="10",font=("bold",10),bg="lightblue").grid(row=i+1,column=2)
        tk.Label(window14,text=doctor.pats[i].weight,width="10",font=("bold",10),bg="lightblue").grid(row=i+1,column=3)
        tk.Label(window14,text=doctor.getkey(doctor.pats[i]),width="10",font=("bold",10),bg="lightblue").grid(row=i+1,column=4)
    window14.mainloop()
def about():
    window4=tk.Tk()
    window4.title("About")
    window4.geometry("500x500")
    window4.configure(bg="rosy brown")
    tk.Label(window4,text="",bg="rosy brown").pack()
    tk.Label(window4,text="PACTO",font=("bold Italics",20),fg="black",bg="rosy brown").pack()
    tk.Label(window4,text="",bg="rosy brown").pack()
    t=tk.Text(window4,height=70,width=100,font=("Tempus Sans ITC",12),bg="lavender blush",fg='purple')
    t.pack()
    paragraph='''
        Going to the doctor isn’t most people’s favorite activity.
    But it is part of staying healthy (the other major parts are
    what you eatand how much you exercise).So you may as well get
    the most out of it.
    Whether you are just checking to make sure things are on
    track,or have a specific symptom you are concerned about,
    choosing your doctor is the first step.
           This application is useful for the pupose of booking
    online appointment of doctor especially in these lockdown period.
    In this Covid19 crisis situation ,OPs are shut down .So whatever
    be the problem you have regarding your health either about covid-19
    or any other health issue,you can consult a doctor on this platform
    by booking an appointment online'''
    t.insert(tk.END,paragraph)
    window4.mainloop()

def register2():
    window12=tk.Tk()
    window12.title("Signup")
    window12.geometry("500x500")
    window12.configure(bg="lightblue")
    firstname=tk.StringVar(window12)
    lastname=tk.StringVar(window12)
    age=tk.StringVar(window12)
    pwd=tk.StringVar(window12)
    confirmpwd=tk.StringVar(window12)
    mobile=tk.StringVar(window12)
    EmailID=tk.StringVar(window12)
    g=tk.IntVar(window12)
    weight=tk.StringVar(window12)
    def getvalues():
            gen=['0','Male','Female']
            f_name=firstname.get()
            l_name=lastname.get()
            a=age.get()
            pw_d=pwd.get()
            con_pwd=confirmpwd.get()
            mob=mobile.get()
            email=EmailID.get()
            gender=gen[g.get()]
            wei_ght=weight.get()
            createpat(f_name,l_name,a,pw_d,con_pwd,mob,email,gender,wei_ght)
            messagebox.showinfo("showinfo","Registered Successfully Now you can login",parent=window12 )

    tk.Label(window12,text="SIGN UP",width="20",font=("bold",20),bg="lightblue").place(x=63,y=31)
    tk.Label(window12,text="",bg="lightblue").pack()
    tk.Label(window12,text="FirstName",width="20",font=("bold",10),bg="lightblue").place(x=70,y=88)
    tk.Entry(window12,textvariable=firstname).place(x=200,y=88)
    tk.Label(window12,text="LastName",width="20",font=("bold",10),bg="lightblue").place(x=70,y=128)
    tk.Entry(window12,textvariable=lastname).place(x=200,y=128)
    tk.Label(window12,text="Age",width="20",font=("bold",10),bg="lightblue").place(x=80,y=168)
    tk.Entry(window12,textvariable=age).place(x=200,y=168)
    tk.Label(window12,text="Password",width="20",font=("bold",10),bg="lightblue").place(x=70,y=208)
    tk.Entry(window12,textvariable=pwd).place(x=200,y=208)
    tk.Label(window12,text="Confirm Password",width="20",font=("bold",10),bg="lightblue").place(x=50,y=248)
    tk.Entry(window12,textvariable=confirmpwd).place(x=200,y=248)
    tk.Label(window12,text="Mobile",width="20",font=("bold",10),bg="lightblue").place(x=76,y=288)
    tk.Entry(window12,textvariable=mobile).place(x=200,y=288)
    tk.Label(window12,text="EmailID",width="20",font=("bold",10),bg="lightblue").place(x=75,y=328)
    tk.Entry(window12,textvariable=EmailID).place(x=200,y=328)
    tk.Label(window12,text="Gender",width="20",font=("bold",10),bg="lightblue").place(x=76,y=368)
    tk.Radiobutton(window12,text="Male",variable=g,value=1,bg="lightblue").place(x=200,y=368)
    tk.Radiobutton(window12,text="Female",variable=g,value=2,bg="lightblue").place(x=250,y=368)
    tk.Label(window12,text="Weight(inKgs)",width="20",font=("bold",10),bg="lightblue").place(x=55,y=403)
    tk.Entry(window12,textvariable=weight).place(x=200,y=403)
    tk.Button(window12,text="SUBMIT",fg="white",bg="blue",height="2",width="20",command=getvalues).place(x=55,y=443)
    tk.Button(window12,text="LOGIN",fg="white",bg="blue",height="2",width="20",command=login2).place(x=245,y=443)
    window12.mainloop()
c=None
def login2():
    window13=tk.Tk()
    window13.title("Login")
    window13.geometry("200x270")
    window13.configure(bg="lightblue")
    emailid=tk.StringVar(window13)
    pwd=tk.StringVar(window13)
    global listofpats

    def getdetails():
        EmailID=emailid.get()
        password=pwd.get()
        global listofpats
        m=1
        for i in listofpats:
            if(i.EmailID==EmailID and i.confirmpwd==password):
                m=0
                break
        global c
        c=i
        if(m==0):
            messagebox.showinfo("showinfo","Login Successful Now you can book appointment" ,parent=window13)
        else:
            messagebox.showinfo("showinfo","invalid password and emailid",parent=window13)
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Label(window13,text="LOGIN",width="20",font=("bold",10),bg="lightblue").pack()
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Label(window13,text="EmailID",width="20",font=("bold",10),bg="lightblue").pack()
    tk.Entry(window13,textvariable=emailid).pack()
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Label(window13,text="Password",width="20",font=("bold",10),bg="lightblue").pack()
    tk.Entry(window13,textvariable=pwd).pack()
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Button(window13,text="LOGIN",bg="blue",fg="white",height="2",width="10",command=getdetails).place(x=20,y=200)
    tk.Button(window13,text="BOOK",bg="blue",fg="white",height="2",width="10",command=lambda:displaydetails(c)).place(x=110,y=200)
    window13.mainloop()
def register1():
    window12=tk.Tk()
    window12.title("Signup")
    window12.geometry("500x500")
    window12.configure(bg="lightblue")
    firstname=tk.StringVar(window12)
    lastname=tk.StringVar(window12)
    licenseID_no=tk.StringVar(window12)
    pwd=tk.StringVar(window12)
    confirmpwd=tk.StringVar(window12)
    mobile=tk.StringVar(window12)
    EmailID=tk.StringVar(window12)
    g=tk.IntVar(window12)
    specialization=tk.StringVar(window12)
    def getvalues():
            gen=['0','Male','Female']
            f_name=firstname.get()
            l_name=lastname.get()
            l_id=licenseID_no.get()
            pw_d=pwd.get()
            con_pwd=confirmpwd.get()
            mob=mobile.get()
            email=EmailID.get()
            gender=gen[g.get()]
            special_ize=specialization.get()
            createdoc(f_name,l_name,l_id,pw_d,con_pwd,mob,email,gender,special_ize)
            messagebox.showinfo("showinfo","Registered Successfully Now you can login",parent=window12)

    tk.Label(window12,text="SIGN UP",width="20",font=("bold",20),bg="lightblue").place(x=63,y=31)
    tk.Label(window12,text="",bg="lightblue").pack()
    tk.Label(window12,text="FirstName",width="20",font=("bold",10),bg="lightblue").place(x=70,y=88)
    tk.Entry(window12,textvariable=firstname).place(x=200,y=88)
    tk.Label(window12,text="LastName",width="20",font=("bold",10),bg="lightblue").place(x=70,y=128)
    tk.Entry(window12,textvariable=lastname).place(x=200,y=128)
    tk.Label(window12,text="LicenseID Number",width="20",font=("bold",10),bg="lightblue").place(x=50,y=168)
    tk.Entry(window12,textvariable=licenseID_no).place(x=200,y=168)
    tk.Label(window12,text="Password",width="20",font=("bold",10),bg="lightblue").place(x=70,y=208)
    tk.Entry(window12,textvariable=pwd).place(x=200,y=208)
    tk.Label(window12,text="Confirm Password",width="20",font=("bold",10),bg="lightblue").place(x=50,y=248)
    tk.Entry(window12,textvariable=confirmpwd).place(x=200,y=248)
    tk.Label(window12,text="Mobile",width="20",font=("bold",10),bg="lightblue").place(x=76,y=288)
    tk.Entry(window12,textvariable=mobile).place(x=200,y=288)
    tk.Label(window12,text="EmailID",width="20",font=("bold",10),bg="lightblue").place(x=75,y=328)
    tk.Entry(window12,textvariable=EmailID).place(x=200,y=328)
    tk.Label(window12,text="Gender",width="20",font=("bold",10),bg="lightblue").place(x=76,y=368)
    tk.Radiobutton(window12,text="Male",variable=g,value=1,bg="lightblue").place(x=200,y=368)
    tk.Radiobutton(window12,text="Female",variable=g,value=2,bg="lightblue").place(x=250,y=368)
    tk.Label(window12,text="Specialization",width="20",font=("bold",10),bg="lightblue").place(x=55,y=403)
    lspecial=['physician','gynaec','Pulmonary','Gastro','Cardio']
    droplist=tk.OptionMenu(window12,specialization,*lspecial)
    droplist.config(bg="lightblue",width="16")
    specialization.set("select")
    droplist.place(x=200,y=403)
    tk.Button(window12,text="SUBMIT",fg="white",bg="blue",height="2",width="20",command=getvalues).place(x=55,y=443)
    tk.Button(window12,text="LOGIN",fg="white",bg="blue",height="2",width="20",command=login1).place(x=245,y=443)
    window12.mainloop()
b=None
def login1():
    window13=tk.Tk()
    window13.title("Login")
    window13.geometry("200x270")
    window13.configure(bg="lightblue")
    emailid=tk.StringVar(window13)
    pwd=tk.StringVar(window13)
    def getdetails():
        EmailID=emailid.get()
        password=pwd.get()
        global listofdocs
        k=1
        for i in listofdocs:
            if(i.EmailID==EmailID and i.confirmpwd==password):
                k=0
                break
        global b
        b=i
        if k==0:
            messagebox.showinfo("showinfo","Login Successful Now you can view appointment",parent=window13 )
        else:
            messagebox.showinfo("showinfo","invalid password and emailid",parent=window13)
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Label(window13,text="LOGIN",width="20",font=("bold",10),bg="lightblue").pack()
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Label(window13,text="EmailID",width="20",font=("bold",10),bg="lightblue").pack()
    tk.Entry(window13,textvariable=emailid).pack()
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Label(window13,text="Password",width="20",font=("bold",10),bg="lightblue").pack()
    tk.Entry(window13,textvariable=pwd).pack()
    tk.Label(window13,text="",bg="lightblue").pack()
    tk.Button(window13,text="LOGIN",bg="blue",fg="white",height="2",width="10",command=getdetails).place(x=20,y=200)
    tk.Button(window13,text="VIEW",bg="blue",fg="white",height="2",width="10",command=lambda:displaydetailsofpat(b)).place(x=110,y=200)
    window13.mainloop()
def Note1(login, register, name):
    window1=tk.Tk()
    window1.title(name)
    window1.geometry("300x150")
    window1.configure(bg="lightblue")
    tk.Label(window1,text="",bg="lightblue").pack()
    tk.Button(window1,text="Login",height="2",width="30",command=login).pack()
    tk.Label(window1,text="",bg="lightblue").pack()
    tk.Button(window1,text="register",height="2",width="30",command=register).pack()
    window1.mainloop()
def mainscreen():
    global window
    window=tk.Tk()
    window.title("PACTO")
    window.geometry("300x250")
    window.configure(background="lightblue")
    label=tk.Label(window,text="WELCOME TO PACTO APPLICATION",fg="black",bg="lightblue").pack()
    tk.Label(window,text="",bg="lightblue").pack()
    tk.Button(window,text="About",bg="green",fg="black",height="2",width="15",command=about).pack()
    tk.Label(window,text="",bg="lightblue").pack()
    doctor=tk.Button(window,text="DOCTOR",fg="white",bg="red",height="2",width="30",command=lambda: Note1(login1,register1, "DoctorLogin")).pack()
    tk.Label(window,text="",bg="lightblue").pack()
    patient=tk.Button(window,text="PATIENT",fg="black",bg="blue",height="2",width="30",command=lambda: Note1(login2,register2, "PatientLogin")).pack()
    window.mainloop()
mainscreen()
