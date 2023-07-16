from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector


def main_page():
    login_window.destroy()
    import main

def login_user():
    if unameEntry.get() == '' or passEntry.get() == '':
        messagebox.showerror('Error!', 'Please fill all the fields!')
    else:
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='2002'
            )
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error!', 'Connection is not established, Try Again!')
            return
        
        query = 'USE user_data'
        mycursor.execute(query)
        query = 'SELECT * FROM pengguna WHERE username=%s AND password=%s'
        mycursor.execute(query, (unameEntry.get(), passEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error!', 'Incalid Username or Password!')
        else:
            messagebox.showinfo('Welcome!', 'Login is Successful!')
            login_window.destroy()
            import home


def hide_button():
    view.config(file='hide.png')
    passEntry.config(show='*')
    viewButton.config(command=show_button)

def show_button():
    view.config(file='view.png')
    passEntry.config(show='')
    viewButton.config(command=hide_button)
    

#Window
login_window = Tk()
login_window.title('Catatanku')
login_window.geometry('500x500')
login_window.resizable(0,0)

login_heading = Label(login_window, text='Login', font=('Open Sans', 23))
login_heading.place(x=220, y=50)

#Username Entry
unameLabel = Label(login_window, text='Username :', font=('Open Sans', 11))
unameLabel.place(x=70,y=150)

unameEntry = Entry(login_window, width=30, font=('Open Sans', 11))
unameEntry.place(x=165,y=150)


#Password Entry
passLabel = Label(login_window, text='Password :', font=('Open Sans', 11))
passLabel.place(x=70,y=200)

passEntry = Entry(login_window, width=30, font=('Open Sans', 11), show='*')
passEntry.place(x=165, y=200)

#View / Hide Button
view = PhotoImage(file='hide.png')

viewButton = Button(login_window, image=view, bd=0, command=show_button)
viewButton.place(x=420,y=200)

#Login Button
loginButton = Button(login_window, text='Login', font=('Open Sans', 16), command=login_user)
loginButton.place(x=230, y=255)

#Button Kembali
kembaliButton = Button(login_window, text='Back', font=('Open Sans', 10), command=main_page)
kembaliButton.place(x=40, y=450)

login_window.mainloop()