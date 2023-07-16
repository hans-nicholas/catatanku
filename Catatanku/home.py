from tkinter import *
from tkinter import messagebox
import mysql.connector


#Membuat window
home_window = Tk()
home_window.title('Catatanku')
home_window.resizable(0,0)
home_window.geometry('500x500')

#Membuat Button
#Buat Catatan Button
buatButton = Button(home_window, text='Buat Catatan', font=('Open Sans', 16))
buatButton.place(x=80,y=200)

#Lihat Catatan Button
lihatButton = Button(home_window, text='Lihat Catatan', font=('Open Sans', 16))
lihatButton.place(x=270,y=200)


home_window.mainloop()