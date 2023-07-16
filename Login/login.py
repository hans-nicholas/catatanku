from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part

def forget_pass():
    window = Toplevel()
    window.title('Change Password')

    window.main()





def login_user():
    if usernameEntry.get() == '' or passwordEntry.get == '':
        messagebox.showerror('Error!', 'Please fill all the fields!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='2002')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error!', 'Conection is not established, Try Again!')
            return
        
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error!', 'Invalid username or password!')
        else:
            messagebox.showinfo('Welcome!', 'Login is successful!')


def USER_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def PASS_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
   openeye.config(file='openeye.png') 
   passwordEntry.config(show='')
   eyeButton.config(command=hide)

def signup_page():
    login_window.destroy()
    import signup



#GUI Part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Times New Roman', 23, 'bold'), bg='white')
heading.place(x=605, y=120)

#Username Entry
usernameEntry = Entry(login_window, width=30,font=('',11,'bold'), bd=0)
usernameEntry.place(x=605, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', USER_enter)

frame1 = Frame(login_window, width=250, height=2, bg='black')
frame1.place(x=580, y=222)

#Password Entry
passwordEntry = Entry(login_window, width=30, font=('',11,'bold'), bd=0)
passwordEntry.place(x=605, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', PASS_enter)

frame2 = Frame(login_window, width=250, height=2, bg='black')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white'
                 ,cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

#Forget Password
forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white',font=('',9, 'bold')
                 ,cursor='hand2',fg='red', activeforeground='red', command=forget_pass)
forgetButton.place(x=715, y=295)

#Login Button
loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
                     fg='white', bg='firebrick1', activebackground='firebrick1', activeforeground='white', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)


orLabel = Label(login_window,text='--------------- OR ---------------', font=('Open Sans', 16), bg='white')
orLabel.place(x=575,y=400)

#LOGOS
facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

signupLabel = Label(login_window,text='Dont have an account?', font=('Open Sans',9), bg='white')
signupLabel.place(x=590,y=500)

#New Account Button
newaccountButton = Button(login_window, text='Create New One', font=('Open Sans', 9, 'bold underline'),
                     fg='blue', bg='white', activebackground='white', activeforeground='blue', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=720, y=500)


login_window.mainloop()