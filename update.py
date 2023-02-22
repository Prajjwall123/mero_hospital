#importing modules
from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import runpy

database = sqlite3.connect("data.db")
cursor = database.cursor()

#functions
def hide():
    open_eye.config(file="closeye.png")
    password.config(show="*")
    eyeButton.config(command=show)
def show():
    open_eye.config(file="openeye(1).png")
    password.config(show=" ")
    eyeButton.config(command=hide)
def on_enter(event):
    if username.get()=="NAME":
        username.delete(0,END)
def on_enter_2(event):
    if password.get()=="PASSWORD":
        password.delete(0,END)
def on_enter_3(event):
    if phone_number.get()=="PHONE NUMBER":
        phone_number.delete(0,END)
def on_enter_4(event):
    if address.get()=="ADDRESS":
        address.delete(0,END)
def font():
    login_page.destroy()
    runpy.run_path("font.py")

#connect to the database
def connect_database():

    try:
        database = sqlite3.connect("data.db")
        cursor = database.cursor()
        if username.get()=="NAME" or password.get()=="PASSWORD" or address.get()=="ADDRESS" or phone_number.get()=="PHONE NUMBER":
            messagebox.showerror("error","no field can be empty")
        else:

            #inserting into database
            try:

                cursor.execute("INSERT INTO login_info VALUES(:phone_number,:username,:password,:address)",{
                    'phone_number': phone_number.get(),
                    'username': username.get(),
                    'password': password.get(),
                    'address':address.get(),
                })
                messagebox.showinfo("success","try sign-in now")
                password.delete(0,END)
                address.delete(0, END)
                username.delete(0, END)
                phone_number.delete(0,END)
            
            except:
                messagebox.showinfo("Error","Number in use or incorrect data format entered")

        database.commit()
        database.close()
    except:
        messagebox.showerror("error","problems connecting the database")
        


#defining the window and some basic configuration
login_page=Tk()
login_page.title("MERO HOSPITAL")
login_page.iconbitmap("download.ico")
login_page.geometry("900x550")#window size same as the image size
login_page.config(bg="white")
login_page.resizable(False,False)


#loading image
my_image=ImageTk.PhotoImage(Image.open("mero.png"))
bg_label=Label(image=my_image,bd=0)
bg_label.place(x=0,y=0)#placing the image
heading=Label(login_page,text="SIGN UP",bg="white",fg="VioletRed3",font=("Arial",20,"bold"))
heading.place(x=670,y=50)
#entry classes
#username
username=Entry(login_page,width=25,font=("Arial",11),fg="VioletRed3",bd=0)
username.insert(0,"NAME")
username.place(x=640,y=150)
username.bind("<FocusIn>",on_enter)
#password
password=Entry(login_page,width=25,font=("Arial",11),fg="VioletRed3",bd=0)
password.insert(0,"PASSWORD")
password.place(x=640,y=250)
password.bind("<FocusIn>",on_enter_2)
#phone number
phone_number=Entry(login_page,width=25,font=("Arial",11),fg="VioletRed3",bd=0)
phone_number.insert(0,"PHONE NUMBER")
phone_number.place(x=640,y=350)
phone_number.bind("<FocusIn>",on_enter_3)
#address
address=Entry(login_page,width=25,font=("Arial",11),fg="VioletRed3",bd=0)
address.insert(0,"ADDRESS")
address.place(x=640,y=450)
address.bind("<FocusIn>",on_enter_4)
#frames
frame1=Frame(login_page,width=200,height=2,bg="VioletRed3").place(x=640,y=175)#username
frame2=Frame(login_page,width=200,height=2,bg="VioletRed3").place(x=640,y=275)#password
frame3=Frame(login_page,width=200,height=2,bg="VioletRed3").place(x=640,y=375)#phone_number
frame4=Frame(login_page,width=200,height=2,bg="VioletRed3").place(x=640,y=475)#address
#Button(show_notshow)
open_eye=PhotoImage(file="openeye(1).png")
eyeButton=Button(login_page,image=open_eye,bd=0,bg="white",cursor="hand2",command=hide)
eyeButton.place(x=810,y=245)
label = Label(login_page,text="Have an account?",fg='VioletRed3',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=635,y=485)
registerButton=Button(login_page,text="SIGN IN",bd=0,bg="VioletRed3",fg="white",cursor="hand2",font=("Arial",11),command=font)
registerButton.place(x=775,y=485)
loginButton=Button(login_page,text="SIGN UP",bg="VioletRed3",fg="white",cursor="hand2",font=("Arial",9),command=connect_database)
loginButton.place(x=705,y=510)

#running the loop
login_page.mainloop()
