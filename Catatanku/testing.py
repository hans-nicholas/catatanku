from tkinter import *
from tkinter import messagebox
import mysql.connector

# def main():
#     #Membuat form utama
#     mainform = Tk()

#     #MEMBUAT OBJEK BUTTON
#     btn = Button(mainform)

#     #Mengubah warna form
#     btn['text'] = 'Klik Saya'
#     btn['background'] = '#66ccff'

#     #Menempatkan kontrol ke dalam form
#     #Menggunakan Pack Manager
#     btn.pack(padx=30, pady=30)

#     #menampilkan form
#     mainform.mainloop()
# if __name__ == '__main__':
#     main()


#   Membuat kelas DemoFrame
# yang diturunkan dari kelas Frame
# class DemoFrame(Frame):
#     #konstruktor DemoFrame
#     def __init__(self, master=None):
#         #memanggil konstruktor kelas induk (Frame)
#         Frame.__init__(self, master)
#         self.grid()
#         self.buatKontrol()

#         #membuat dan menempatkan kontrol ke dalam frame
#     def buatKontrol(self):
#         self.btnKeluar = Button(self, text='Keluar', command=self.quit)
#         self.btnKeluar.grid(sticky=E, padx=90, pady=90)

# def main():
#     # Membuat keasd DemoFrame
#     app = DemoFrame()
#     app.mainloop()

# if __name__ == '__main__':
#     main()


import mysql.connector

# try:
#     # Ganti 'user', 'password', 'host', dan 'database' sesuai dengan pengaturan database Anda
#     connection = mysql.connector.connect(
#         user='root',
#         password='2002',
#         host='localhost',
#         database='user_data'
#     )
#     print("Koneksi ke database berhasil.")
#     connection.close()
# except mysql.connector.Error as err:
#     print(f"Error: {err}")


conn = mysql.connector.connect(
    user='root',
    host='localhost',
    password='2002',
    database='user_data'
)

cur = conn.cursor()

#Membaca data
cur.execute('SELECT * FROM pengguna')
result = cur.fetchall()
