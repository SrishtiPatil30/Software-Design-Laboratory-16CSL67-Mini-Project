# -*- coding: cp1252 -*-
from Tkinter import *
import MySQLdb
import Tkinter
import tkMessageBox
from datetime import datetime

db=MySQLdb.connect("localhost","root","","ngo")
cr=db.cursor()

def donate():
    try:
        window.destroy()
    except:
        """DO NOTHING"""
    def insert_donate():
        address = entry_address.get()
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')

        if(item.get()==1):
            item_name="Toys"
        elif(item.get()==2):
            item_name="Clothes"
        elif (item.get() == 3):
            item_name = "Health"
        elif (item.get() == 4):
            item_name = "Elders"
        elif (item.get() == 5):
            item_name = "Education"
        else:
            item_name = "Food"

        if(pick.get()==1):
            pickup="come to organization"
        else:
            pickup = "pick from address"

        i=("insert into donated(user,address,donation_type,date_donated) values(%s,%s,%s,%s)")
        v=(userid,address,pickup,date)
        cr.execute(i,v)
        db.commit()
        tkMessageBox.showinfo("Info","Donation successfull!")
        donar_screen()
        
    global donate_window
    donate_window=Tk()
    donate_window.title("Donate")

    donate_window.geometry('500x500')
    donate_window.configure(background="white");

    item = IntVar()
    address=StringVar()
    pick = IntVar()

    Label(donate_window,text="What do you want to donate?", bg="white",width="150", height="2", font=("Calibri 15 bold")).pack()
    Label(text="").pack()
    Radiobutton(donate_window, text="  Toys   ", variable=item,value=1, indicator=0,background="light blue",padx=35,pady=15).place(x=70, y=80)
    Radiobutton(donate_window, text=" Clothes ", variable=item,value=2, indicator=0,background="light blue",padx=35,pady=15).place(x=188, y=80)
    Radiobutton(donate_window, text=" Health  ", variable=item, value=3, indicator=0, background="light blue", padx=35,pady=15).place(x=314, y=80)
    Radiobutton(donate_window, text=" Elders  ", variable=item,value=4, indicator=0,background="light blue",padx=34,pady=15).place(x=70, y=135)
    Radiobutton(donate_window, text="Education", variable=item,value=5, indicator=0,background="light blue",padx=32,pady=15).place(x=188, y=135)
    Radiobutton(donate_window, text="  Food   ", variable=item, value=6, indicator=0, background="light blue", padx=35,pady=15).place(x=315, y=135)

    enteraddress = Label(donate_window, text="Address", font=("bold", 10), bg="white")
    enteraddress.place(x=80, y=230)
    entry_address = Entry(donate_window, textvariable=address, width=30)
    entry_address.place(x=150, y=230)

    info = Label(donate_window, text="How we collect your donation?", font=("bold", 10), bg="white")
    info.place(x=80, y=290)
    Radiobutton(donate_window, text="I'll come to the organization", variable=pick,value=1,background="white").place(x=90, y=320)
    Radiobutton(donate_window, text="Pick it up from my address", variable=pick,value=2,background="white").place(x=90, y=340)
    Button(donate_window, text="Donate", background="green",foreground="white",command=insert_donate,font=("bold",12)).place(x=190, y=400)
    Button(donate_window, text="Cancel", background="red", foreground="white",command=donar_screen, font=("bold", 12)).place(x=270, y=400)
    donate_window.mainloop()


def update():
    try:
        window.destroy()
    except:
        """DO NOTHING"""

    def update_profile():
        n=fullname_entry.get()
        u=username_entry.get()
        p=phonenumber_entry.get()
        ps=passwd_entry.get()

        q = ("update donars set name=%s, username=%s, phone=%s, password=%s where username=%s")
        val = (n, u, p, ps, userid)
        cr.execute(q,val)
        db.commit()
        
        tkMessageBox.showinfo("Info","Profile Updated Successfully!")
        update_window.destroy()
        donar_screen()


    global update_window

    sql = ("select * from donars where username=%s")
    cr.execute(sql,(userid,))
    results = cr.fetchall()
    for row in results:
        fullname=row[0]
        name=row[1]
        phone=row[2]
        email=row[3]
        pwd=row[4]
    qname=fullname
    quname=name
    qphone=phone
    qpwd=pwd
    

    update_window=Tk()
    update_window.title("Update profile")

    update_window.geometry('500x500')
    update_window.configure(background="white");

    heading = Label(update_window, text="Update Profile", width=20, bg="white", font=("bold", 20)).place(x=70, y=50)

    fullname = Label(update_window, text="Fullname",bg="white",font=("bold", 10)).place(x=60,y=130)
    fullname_entry = Entry(update_window)
    fullname_entry.insert(10,qname)
    fullname_entry.place(x=210,y=130)


    username = Label(update_window, text="Username",bg="white",font=("bold", 10)).place(x=60,y=170)
    username_entry = Entry(update_window)
    username_entry.insert(10,quname)
    username_entry.place(x=210,y=170)


    phonenumber = Label(update_window, text="Phone",bg="white",font=("bold", 10)).place(x=60,y=210)
    phonenumber_entry = Entry(update_window)
    phonenumber_entry.insert(10,qphone)
    phonenumber_entry.place(x=210,y=210)


    passwd = Label(update_window, text="Password",bg="white",font=("bold", 10)).place(x=60,y=250)
    passwd_entry = Entry(update_window,show="*")
    passwd_entry.insert(10,qpwd)
    passwd_entry.place(x=210,y=250)

    Button(update_window, text="Update",background="green", foreground="white",command=update_profile, font=("bold", 12)).place(x=180, y=300)
    Button(update_window, text="Cancel",background="red", foreground="white",command=donar_screen, font=("bold", 12)).place(x=260, y=300)

    update_window.mainloop()
    
def viewevents():
    try:
        window.destroy()
    except:
        """DO NOTHING"""
   
    global view_donor

    view_donor=Tkinter.Tk()
    view_donor.geometry("1600x750")
    
    try:
        Label(view_donor,text="Date", bg="#3C66EE", fg="white",font=('Helvetica', 12, 'bold')).grid(row=0,column=0)
        Label(view_donor,text="Event Name", bg="#3C66EE", fg="white",font=('Helvetica', 12, 'bold')).grid(row=0,column=1)
        Label(view_donor,text="Event Description", bg="#3C66EE", fg="white",font=('Helvetica', 12, 'bold')).grid(row=0,column=2)
        
        sql="select * from events"
        cr.execute(sql)
        data=cr.fetchall()
        c=len(data)
        rows = []
        for i in range(0,c):
            cols = []
            for j in range(0,3):
                e = Entry(view_donor,relief=RIDGE,width=27,justify='center')
                e.grid(row=i+1, column=j, sticky=NSEW)
                e.insert(END,data[i][j])
                cols.append(e)
                e.config(state=DISABLED)
            rows.append(cols)
    except:
        tkMessageBox.showinfo("message","ERROR IN DATABASE")
    Button(view_donor,text="GO BACK",command=donar_screen).grid(row=2000,column=2)
    
def donar_screen():
    try:
        view_donor.destroy()
    except:
        """DO NOTHING"""
    try:
        index.destroy()
    except:
        """DO NOTHING"""
    try:
        update_window.destroy()
    except:
        """DO NOTHING"""
    try:
        donate_window.destroy()
    except:
        """DO NOTHING"""
    try:
        donar_login.destroy()
    except:
        """DO NOTHING"""

    global window

    window=Tk()
    window.title("Donation")

    window.geometry('500x500')
    window.configure(background="white");

    Label(window, text="Donate", bg="blue", fg="White", width="150", height="2", font=("Calibri 20 bold")).pack()
    Label(text="").pack()

    Button(window, text="Donate", height="2", width="30", command=donate).pack()
    Label(text="").pack()

    Button(window, text="Events", height="2", width="30", command=viewevents).pack()
    Label(text="").pack()

    Button(window, text="Update profile", height="2", width="30", command=update).pack()
    Label(text="").pack()

    Button(window, text="Logout", command=main, bg="red", fg="white", font=("bold",12)).pack()

    window.mainloop()

def verifydonarlogin():
    global userid
    username_info = username_entry.get()
    password_info = password_entry.get()
    try:
        query = ('select username,password from donars')
        cr.execute(query)
        results = cr.fetchall()
        for row in results:
            user=row[0]
            password=row[1]
            if username_info == user and password_info == password:
                login = True
                break
            else:
                login = False

        if login == True:
            userid=username_info
            tkMessageBox.showinfo("Info", "login successfull")
            donar_screen()    
        else:
            tkMessageBox.showinfo("Info", "Username or password invalid, please try again")

    except:
        tkMessageBox.showinfo("Error:", "Cannot Login")
        db.rollback()



def donarlogin():

    try:
        window.destroy()
    except:
        """DO NOTHING"""

    global username_entry
    global password_entry
    global donar_login
      
    donar_login=Toplevel(index)
    donar_login.geometry("350x350")
     
    username = StringVar()
    password = StringVar()

    Label(donar_login, text="Please Enter Donor Details", bg="blue", fg="white",width="300", height="2", font=("Calibri 20 bold")).pack()
    Label(donar_login, text="").pack()

    username_lable = Label(donar_login, text="Username",font=("Calibri 15 bold"))
    username_lable.pack()

    username_entry = Entry(donar_login, textvariable=username)
    username_entry.pack()

    password_lable = Label(donar_login, text="password",font=("Calibri 15 bold"))
    password_lable.pack()
    password_entry = Entry(donar_login, textvariable=password, show='*')
    password_entry.pack()

    Label(donar_login, text="").pack()
    username_entry.focus()
    Button(donar_login, text="Login", width=10, height=1, bg="blue",fg="white" ,font=("Calibri 15 bold"),command=verifydonarlogin).pack()
  
    donar_login.mainloop()

def validate_user(donar_user):
    cr = db.cursor()
    query = ("select * from donars")
    cr.execute(query)
    results = cr.fetchall()
    for row in results:
        name = row[1]
        if name != donar_user:
            return True
        else:
            return False
    db.close()

def validate_phone(donar_phone):
    if donar_phone.isdigit():
        return True
    else:
        tkMessageBox.showinfo('error','Please enter a valid phone number')
        return False

def validate_email(donar_email):
    if len(donar_email)>7:
        if re.match("^.+@(\[?)[a-zA-Z0-9]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", donar_email) !=None:
            return True
        return False
    else:
        tkMessageBox.showinfo('error','Please enter a valid email address')
        return False

def validate_info():
    if entry_fullname.get()=="":
        tkMessageBox.showinfo('Info','Please enter your Full-name')
        entry_fullname.focus()
        
    elif entry_donarname.get()=="":
        tkMessageBox.showinfo('Info','Please enter your username')
        entry_donarname.focus()
        
    elif entry_phonenumber.get()=="":
        tkMessageBox.showinfo('Info','Please enter your phone number')
        entry_phonenumber.focus()
        
    elif len(entry_phonenumber.get())!=10:
        tkMessageBox.showinfo('Info', 'Please enter a 10 digit phone number')
        
    elif entry_emailID.get()=="":
        tkMessageBox.showinfo('Info','Please enter your email id')
        entry_emailID.focus()
        
    elif entry_password.get()=="":
        tkMessageBox.showinfo('Info','Please enter a password')
        entry_password.focus()
        
    elif entry_confirmpassword.get() == "":
        tkMessageBox.showinfo('Info', 'Please confirm password to proceed')
        entry_confirmpassword.focus()
        
    elif entry_password.get()!=entry_confirmpassword.get():
        tkMessageBox.showinfo('Info','Password mismatch')
        entry_confirmpassword.delete(0,END)
        entry_confirmpassword.focus()
        
    elif entry_emailID.get()!="":
        status=validate_email(entry_emailID.get())
        if(status):
            if(validate_user(entry_donarname.get())):
                cr = db.cursor()
                sql = ("insert into donars(name,username,phone,email,password) values(%s,%s,%s,%s,%s)")
                val = (entry_fullname.get(),entry_donarname.get(), entry_phonenumber.get(), entry_emailID.get(), entry_password.get())
                cr.execute(sql, val)
                db.commit()
                tkMessageBox.showinfo('Info','Registered Successfully')
                window.destroy()
            else:
                tkMessageBox.showinfo('error','Username already exists')
                entry_donarname.delete(0,END)
                entry_donarname.focus()
            


def donor_registration():
    global window
    global entry_fullname,entry_donarname,entry_phonenumber,entry_emailID,entry_password,entry_confirmpassword
    window=Toplevel(index)
    window.title("Donar Registration")

    window.geometry('500x500')
    window.configure(background="white");
    fullname=StringVar()
    fname=StringVar()
    phoneno=StringVar()
    email=StringVar()
    pwd=StringVar()
    confirmpwd=StringVar()

    heading=Label(window,text="Donar Registration",width=20, font=("bold",20),bg="white")
    heading.place(x=90,y=53)

    fullname=Label(window,text="Full-name",width=20, font=("bold",10),bg="white")
    fullname.place(x=80,y=130)
    entry_fullname=Entry(window, textvariable=fullname)
    entry_fullname.place(x=240,y=130)

    donarname=Label(window,text="Username",width=20, font=("bold",10),bg="white")
    donarname.place(x=80,y=170)
    entry_donarname=Entry(window, textvariable=fname)
    entry_donarname.place(x=240,y=170)

    phonenumber=Label(window,text="Phone No.",width=20, font=("bold",10),bg="white")
    phonenumber.place(x=80,y=210)
    entry_phonenumber=Entry(window, textvariable=phoneno)
    entry_phonenumber.place(x=240,y=210)
    valid_phonenumber=window.register(validate_phone)
    entry_phonenumber.config(validate="key", validatecommand=(valid_phonenumber, '%P'))

    emailID=Label(window,text="Email ID",width=20, font=("bold",10),bg="white")
    emailID.place(x=80,y=250)
    entry_emailID=Entry(window, textvariable=email)
    entry_emailID.place(x=240,y=250)


    password=Label(window,text="Password",width=20, font=("bold",10),bg="white")
    password.place(x=80,y=290)
    entry_password=Entry(window, show='*', textvariable=pwd)
    entry_password.place(x=240,y=290)

    confirmpassword=Label(window,text="Confirm password",width=20, font=("bold",10),bg="white")
    confirmpassword.place(x=80,y=330)
    entry_confirmpassword=Entry(window, show='*', textvariable=confirmpwd)
    entry_confirmpassword.place(x=240,y=330)
    entry_fullname.focus()
    register_button=Button(window, text="Register", command=validate_info, bg="dark green", fg="white", font=("bold",10)).place(x=250, y=380)

    window.mainloop()


    
def event_inserting():
    evedesc=desc.get("1.0","end-1c")
    try:
        if evename.get()=="":
            tkMessageBox.showinfo('Info','Please Enter Event Name')
            evename.focus()
        elif evedesc=="":
            tkMessageBox.showinfo('Info','Please enter Event description')
            desc.focus()
        else:
            sql='insert into events values(%s,%s,%s)'
            cr.execute(sql, (evedate.get(), evename.get() ,evedesc ))
            cr.execute("commit")
            tkMessageBox.showinfo('Info','Inserted Successfully')
            eve_add.destroy()
            adminpage()
            
    except:
            tkMessageBox.showinfo('info','Cannot insert in database')
      
def addevent():
    try:
        admin_screen.destroy()
    except:
        """DO NOTHING"""
    global eve_add
    global datevar,eve_name,eve_desc
    global evedate,evename,desc
    eve_add=Tk()
    eve_add.geometry("550x500")
     
    eve_name=StringVar()
    eve_desc=StringVar()
    datevar=StringVar()
      
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    label1= Label(eve_add, text="Add Events",width=20,font=("bold", 20)).place(x=90,y=53)

    label2 = Label(eve_add, text="Date",width=20,font=("bold", 10)).place(x=80,y=130)
    evedate = Entry(eve_add,textvar=datevar)
    evedate.insert(10,formatted_date)
    evedate.config(state=DISABLED)
    evedate.place(x=240,y=130)
         
    label3 = Label(eve_add, text="Name",width=20,font=("bold", 10)).place(x=68,y=180)
    evename = Entry(eve_add,textvar=eve_name)
    evename.place(x=240,y=180)

    label4 = Label(eve_add, text="Description",width=20,font=("bold", 10)).place(x=70,y=230)
    desc = Text(eve_add,height=5,width=30)
    desc.place(x=240,y=230)
      
    Button(eve_add, text='Submit',width=20,bg='brown',fg='white',command=event_inserting).place(x=120,y=340)
    Button(eve_add, text='GO BACK',width=20,bg='brown',fg='white',command=adminpage).place(x=240,y=340)
    eve_add.mainloop()

      
def viewdonorlist():
    try:
        admin_screen.destroy()
    except:
        """DO NOTHING"""
   
    global view_donor

    view_donor=Tkinter.Tk()
    view_donor.geometry("1600x750")
    
    try:
        sql1="SELECT COLUMN_NAME FROM  `INFORMATION_SCHEMA`.`COLUMNS` WHERE TABLE_NAME =  'donars'"
        cr.execute(sql1)
        d=cr.fetchall()
        for i in range(0,5):
            Label(view_donor,text=d[i], bg="#3C66EE", fg="white",font=('Helvetica', 12, 'bold')).grid(row=0,column=i)
        sql="select * from donars"
        cr.execute(sql)
        data=cr.fetchall()
        c=len(data)
        rows = []
        for i in range(0,c):
            cols = []
            for j in range(0,5):
                e = Entry(view_donor,relief=RIDGE,width=27,justify='center')
                e.grid(row=i+1, column=j, sticky=NSEW)
                e.insert(END,data[i][j])
                cols.append(e)
                e.config(state=DISABLED)
            rows.append(cols)
    except:
        tkMessageBox.showinfo("message","ERROR IN DATABASE")
    Button(view_donor,text="GO BACK",command=adminpage).grid(row=2000,column=2)
    

def donorlilst():
    mail=donormail.get()

    if mail=="":
        tkMessageBox.showinfo("message","Please enter the email")
        donormail.delete(0,END)
        donormail.focus()    
    else:
        
        sql ="select * from donars where email=%s"
        cr.execute(sql,(mail,))
        data=cr.fetchall()
      
        if len(data)==1:
            global select_dnr
            select_dnr=Tkinter.Tk()
            select_dnr.geometry("500x500")
            Label(select_dnr,text="Donar Id",font="Times 14 bold").grid(row=1)
            Label(select_dnr,text="name",font="Times 14 bold").grid(row=2)
            Label(select_dnr,text="Mail Id",font="Times 14 bold").grid(row=3)
            Label(select_dnr,text="Phone No.",font="Times 14 bold").grid(row=4)
            Label(select_dnr,text="Address",font="Times 14 bold").grid(row=5)
        
        
            did=Entry(select_dnr)
            name=Entry(select_dnr)
            mail=Entry(select_dnr)
            phone=Entry(select_dnr)
            address=Entry(select_dnr)
                
            did.insert(1,data[0][0])
            did.config(state=DISABLED)
            name.insert(2,data[0][1])
            name.config(state=DISABLED)
            mail.insert(3,data[0][2])
            mail.config(state=DISABLED)
            phone.insert(2,data[0][3])
            phone.config(state=DISABLED)
            address.insert(3,data[0][4])
            address.config(state=DISABLED)
            
                
            did.grid(row=1,column=5)
            name.grid(row=2,column=5)
            mail.grid(row=3,column=5)
            phone.grid(row=4,column=5)
            address.grid(row=5,column=5)
            q=Button(select_dnr,text="OK",command=searchdonorlist).grid(row=6,column=1)

        else:
            tkMessageBox.showinfo("message","No donor exists")
            donormail.delete(0,END)
            donormail.focus()
            
            
        


def searchdonorlist():
    global search_donor,donormail
    try:
        search_donor.destroy()
    except:
        """DO NOTHING"""
    try:
        admin_screen.destroy()
    except:
        """DO NOTHING"""
    try:
        select_dnr.destroy()
    except:
        """DO NOTHING"""

    search_donor=Tkinter.Tk()
    search_donor.geometry("1600x750")

    Label(search_donor,text="Donar mail Id",font="ariel 15 bold").grid(row=1)

    donormail=Entry(search_donor)
    donormail.grid(row=1,column=1)
    
    
    
    Button(search_donor,text="Enter",command=donorlilst).grid(row=2,column=1)
    Button(search_donor,text="GO BACK",command=adminpage).grid(row=2,column=2)

def viewdonations():
    try:
        admin_screen.destroy()
    except:
        """DO NOTHING"""
   
    global view_donor

    view_donor=Tkinter.Tk()
    view_donor.geometry("1600x750")
    
    try:
        sql1="SELECT COLUMN_NAME FROM  `INFORMATION_SCHEMA`.`COLUMNS` WHERE TABLE_NAME =  'donated'"
        cr.execute(sql1)
        d=cr.fetchall()
        for i in range(0,4):
            Label(view_donor,text=d[i], bg="#3C66EE", fg="white",font=('Helvetica', 12, 'bold')).grid(row=0,column=i)
        sql="select * from donated"
        cr.execute(sql)
        data=cr.fetchall()
        c=len(data)
        rows = []
        for i in range(0,c):
            cols = []
            for j in range(0,4):
                e = Entry(view_donor,relief=RIDGE,width=27,justify='center')
                e.grid(row=i+1, column=j, sticky=NSEW)
                e.insert(END,data[i][j])
                cols.append(e)
                e.config(state=DISABLED)
            rows.append(cols)
    except:
        tkMessageBox.showinfo("message","ERROR IN DATABASE")
    Button(view_donor,text="GO BACK",command=adminpage).grid(row=2000,column=2)


def adminpage():
    try:
        eve_add.destroy()
    except:
        """DO NOTHING"""
    try:
        view_donor.destroy()
    except:
        """DO NOTHING"""
    try:
        search_donor.destroy()
    except:
        """DO NOTHING"""

    global admin_screen
    admin_screen=Tkinter.Tk()
    admin_screen.geometry("1600x750")
    Label(admin_screen,text="Admin Page", bg="blue", fg="White",width="150", height="2", font=("Calibri 20 bold")).pack() 
    Label(text="").pack()
     
    
    Button(admin_screen,text="View Donor", height="2", width="30",command=viewdonorlist).pack()
    Label(text="").pack()
      
    Button(admin_screen,text="Search Donor", height="2", width="30",command=searchdonorlist).pack()
    Label(text="").pack()
      
    Button(admin_screen,text="Events", height="2", width="30",command=addevent).pack()
    Label(text="").pack()

    Button(admin_screen,text="View Donations", height="2", width="30",command=viewdonations).pack()
    Label(text="").pack()
     
               
    q=Tkinter.Button(admin_screen,width=15,height="2",text="LOGOUT",command=main).pack()

    admin_screen.mainloop()
   

      
def verifyadminlogin():
      username_info=username_entry.get()
      password_info=password_entry.get()
      try:
            sql="select * from admin"
            cr.execute(sql)
            data=cr.fetchall()
            z=0
            k=0
            for i in data:
                z=z+1
            for i in data:
                k=k+1
                if (username_info== i[0]):
                    if(password_info!=i[1]):
                        tkMessageBox.showinfo("Error:","Wrong Password!!!")
                        password_entry.delete(0,END)
                        password_entry.focus()
                    elif(password_info==i[1]):
                        k=k-1
                        tkMessageBox.showinfo("MessageBox","login succsseful")
                        index.destroy()
                        adminpage()
                        
                elif(username_info!=i[0] and k==z):
                    tkMessageBox.showinfo("Error:","User Doesn't Exist")
                    username_entry.delete(0,END)
                    password_entry.delete(0,END)
                    username_entry.focus()
                
          
      except:
            tkMessageBox.showinfo("Error:","Cannot Login")
            db.rollback()
    



def adminlogin():
      global username_entry
      global password_entry
      global admin_login
      
      admin_login=Toplevel(index)
      admin_login.geometry("350x350")
     
      username = StringVar()
      password = StringVar()

      Label(admin_login, text="Please Enter Admin Details", bg="blue", fg="white",width="300", height="2", font=("Calibri 20 bold")).pack()
      Label(admin_login, text="").pack()

      username_lable = Label(admin_login, text="Username",font=("Calibri 15 bold"))
      username_lable.pack()

      username_entry = Entry(admin_login, textvariable=username)
      username_entry.pack()

      password_lable = Label(admin_login, text="password",font=("Calibri 15 bold"))
      password_lable.pack()

      password_entry = Entry(admin_login, textvariable=password, show='*')
      password_entry.pack()
      Label(admin_login, text="").pack()
      username_entry.focus()
      Button(admin_login, text="Login", width=10, height=1, bg="blue",fg="white" ,font=("Calibri 15 bold"),command=verifyadminlogin).pack()
  
      admin_login.mainloop()

def aboutus():
    try:
        index.destroy()
    except:
        """DO NOTHING"""
    global about
    about=Tkinter.Tk()
    about.geometry("1600x750")
    

    Label(about,text="Sparsh Foundation", bg="blue", fg="White",width="150", height="2", font=("Calibri 20 bold")).pack()
    Label(text="").pack()
    describe1="Hope for Children is an international charity working towards a world in which every child has the happy,\n healthy and positive childhood we passionately believe they deserve.\n\n"
    describe2="Almost half the world’s children live in extreme poverty. We are helping to change this by delivering \n education, health, livelihoods and Child Rights projects that benefit thousands of children each year.\n\n"
    describe3="Changing the lives of children is a continuous process. Nothing can be done in a limited period.\n As individuals we have to continue to give support by way of financial help, time as well as other resources.\n\n"
    describe4="I have always believed in and I stand for child rights because it is absolutely unreal and unthinkable to imagine a child being treated poorly. \nThey bring happiness to you and its important that all of us be responsible and make sure we give back the happiness back to them.\n Nobody in this world has got the right to treat them poorly.\n\n"
    label = Label(about, text =describe1,font=('arial', 15, 'bold')) 
    label.pack(side = TOP)

    label = Label(about, text =describe2,font=('arial', 15, 'bold')) 
    label.pack(side = TOP)

    label = Label(about, text =describe3,font=('arial', 15, 'bold')) 
    label.pack(side = TOP) 

    label = Label(about, text =describe4,font=('arial', 15, 'bold')) 
    label.pack(side = TOP)

    Button(about, text='GO BACK',width=20,bg='brown',fg='white',command=main).pack(side = TOP)

    about.mainloop()

def main():
    
    try:
        about.destroy()
    except:
        """DO NOTHING"""
    try:
        window.destroy()
    except:
        """DO NOTHING"""
    try:
        admin_screen.destroy()
    except:
        """DO NOTHING"""
    global index
    index=Tkinter.Tk()
    index.geometry("1600x750")
    Label(index,text="Home Page", bg="blue", fg="White",width="150", height="2", font=("Calibri 20 bold")).pack()
    Label(text="").pack()
    Button(index,text="Admin Login", height="2", width="30",command=adminlogin).pack()
    Label(text="").pack()
    Button(index,text="Donor registration", height="2", width="30",command=donor_registration).pack()
    Label(text="").pack()
    Button(index,text="Donor Login", height="2", width="30",command=donarlogin).pack()
    Label(text="").pack()
    Button(index,text="About us", height="2", width="30",command=aboutus).pack()
    Label(text="").pack()
    index.mainloop()
main()  
