from tkinter import *
from tkinter import messagebox
import mysql.connector


def register_page():
    main_window.destroy()
    import register

def login_page():
    main_window.destroy()
    import login

#Membuat Window
main_window = Tk()
main_window.title('Catatanku')
main_window.resizable(0,0)
main_window.geometry('500x500')

#Membuat Button
#Register Button
registerButton = Button(main_window, text='Register', font=('Open Sans', 16), command=register_page)
registerButton.place(x=100,y=200)

#Login Button
loginButton = Button(main_window, text='Login', font=('Open Sans', 16), command=login_page)
loginButton.place(x=300,y=200)


main_window.mainloop()
