#import modules
from tkinter import*
from tkinter import messagebox
import runpy
import sqlite3

#basic configuration
root = Tk()
root.title('Mero Hospital')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

#connecting the database
database = sqlite3.connect("data.db")
cursor = database.cursor()


# Icon Install

photo = PhotoImage(file='download.png')
root.iconphoto(False,photo)
root.configure(bg='white')

# Log in Image

img = PhotoImage(file='Mero.png')
Label(root,image = img,bg='white').place(x=0,y=20)

# Frame and Heading

frame = Frame(root,width=400,height=350,bg='white')
frame.place(x=480,y=75)

# Heading Name
 
heading = Label(frame,text='SIGN IN AS ADMIN',fg='VioletRed3',border=0,bg='white',font=('comicsansms',25,'bold'))
heading.place(x=100,y=0)

# Function For User

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'phone number')


#for loading dashboard
def main():
    root.destroy()
    runpy.run_path("update.py")

#for register page
def sign_up():
    root.destroy()
    runpy.run_path("register.py")

# UserName And PhoneNUmber

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('comicsansms',11))
user.place(x=100,y=86)
user.insert(0,'phone number')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=285,height=2,bg='black').place(x=75,y=107)

# Function For Password

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.delete(0,'PassWord')

 

# Code for the Password

code = Entry(frame,width=25,fg='black',border=0,bg='white',relief=FLAT,show='*',font=('comicsansms',11))
code.place(x=130,y=155)
code.insert(0,'PassWord')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=285,height=2,bg='black').place(x=75,y=177)

# Hide and Show Button

def show():
    hide_button = Button(root,image=hide_img,command=hide,relief=FLAT,activebackground='white',border=0,bg='white')
    hide_button.place(x=810,y=215)
    code.config(show='')
hide_img = PhotoImage(file='closeye.png')

def hide():
    show_button = Button(root,image=show_img,command=show,relief=FLAT,activeforeground='white',border=0,bg='white')
    show_button.place(x=810,y=215)
    code.config(show='*')
show_img = PhotoImage(file='openeye(1).png')

def back():
    root.destroy()
    runpy.run_path("font.py")

# Button for the hide and show password

show_button = Button(root,image=show_img,command=show,relief=FLAT,activebackground='white',border=0,bg='white')
show_button.place(x=810,y=215)

#check the login info
def check():
    database = sqlite3.connect("data.db")
    cursor = database.cursor()
    query="select * from admin where phone_number=?"
    cursor.execute(query,[user.get()])
    row=cursor.fetchone()
    pw=code.get()
    if row!=None:
        if pw==row[2]:
            messagebox.showinfo("success","logged in successfully")
            main()
        else:
            messagebox.showerror("error","incorrect password")
    else:
        messagebox.showerror("error","you don't have access to admin page")

    
    database.commit()
    database.close()


# Button For the Log In

Button(frame,width=39,pady=10,text='SIGN IN',bg='VioletRed3',fg='black',border=0,command=check).place(x=75,y=212)

#go back button
signin = Button(frame,text='BACK',border=5,bg='violetred3',fg='black',command=back)
signin.place(x=165,y=300,width=130,height=40)
root.mainloop()