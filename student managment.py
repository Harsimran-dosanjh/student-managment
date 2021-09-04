from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
import time


def add():
    def submitadd():
        rool = roolval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        adddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (rool, name, mobile, email, address, gender, dob, adddate))
            con.commit()
            msg = messagebox.askyesnocancel('added notification',
                                            'data of rool = {} and name = {} is successfully added... do you want clean form '.format(
                                                rool, name), master=root)
            if msg == True:
                roolval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('rool = {} and name ={} is already exist'.format(rool, name))
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        data = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            studenttable.insert('', END, values=vv)

    root = Toplevel(master=DataEntryFrame)
    root.geometry('500x600')
    root.config(bg='cyan')
    root.title('add student data')
    # root.grab_set()
    root.resizable(False, False)

    root.iconbitmap('logo.ico')
    addlabel = Label(root, text='Add Student Data', bg='gold2', width=25, font=('calibri', 19, 'bold'), bd=5,
                     relief=RIDGE)
    addlabel.place(x=90, y=0)
    welcomelabel = Label(root, bg='cyan', text='----------------------Enter data----------------------',
                         font=('Ariel', 17, 'bold'))
    welcomelabel.place(x=10, y=50)
    rollnolabel = Label(root, bg='pink', text='Enter rollno.', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    rollnolabel.place(x=20, y=100)
    namelabel = Label(root, bg='pink', text='Enter Name', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                      bd=5, activebackground='blue', activeforeground='white', anchor='w')
    namelabel.place(x=20, y=160)
    mobilelabel = Label(root, bg='pink', text='Enter mobile', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    mobilelabel.place(x=20, y=220)
    emaillabel = Label(root, bg='pink', text='Enter email', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                       bd=5, activebackground='blue', activeforeground='white', anchor='w')
    emaillabel.place(x=20, y=280)
    addresslabel = Label(root, bg='pink', text='Enter address', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                         bd=5, activebackground='blue', activeforeground='white', anchor='w')
    addresslabel.place(x=20, y=340)
    genderlabel = Label(root, bg='pink', text='Enter gender', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    genderlabel.place(x=20, y=400)
    doblabel = Label(root, bg='pink', text='Enter D.O.B', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                     bd=5, activebackground='blue', activeforeground='white', anchor='w')
    doblabel.place(x=20, y=460)

    submitbutton = Button(root, text='Submit', font=('roman', 15, 'bold'), bg='dark violet', bd=5, width=20,
                          activebackground='red', activeforeground='white', command=submitadd)
    submitbutton.place(x=150, y=520)

    # -----------------------------------------------
    roolval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    rollnoentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=roolval)
    rollnoentry.place(x=270, y=100)
    nameentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=nameval)
    nameentry.place(x=270, y=160)
    mobileentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=mobileval)
    mobileentry.place(x=270, y=220)
    emailentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=emailval)
    emailentry.place(x=270, y=280)
    emailentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=addressval)
    emailentry.place(x=270, y=340)
    genderentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=genderval)
    genderentry.place(x=270, y=400)
    dobentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=dobval)
    dobentry.place(x=270, y=460)


def search():
    def submit():
        rool = roolval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        if (rool != ''):
            strr = 'select * from studentdata1 where rool = %s'
            mycursor.execute(strr, (rool))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (name != ''):
            strr = 'select * from studentdata1 where name = %s'
            mycursor.execute(strr, (name))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (mobile != ''):
            strr = 'select * from studentdata1 where mobile = %s'
            mycursor.execute(strr, (mobile))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (email != ''):
            strr = 'select * from studentdata1 where email = %s'
            mycursor.execute(strr, (email))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (address != ''):
            strr = 'select * from studentdata1 where address = %s'
            mycursor.execute(strr, (address))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (gender != ''):
            strr = 'select * from studentdata1 where gender = %s'
            mycursor.execute(strr, (gender))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (dob != ''):
            strr = 'select * from studentdata1 where dob = %s'
            mycursor.execute(strr, (dob))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

        if (date != ''):
            strr = 'select * from studentdata1 where Date = %s'
            mycursor.execute(strr, (date))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)

    root = Toplevel(master=DataEntryFrame)
    root.config(bg='blue')
    root.geometry('500x660+100+50')
    root.iconbitmap('logo.ico')
    root.title('Search student data')
    searchlabel = Label(root, text='search the student data', bg='gold2', width=25, font=('calibri', 19, 'bold'), bd=5,
                        relief=RIDGE)
    searchlabel.place(x=80, y=0)
    welcomelabel = Label(root, bg='blue', text='--------------------Search data----------------------',
                         font=('Ariel', 17, 'bold'))
    welcomelabel.place(x=10, y=50)
    rollnolabel = Label(root, bg='pink', text='Enter rollno.', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    rollnolabel.place(x=20, y=100)
    namelabel = Label(root, bg='pink', text='Enter Name', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                      bd=5, activebackground='blue', activeforeground='white', anchor='w')
    namelabel.place(x=20, y=160)
    mobilelabel = Label(root, bg='pink', text='Enter mobile', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    mobilelabel.place(x=20, y=220)
    emaillabel = Label(root, bg='pink', text='Enter email', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                       bd=5, activebackground='blue', activeforeground='white', anchor='w')
    emaillabel.place(x=20, y=280)
    addresslabel = Label(root, bg='pink', text='Enter address', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                         bd=5, activebackground='blue', activeforeground='white', anchor='w')
    addresslabel.place(x=20, y=340)
    genderlabel = Label(root, bg='pink', text='Enter gender', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    genderlabel.place(x=20, y=400)
    doblabel = Label(root, bg='pink', text='Enter D.O.B', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                     bd=5, activebackground='blue', activeforeground='white', anchor='w')
    doblabel.place(x=20, y=460)
    datelabel = Label(root, bg='pink', text='Enter Date', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                      bd=5, activebackground='blue', activeforeground='white', anchor='w')
    datelabel.place(x=20, y=520)

    submitbutton = Button(root, text='Submit', font=('roman', 15, 'bold'), bg='dark violet', bd=5, width=20,
                          activebackground='red', activeforeground='white', command=submit)
    submitbutton.place(x=150, y=580)
    # ------------------------
    roolval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    rollnoentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=roolval)
    rollnoentry.place(x=270, y=100)
    nameentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=nameval)
    nameentry.place(x=270, y=160)
    mobileentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=mobileval)
    mobileentry.place(x=270, y=220)
    emailentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=emailval)
    emailentry.place(x=270, y=280)
    emailentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=addressval)
    emailentry.place(x=270, y=340)
    genderentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=genderval)
    genderentry.place(x=270, y=400)
    dobentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=dobval)
    dobentry.place(x=270, y=460)
    dateentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=dateval)
    dateentry.place(x=270, y=520)
    root.mainloop()


def delete():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where rool = %s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notification', 'roll {} deleted succesfully...'.format(pp))
    strr = 'select * from studentdata1 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
        studenttable.insert('', END, values=vv)


def update():
    def update():
        rool = roolval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s where rool = %s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, rool))
        con.commit()
        messagebox.showinfo('Notificcation', 'rool {} modified succesfully'.format(rool), parent=root)
        strr = 'select * from studentdata1 '
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            studenttable.insert('', END, values=vv)

    root = Toplevel(master=DataEntryFrame)
    root.config(bg='blue')
    root.geometry('500x660+100+50')
    root.iconbitmap('logo.ico')
    root.title('Search student data')
    searchlabel = Label(root, text='update the student data', bg='gold2', width=25, font=('calibri', 19, 'bold'), bd=5,
                        relief=RIDGE)
    searchlabel.place(x=80, y=0)
    welcomelabel = Label(root, bg='blue', text='--------------------Update data----------------------',
                         font=('Ariel', 17, 'bold'))
    welcomelabel.place(x=10, y=50)
    rollnolabel = Label(root, bg='pink', text='Enter rollno.', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    rollnolabel.place(x=20, y=100)
    namelabel = Label(root, bg='pink', text='Enter Name', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                      bd=5, activebackground='blue', activeforeground='white', anchor='w')
    namelabel.place(x=20, y=160)
    mobilelabel = Label(root, bg='pink', text='Enter mobile', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    mobilelabel.place(x=20, y=220)
    emaillabel = Label(root, bg='pink', text='Enter email', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                       bd=5, activebackground='blue', activeforeground='white', anchor='w')
    emaillabel.place(x=20, y=280)
    addresslabel = Label(root, bg='pink', text='Enter address', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                         bd=5, activebackground='blue', activeforeground='white', anchor='w')
    addresslabel.place(x=20, y=340)
    genderlabel = Label(root, bg='pink', text='Enter gender', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                        bd=5, activebackground='blue', activeforeground='white', anchor='w')
    genderlabel.place(x=20, y=400)
    doblabel = Label(root, bg='pink', text='Enter D.O.B', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                     bd=5, activebackground='blue', activeforeground='white', anchor='w')
    doblabel.place(x=20, y=460)
    datelabel = Label(root, bg='pink', text='Enter Date', font=('algerian', 19, 'bold'), width=13, relief=GROOVE,
                      bd=5, activebackground='blue', activeforeground='white', anchor='w')
    datelabel.place(x=20, y=520)

    submitbutton = Button(root, text='Submit', font=('roman', 15, 'bold'), bg='dark violet', bd=5, width=20,
                          activebackground='red', activeforeground='white', command=update)
    submitbutton.place(x=150, y=580)

    roolval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    rollnoentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=roolval)
    rollnoentry.place(x=270, y=100)
    nameentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=nameval)
    nameentry.place(x=270, y=160)
    mobileentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=mobileval)
    mobileentry.place(x=270, y=220)
    emailentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=emailval)
    emailentry.place(x=270, y=280)
    emailentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=addressval)
    emailentry.place(x=270, y=340)
    genderentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=genderval)
    genderentry.place(x=270, y=400)
    dobentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=dobval)
    dobentry.place(x=270, y=460)
    dateentry = Entry(root, font=('roman', 18, 'bold'), bd=5, width=18, textvariable=dateval)
    dateentry.place(x=270, y=520)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if len(pp) != 0:
        roolval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        # timeval.set(pp[8])

    root.mainloop()


def showall():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    data = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in data:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
        studenttable.insert('', END, values=vv)


def exit():
    res = messagebox.askyesnocancel('Notification', 'do you want to exit')
    if res == True:
        root.destroy()


# -----------------------
def database():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification', 'data is incorrect please try again')
            return
        try:
            strr = 'create database studentmanagmentsystem2'
            mycursor.execute(strr)
            strr = 'use studentmanagmentsystem2'
            mycursor.execute(strr)
            strr = 'create table studentdata1(rool int,name varchar(30),mobile varchar(12),email  varchar(35),address varchar(100),gender varchar(50),dob varchar(40),Date varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int NOT NULL'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'database connected....', parent=dbroot)
        except:
            strr = 'use studentmanagmentsystem2'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'database connected....', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.iconbitmap('logo.ico')
    dbroot.geometry('470x250')
    dbroot.resizable(False, False)
    dbroot.config(bg='chartreuse')
    # ---------------------------dblables
    hostlabel = Label(dbroot, text='enter host:', bg='red', font=('times', 20, 'bold'), relief=RIDGE,
                      borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text='enter user:', bg='red', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,
                      width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='enter password:', bg='red', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3,
                          width=13, anchor='w')
    passwordlabel.place(x=10, y=130)
    # ----------------------------------connectdb entey
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # --------------------------------------------connectdb button
    submitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bg='blue', bd=5, width=20,
                          activebackground='red', activeforeground='white', command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()


root = Tk()
root.title('student managment system')
root.config(bg='Blue')
root.geometry('1174x700+200+50')
root.resizable(True, True)
# root.grab_set()
root.iconbitmap('logo.ico')

# ---------------------
SliderLabel = Label(root, text='Student Managment System', width=30, font=('Arial', 25, ' bold'), relief=RIDGE,
                    borderwidth=5, bg='gold2')
SliderLabel.place(x=220, y=0)
conbutton = Button(root, text='Login ', width=10, font=('oracle', 19, 'bold'), relief=GROOVE, bg='green',
                   activebackground='firebrick1', activeforeground='royal blue', command=database)
conbutton.place(x=0, y=0)
DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=1150, height=50)
# ----------------------------frames intro

addbutton = Button(DataEntryFrame, text='1: Add students', width=15, font=('chiller', 20, 'bold'), bd=4,
                   bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=add)
addbutton.pack(side=LEFT, expand=True)

serchbutton = Button(DataEntryFrame, text='2: Serch students', width=15, font=('chiller', 20, 'bold'), bd=6,
                     bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=search)
serchbutton.pack(side=LEFT, expand=True)

deletebutton = Button(DataEntryFrame, text='3: Delete students', width=15, font=('chiller', 20, 'bold'), bd=6,
                      bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=delete)
deletebutton.pack(side=LEFT, expand=True)

updatebutton = Button(DataEntryFrame, text='4: update students', width=15, font=('chiller', 20, 'bold'), bd=6,
                      bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=update)
updatebutton.pack(side=LEFT, expand=True)

showbutton = Button(DataEntryFrame, text='5: Show All', width=15, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',
                    activebackground='blue', relief=RIDGE, activeforeground='white', command=showall)
showbutton.pack(side=LEFT, expand=True)

Exitbutton = Button(DataEntryFrame, text='6: Exit', width=15, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',
                    activebackground='blue', relief=RIDGE, activeforeground='white', command=exit)
Exitbutton.pack(side=LEFT, expand=True)
# -----------------------------Show data frame

ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=30, y=140, width=1120, height=550)


def clock1():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + "\n" + "Time :" + time_string)
    clock.after(200, clock1)


style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 15, 'bold'), foreground='black', background='cyan')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,
                        column=('id', 'Name', 'mobile', 'Email', 'address', 'gender', 'D.O.B', 'Added Date'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('id', text='id')
studenttable.heading('Name', text='Name')
studenttable.heading('mobile', text='mobile')
studenttable.heading('Email', text='Email')
studenttable.heading('address', text='address')
studenttable.heading('gender', text='gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
# studenttable.heading('Added time', text='Added time')
studenttable['show'] = 'headings'
studenttable.column('id', width=100)
studenttable.column('Name', width=200)
studenttable.column('mobile', width=200)
studenttable.column('Email', width=300)
studenttable.column('address', width=200)
studenttable.column('gender', width=100)
studenttable.column('D.O.B', width=150)
studenttable.column('Added Date', width=150)
# studenttable.column('Added time', width=150)
studenttable.pack(fill=BOTH, expand=1)
clock = Label(root, bg='green', width=15, font=('oracle', 15, 'bold'), bd=5)
clock.place(x=990, y=0)
clock1()
root.mainloop()
