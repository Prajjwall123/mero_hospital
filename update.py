#importing modules
from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import runpy

#connecting the database
database = sqlite3.connect("data.db")
cursor = database.cursor()


#defining the window and some basic configuration
admin_page=Tk()
admin_page.title("MERO HOSPITAL")
admin_page.iconbitmap("download.ico")
admin_page.geometry("1200x250")
admin_page.config(bg="white")
admin_page.resizable(False,False)

#headings for the tables
heading = Label(admin_page,text='login_info',fg='black',border=0,bg='white',font=('comicsansms',25,'bold'))
heading.place(x=0,y=0)
heading_1 = Label(admin_page,text='department',fg='black',border=0,bg='white',font=('comicsansms',25,'bold'))
heading_1.place(x=200,y=0)
heading_2 = Label(admin_page,text='patient',fg='black',border=0,bg='white',font=('comicsansms',25,'bold'))
heading_2.place(x=400,y=0)
heading_3 = Label(admin_page,text='doctor',fg='black',border=0,bg='white',font=('comicsansms',25,'bold'))
heading_3.place(x=600,y=0)
heading_3 = Label(admin_page,text='ambulance',fg='black',border=0,bg='white',font=('comicsansms',25,'bold'))
heading_3.place(x=800,y=0)
heading_4 = Label(admin_page,text='admin',fg='black',border=0,bg='white',font=('comicsansms',25,'bold'))
heading_4.place(x=1100,y=0)

#frames
frame1=Frame(admin_page,width=2,height=200,bg="VioletRed3").place(x=180,y=0)
frame2=Frame(admin_page,width=2,height=200,bg="VioletRed3").place(x=380,y=0)
frame3=Frame(admin_page,width=2,height=200,bg="VioletRed3").place(x=580,y=0)
frame4=Frame(admin_page,width=2,height=200,bg="VioletRed3").place(x=780,y=0)
frame4=Frame(admin_page,width=2,height=200,bg="VioletRed3").place(x=1080,y=0)

#show contents of login page
def show_records_login():

    cursor.execute("SELECT *, oid FROM login_info")
    records=cursor.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+" "+str(record[1])+ " "+ "\t"+str(record[4])+"\n"

    # query_label=Label(admin_page,text=print_record)
    # query_label.place(x=0,y=200)

show_button=Button(admin_page,text="show",command=show_records_login,bg="red",fg="white")
show_button.place(x=0,y=50)

#delete records of login page

def delete_login():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()
    a=delete_entry.get()
    cursor.execute("DELETE from login_info WHERE oid = "+str(a))
    print("Deleted Successfully")
    database.commit()
    database.close()


delete_entry=Entry(admin_page)
delete_entry.place(x=0,y=100)

delete_button=Button(admin_page,text="delete",command=delete_login,bg="red",fg="white")
delete_button.place(x=0,y=150)

#show contents of department
def show_records_department():

    cursor.execute("SELECT *, oid FROM department")
    records=cursor.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+" "+str(record[1])+"\n"

    # query_label=Label(admin_page,text=print_record)
    # query_label.place(x=200,y=200)

show_button=Button(admin_page,text="show",command=show_records_department,bg="red",fg="white")
show_button.place(x=200,y=50)

#delete records of department

def delete_department():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()
    cursor.execute("DELETE from department WHERE oid = "+delete_entry.get())
    print("Deleted Successfully")
    database.commit()
    database.close()


delete_entry=Entry(admin_page)
delete_entry.place(x=200,y=100)

delete_button=Button(admin_page,text="delete",command=delete_department,bg="red",fg="white")
delete_button.place(x=200,y=150)

#show contents of patient
def show_records_patient():

    cursor.execute("SELECT *, oid FROM patient")
    records=cursor.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+" "+str(record[2])+"\n"

    # query_label=Label(admin_page,text=print_record)
    # query_label.place(x=400,y=200)

show_button=Button(admin_page,text="show",command=show_records_patient,bg="red",fg="white")
show_button.place(x=400,y=50)

#delete records of patient

def delete_patient():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()
    cursor.execute("DELETE from patient WHERE oid = "+delete_entry.get())
    print("Deleted Successfully")
    database.commit()
    database.close()


delete_entry=Entry(admin_page)
delete_entry.place(x=400,y=100)

delete_button=Button(admin_page,text="delete",command=delete_patient,bg="red",fg="white")
delete_button.place(x=400,y=150)

#show contents of doctor
def show_records_admin():

    cursor.execute("SELECT *, oid FROM doctor")
    records=cursor.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+" "+str(record[5])+"\n"

    # query_label=Label(admin_page,text=print_record)
    # query_label.place(x=600,y=200)

show_button=Button(admin_page,text="show",command=show_records_admin,bg="red",fg="white")
show_button.place(x=600,y=50)

#delete records of doctor

def delete_admin():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()
    cursor.execute("DELETE from admin WHERE oid = "+delete_entry.get())
    print("Deleted Successfully")
    database.commit()
    database.close()


delete_entry=Entry(admin_page)
delete_entry.place(x=600,y=100)

delete_button=Button(admin_page,text="delete",command=delete_admin,bg="red",fg="white")
delete_button.place(x=600,y=150)

#show contents of ambulance
def show_records_ambulance():

    cursor.execute("SELECT *, oid FROM ambulance")
    records=cursor.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+" "+str(record[1])+ " "+ "\t"+str(record[4])+"\n"

    # query_label=Label(admin_page,text=print_record)
    # query_label.place(x=900,y=200)

show_button=Button(admin_page,text="show",command=show_records_ambulance,bg="red",fg="white")
show_button.place(x=900,y=50)

#delete records of ambulance

def delete_ambulance():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()
    a=delete_entry.get()
    cursor.execute("DELETE from ambulance WHERE oid = "+str(a))
    print("Deleted Successfully")
    database.commit()
    database.close()


delete_entry=Entry(admin_page)
delete_entry.place(x=900,y=100)

delete_button=Button(admin_page,text="delete",command=delete_ambulance,bg="red",fg="white")
delete_button.place(x=900,y=150)

#show contents of admin
def show_records_admin():

    cursor.execute("SELECT *, oid FROM admin")
    records=cursor.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+" "+str(record[1])+ " "+ "\t"+str(record[3])+"\n"

    # query_label=Label(admin_page,text=print_record)
    # query_label.place(x=1100,y=200)

show_button=Button(admin_page,text="show",command=show_records_admin,bg="red",fg="white")
show_button.place(x=1100,y=50)

#delete records of admin

def delete_login():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()
    a=delete_entry.get()
    cursor.execute("DELETE from admin WHERE oid = "+str(a))
    print("Deleted Successfully")
    database.commit()
    database.close()


delete_entry=Entry(admin_page)
delete_entry.place(x=1100,y=100)

delete_button=Button(admin_page,text="delete",command=delete_login,bg="red",fg="white")
delete_button.place(x=1100,y=150)

#open the dashboard
def dash():
    admin_page.destroy()
    runpy.run_path("dashb1.py")

dash = Button(admin_page,text='OPEN DASHBOARD',border=5,bg='violetred3',fg='black',command=dash)
dash.place(x=0,y=200,width=1200,height=60)

#running the loop
admin_page.mainloop()