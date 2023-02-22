#importing the modules
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

#connecting the database
database = sqlite3.connect("data.db")
cursor = database.cursor()

#basic configuration
root = Tk()
root.title('Mero Hospital')
root.geometry('1280x720')
root.resizable(False,False)

# Icon Install

photo = PhotoImage(file='download.png')
root.iconphoto(False,photo)
root.configure(bg='white')

# Frame for the Heading

Heading = LabelFrame(root,border=2,relief='groove',bg='VioletRed3')
Heading.place(x=0,y=0,width=1280,height=60)

# Name of the application

name = Label(Heading,bg='VioletRed3',fg='black',text='Mero : Hospital',font=('arail',25,'bold'))
name.place(x=0,y=5)

# Tagline for the Application

tagline = Label(Heading,bg='VioletRed3',fg='black',text='OUR SERVICES',font=('arial',25,'bold'))
tagline.place(x=420,y=5)

# Frame for the Selection of Requirement

frame = LabelFrame(root,border=2,relief='groove',text='SERVICES',font=('arial',20,'bold'),bg='white')
frame.place(x=50,y=130,width=1120,height=520)

# Logo On Option Frame

Logo = Image.open('hos.png')
image = ImageTk.PhotoImage(Logo)
Label(frame,image=image,bg='white').place(x=380,y=50)

# Button Frame

Btn_frame = LabelFrame(root,border=1,relief='groove',bg='white')
Btn_frame.place(x=2,y=65,width=1280,height=55)

# Image for the Option After the Department Button

dego = Image.open('Mero Hos2.jpg')
log = ImageTk.PhotoImage(dego)

# Function to Hide all Frames

def HideAllFrames():
    for widget in frame.winfo_children():
        widget.destroy()


def departmentCall():
    HideAllFrames()

    Department_Lbl = Label(frame,text='Department',bg='white',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)
    btn_frame = LabelFrame(frame,border=2,relief='groove',bg='violetred3')
    btn_frame.place(x=15,y=65,width=315,height=345)

    imge_lfl= LabelFrame(frame,border=2,relief='groove')
    imge_lfl.place(x=340,y=15,width=820,height=450)
    img = Label(imge_lfl,image=log).place(x=250,y=55)

# Function for the Dental

    def DentalCall():
        HideAllFrames()
        query="select * from doctor where doctor_id=?"
        cursor.execute(query,[1])
        row=cursor.fetchone()
        cursor.execute(query,[2])
        row_1=cursor.fetchone()
        cursor.execute(query,[3])
        row_2=cursor.fetchone()
        cursor.execute(query,[4])
        row_3=cursor.fetchone()

        Dental_lbl = Label(frame,text='Doctor For Dental',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        head1 = Label(frame,text='Doctor',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
        head2 = Label(frame,text='Time',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
        head3 = Label(frame,text='Availability',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

        doc1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
        doc2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
        doc3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
        doc4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

        time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
        time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
        time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
        time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

        day1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
        day2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
        day3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
        day4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

    
    dental_btn = Button(btn_frame,bg="light yellow",fg="black",border=2,text="Dental",font=("times",19,"bold"),activebackground="light blue",command=DentalCall)
    dental_btn.place(x=3,y=5,width=305)

# Function FOr the Dermatology

    def DermatologyCall():
        query="select * from doctor where doctor_id=?"
        cursor.execute(query,[5])
        row=cursor.fetchone()
        cursor.execute(query,[6])
        row_1=cursor.fetchone()
        cursor.execute(query,[7])
        row_2=cursor.fetchone()
        cursor.execute(query,[8])
        row_3=cursor.fetchone()
        HideAllFrames()
        Derma_lbl = Label(frame,text='Doctor For Dermatalogy',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        head1 = Label(frame,text='Doctor',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
        head2 = Label(frame,text='Time',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
        head3 = Label(frame,text='Availability',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

        doc1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
        doc2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
        doc3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
        doc4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

        time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
        time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
        time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
        time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

        day1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
        day2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
        day3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
        day4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

    derma_btn = Button(btn_frame,bg="light yellow",fg="black",border=2,text="Dermatalogy",font=("times",19,"bold"),activebackground="light blue",command=DermatologyCall)
    derma_btn.place(x=3,y=60,width=305)

# Function for the Endocrinology

    def EndocrinologyCall():
        query="select * from doctor where doctor_id=?"
        cursor.execute(query,[9])
        row=cursor.fetchone()
        cursor.execute(query,[10])
        row_1=cursor.fetchone()
        cursor.execute(query,[11])
        row_2=cursor.fetchone()
        cursor.execute(query,[12])
        row_3=cursor.fetchone()
        HideAllFrames()

        Endocri_lbl = Label(frame,text='Doctor For Endocrinology',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        head1 = Label(frame,text='Doctor',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
        head2 = Label(frame,text='Time',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
        head3 = Label(frame,text='Availability',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

        doc1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
        doc2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
        doc3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
        doc4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

        time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
        time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
        time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
        time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

        day1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
        day2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
        day3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
        day4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

    endo_btn = Button(btn_frame,bg="light yellow",fg="black",border=2,text="Endocrinology",font=("times",19,"bold"),activebackground="light blue",command=EndocrinologyCall)
    endo_btn.place(x=3,y=115,width=305)

# Function For the Gynaecology

    def GynaecologyCall():
        query="select * from doctor where doctor_id=?"
        cursor.execute(query,[13])
        row=cursor.fetchone()
        cursor.execute(query,[14])
        row_1=cursor.fetchone()
        cursor.execute(query,[15])
        row_2=cursor.fetchone()
        cursor.execute(query,[16])
        row_3=cursor.fetchone()
        HideAllFrames()

        Gynaecology_lbl = Label(frame,text='Doctor For Gynaecology',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        head1 = Label(frame,text='Doctor',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
        head2 = Label(frame,text='Time',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
        head3 = Label(frame,text='Availability',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

        doc1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
        doc2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
        doc3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
        doc4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

        time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
        time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
        time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
        time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

        day1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
        day2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
        day3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
        day4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

    gyna_btn = Button(btn_frame,bg="light yellow",fg="black",border=2,text="Gynaecology",font=("times",19,"bold"),activebackground="light blue",command=GynaecologyCall)
    gyna_btn.place(x=3,y=170,width=305)

# Function for the NeuroSugery

    def NeurosugeryCall():
        query="select * from doctor where doctor_id=?"
        cursor.execute(query,[17])
        row=cursor.fetchone()
        cursor.execute(query,[18])
        row_1=cursor.fetchone()
        cursor.execute(query,[19])
        row_2=cursor.fetchone()
        cursor.execute(query,[20])
        row_3=cursor.fetchone()
        HideAllFrames()

        Neurosugery_lbl = Label(frame,text='Doctor For Neurosugery',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        head1 = Label(frame,text='Doctor',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
        head2 = Label(frame,text='Time',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
        head3 = Label(frame,text='Availability',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

        doc1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
        doc2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
        doc3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
        doc4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

        time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
        time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
        time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
        time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

        day1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
        day2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
        day3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
        day4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

    neuro_btn = Button(btn_frame,bg="light yellow",fg="black",border=2,text="Neurosugery",font=("times",19,"bold"),activebackground="light blue",command=NeurosugeryCall)
    neuro_btn.place(x=3,y=225,width=305)

# Function for the Psychiatric

    def PsychiatricCall():
        query="select * from doctor where doctor_id=?"
        cursor.execute(query,[21])
        row=cursor.fetchone()
        cursor.execute(query,[22])
        row_1=cursor.fetchone()
        cursor.execute(query,[23])
        row_2=cursor.fetchone()
        cursor.execute(query,[24])
        row_3=cursor.fetchone()
        HideAllFrames()

        Psychiatric_lbl = Label(frame,text='Doctor For Psychiatric',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        head1 = Label(frame,text='Doctor',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
        head2 = Label(frame,text='Time',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
        head3 = Label(frame,text='Availability',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

        doc1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
        doc2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
        doc3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
        doc4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

        time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
        time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
        time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
        time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

        day1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
        day2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
        day3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
        day4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

    pych_btn = Button(btn_frame,bg="light yellow",fg="black",border=2,text="Psychiatric",font=("times",19,"bold"),activebackground="light blue",command=PsychiatricCall)
    pych_btn.place(x=3,y=280,width=305)


depar_btn = Button(Btn_frame,bg="light yellow",fg="black",border=2,text="Departments",font=("times",19,"bold"),activebackground="light blue",command=departmentCall)
depar_btn.place(x=110,y=0,width=305)

# Function for the Ambulance Contact

def ContactCall():
    HideAllFrames()
    query="select * from ambulance where ambulance_id=?"
    cursor.execute(query,[1])
    row=cursor.fetchone()
    cursor.execute(query,[2])
    row_1=cursor.fetchone()
    cursor.execute(query,[3])
    row_2=cursor.fetchone()
    cursor.execute(query,[4])
    row_3=cursor.fetchone()

    contact_lbl = Label(frame,text='Contact Number For Ambulance',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

    head1 = Label(frame,text='AREA',fg='black',bg='white',font=('comicsansms',18)).place(x=150,y=120)
    head2 = Label(frame,text='NUMBER',fg='black',bg='white',font=('comicsansms',18)).place(x=430,y=120)
    head3 = Label(frame,text='ALTERNATE',fg='black',bg='white',font=('comicsansms',18)).place(x=670,y=120)

    doc1 = Label(frame,text=row[3],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=180)
    doc2 = Label(frame,text=row_1[3],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=230)
    doc3 = Label(frame,text=row_2[3],fg='black',bg='white',font=('comicsansms',15)).place(x=150,y=280)
    doc4 = Label(frame,text=row_3[3],fg='black',bg='white',font=('camicsansms',15)).place(x=150,y=330)

    time1 = Label(frame,text=row[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=180)
    time2 = Label(frame,text=row_1[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=230)
    time3 = Label(frame,text=row_2[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=280)
    time4 = Label(frame,text=row_3[2],fg='black',bg='white',font=('comicsansms',15)).place(x=420,y=330)

    day1 = Label(frame,text=row[1],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=180)
    day2 = Label(frame,text=row_1[1],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=230)
    day3 = Label(frame,text=row_2[1],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=280)
    day4 = Label(frame,text=row_3[1],fg='black',bg='white',font=('comicsansms',15)).place(x=670,y=330)

# Button for the Contact

Contact_btn = Button(Btn_frame,bg="light yellow",fg="black",border=2,text="Ambulance Contact",font=("times",19,"bold"),activebackground="light blue",command=ContactCall)
Contact_btn.place(x=505,y=0,width=305)

# Image for Buttons

Dental_1 = Image.open('spem.jpg')
size_image=(500,400)
dental_resized=Dental_1.resize(size_image)
Dental = ImageTk.PhotoImage(dental_resized)

Dermatology_2 = Image.open('ECG2.jpg')
Dermatology = ImageTk.PhotoImage(Dermatology_2)

Endcrocrinology_3 = Image.open('ECG.jpg')
Endcrocrinology = ImageTk.PhotoImage(Endcrocrinology_3)

# Gynaecology_4 = Image.open(' ')
# Gynaecology = ImageTk.PhotoImage(Gynaecology_4)

# Neurosugery_5 = Image.open(' ')
# Neurosugery = ImageTk.PhotoImage(Neurosugery_5)

# Psychiatric_6 = Image.open(' ')
# Psychiatric = ImageTk.PhotoImage(Psychiatric_6)



# Button for the View Report

def ReportCall():
    HideAllFrames()

    Report_lbl = Label(frame,text='Report of Patients',bg='grey',fg='black',font=('times',15,'bold')).grid(row=0,column=0,padx=10)
    log_frame = Frame(frame,border=1,relief='groove',bg='white')
    log_frame.place(x=310,y=80,width=500,height=350)
    lo_lbl = Label(log_frame,text='LOGIN',bg='white',fg='black',font=('time',30,'bold'))
    lo_lbl.place(x=185,y=20)

    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name = user.get()
    if name == '':
        user.insert(0,'UserName/Number')

    # UserName And PhoneNUmber

    user = Entry(log_frame,width=25,fg='black',border=0,bg='white',font=('comicsansms',11))
    user.place(x=135,y=103)
    user.insert(0,'UserName/PhoneNumber')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(log_frame,width=285,height=2,bg='black').place(x=105,y=135)

# Function For Password

    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name = code.get()
    if name == '':
        code.insert(0,'PassWord')

# Code for the Password

    code = Entry(log_frame,width=25,fg='black',border=14,bg='white',relief=FLAT,show='*',font=('comicsansms',11))
    code.place(x=150,y=180)
    code.insert(0,'PassWord')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(log_frame,width=285,height=2,bg='black',border=70).place(x=105,y=220)

    # Hide and Show Button

    def show():
        hide_button = Button(log_frame,image=hide_img,command=hide,relief=FLAT,activebackground='white',border=0,bg='white')
        hide_button.place(x=355,y=190)
        code.config(show='')
    hide_img = PhotoImage(file='closeye.png')

    def hide():
        show_button = Button(log_frame,image=show_img,command=show,relief=FLAT,activeforeground='white',border=0,bg='white')
        show_button.place(x=355,y=190)
        code.config(show='*')
    show_img = PhotoImage(file='openeye(1).png')

# Button for the hide and show password

    show_button = Button(log_frame,image=show_img,command=show,relief=FLAT,activebackground='white',border=0,bg='white')
    show_button.place(x=355,y=190)

    # check the login info
    def check():
        database = sqlite3.connect("data.db")
        cursor = database.cursor()
        query = "select * from login_info where phone_number=?"
        cursor.execute(query, [user.get()])
        row = cursor.fetchone()
        pw = code.get()
        # messagebox.showinfo("show",row[2])
        # messagebox.showinfo("show",pw)
        if row != None:
            if pw == row[2]:
                loginCall()
            else:
                messagebox.showerror("error", "incorrect password")
        else:
            messagebox.showerror("error", "the number is not registered")

        database.commit()
        database.close()


    def loginCall():
        # check the department for access to the report
        database = sqlite3.connect("data.db")
        cursor = database.cursor()
        query = "select * from patient where phone_number=?"
        cursor.execute(query, [user.get()])
        row = cursor.fetchone()

        HideAllFrames()

        report_lbl = Label(frame,text='Patient Report',bg='grey',fg='black',font=('times',30,'bold')).grid(row=0,column=0,padx=10)

        view_frame = LabelFrame(frame,border=2,relief='groove',bg='violetred3')
        view_frame.place(x=15,y=65,width=315,height=380)

        def deCall():
            HideAllFrames()

            den_lbl = Label(frame,text='Report Of Dental',bg='grey',fg='white',font=('times',25,'bold')).grid(row=0,column=0,padx=10)
            lbl_name = Label(frame,image=Dental,border=0,justify='center').place(x=230,y=45)

        if(row[2]==1):
            messagebox.showinfo("allowed","allowed to view dental report")
            log_button = Button(view_frame,text='DENTAL',border=3,bg='light yellow',fg='black',font=('times',19,'bold'),command=deCall)
            log_button.place(x=3,y=5,width=305)

        def derCall():
            HideAllFrames()

            der_lbl = Label(frame,text='Report Of Dermatology',bg='grey',fg='white',font=('times',25,'bold')).grid(row=0,column=0,padx=10)
            lbl_name = Label(frame,image=Dermatology,border=0,justify='center').place(x=380,y=10)

        if(row[2]==2):
            messagebox.showinfo("allowed","allowed to view dermatology report")
            log_button = Button(view_frame,text='Dermatology',border=3,bg='light yellow',fg='black',font=('times',19,'bold'),command=derCall)
            log_button.place(x=3,y=67,width=305)

        def EndCall():
            HideAllFrames()

            der_lbl = Label(frame,text='Report Of Endcrocrinology',bg='grey',fg='white',font=('times',25,'bold')).grid(row=0,column=0,padx=10)
            lbl_name = Label(frame,image=Endcrocrinology,border=0,justify='center').place(x=430,y=20)

        if(row[2]==3):
            messagebox.showinfo("allowed","allowed to view endocrinology report")
            log_button = Button(view_frame,text='Endcrocrinology',border=3,bg='light yellow',fg='black',font=('times',19,'bold'),command=EndCall)
            log_button.place(x=3,y=130,width=305)

        def GnyCall():
            HideAllFrames()

            der_lbl = Label(frame,text='Report Of Gynaecology',bg='grey',fg='white',font=('times',25,'bold')).grid(row=0,column=0,padx=10)
            lbl_name = Label(frame,image=Dental,border=0,justify='center').place(x=430,y=20)

        if(row[2]==4):
            messagebox.showinfo("allowed","allowed to view gynaecology report")
            log_button = Button(view_frame,text='Gynaecology',border=3,bg='light yellow',fg='black',font=('times',19,'bold'),command=GnyCall)
            log_button.place(x=3,y=190,width=305)

        def Psy():
            HideAllFrames()

            der_lbl = Label(frame,text='Report Of Psychiatry',bg='grey',fg='white',font=('times',25,'bold')).grid(row=0,column=0,padx=10)
            lbl_name = Label(frame,image=Endcrocrinology,border=0,justify='center').place(x=430,y=20)

        if(row[2]==5):
            messagebox.showinfo("allowed","allowed to view psychiatry report")
            log_button = Button(view_frame,text='Psychiatry',border=3,bg='light yellow',fg='black',font=('times',19,'bold'),command=Psy)
            log_button.place(x=3,y=250,width=305)

        def Neu():
            HideAllFrames()

            der_lbl = Label(frame,text='Report Of Neurosurgery',bg='grey',fg='white',font=('times',25,'bold')).grid(row=0,column=0,padx=10)
            lbl_name = Label(frame,image=Endcrocrinology,border=0,justify='center').place(x=430,y=20)

        if(row[2]==6):
            messagebox.showinfo("allowed","allowed to view neurosurery report")
            log_button = Button(view_frame,text='Neurosurgery',border=3,bg='light yellow',fg='black',font=('times',19,'bold'),command=Neu)
            log_button.place(x=3,y=310,width=305)

        database.commit()
        database.close()

    log_button = Button(log_frame,text='LOGIN',border=3,bg='light yellow',fg='black',font=('times',15,'bold'),command=check,padx=10)
    log_button.place(x=205,y=230)

Report_btn = Button(Btn_frame,bg="light yellow",fg="black",border=2,text="View Report",font=("times",19,"bold"),activebackground="light blue",command=ReportCall)
Report_btn.place(x=890,y=0,width=305)



root.mainloop()