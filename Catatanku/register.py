from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector


def connectdb():
    if emailEntry.get() == '' or unameEntry.get() == '' or passEntry.get() == '':
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
            messagebox.showerror('Error', 'Database Connectivity Issue!')
            return
        
        try:
            query = 'CREATE DATABASE user_data'
            mycursor.execute(query)
            query = 'USE user_data'
            mycursor.execute(query)
        except:
            mycursor.execute('USE user_data')

        query = 'SELECT * FROM pengguna WHERE username=%s'
        mycursor.execute(query,(unameEntry.get(),))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exists!')
        else:
            query = 'INSERT INTO pengguna(email, username, password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), unameEntry.get(), passEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success!', 'Register Success!')
            register_window.destroy()
            import login

def hide_button():
    view.config(file='hide.png')
    passEntry.config(show='*')
    viewButton.config(command=show_button)

def show_button():
    view.config(file='view.png')
    passEntry.config(show='')
    viewButton.config(command=hide_button)

def main_page():
    register_window.destroy()
    import main



register_window = Tk()
register_window.title('Catatanku')
register_window.geometry('500x500')
register_window.resizable(0,0)

register_heading = Label(register_window, text='Register', font=('Open Sans', 16))
register_heading.place(x=200, y=50)

#Email Entry
emailLabel = Label(register_window, text='Email :', font=('Open Sans', 11))
emailLabel.place(x=70, y=135)

emailEntry = Entry(register_window, width=30, font=('Open Sans', 11))
emailEntry.place(x=165, y=135)

#Username Entry
unameLabel = Label(register_window, text='Username :', font=('Open Sans', 11))
unameLabel.place(x=70, y=190)

unameEntry = Entry(register_window, width=30, font=('Open Sans', 11))
unameEntry.place(x=165, y=190)

#Password Entry
passLabel = Label(register_window, text='Password :', font=('Open Sans', 11))
passLabel.place(x=70, y=245)

passEntry = Entry(register_window, width=30, font=('Open Sans', 11), show='*')
passEntry.place(x=165, y=245)

#View / Hide Password
view = PhotoImage(file='hide.png')

viewButton = Button(register_window, image=view, bd=0, command=show_button)
viewButton.place(x=420,y=240)

#Confirm Button
confirmButton = Button(register_window, text='Confirm', font=('Open Sans', 16), command=connectdb)
confirmButton.place(x=200,y=350)

#Button Kembali
kembaliButton = Button(register_window, text='Back', font=('Open Sans', 10), command=main_page)
kembaliButton.place(x=40, y=450)



register_window.mainloop()