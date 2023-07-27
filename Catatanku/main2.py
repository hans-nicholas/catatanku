import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.access_code = '2002'

        self.geometry('400x150')
        self.title('Login')

        frame_login = ttk.Frame(self)
        frame_login.pack(fill=tk.BOTH, expand=True)

        lbl_login = tk.Label(frame_login, text='Access Code : ', font=('Times New Roman', 14))
        lbl_login.pack(pady=10)

        self.code_entry = ttk.Entry(frame_login, width=30, show='*')
        self.code_entry.pack(pady=10)

        self.submit_btn = tk.Button(text='ENTER', command=self.access_granted)
        self.submit_btn.pack(pady=20)

    def access_granted(self):
        if self.code_entry.get() == self.access_code:
            messagebox.showinfo('Access Granted!', 'Login Successful!, Welcome Hans')
            self.destroy
            MainWindow()

        else:
            messagebox.showerror('Access Denied!', 'Wrong Access Code!')
            self.destroy()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.title('Catatanku')

        frame_main = ttk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True)

        btn_buat_catatan = tk.Button(frame_main, text='Buat Catatan', font=('Times new roman', 16))
        btn_buat_catatan.place(x=100, y=170)

        btn_buka_catatan = tk.Button(frame_main, text='Buka Catatan', font=('Times new roman', 16))
        btn_buka_catatan.place(x=275, y=170)

        uname_label = tk.Label('Hi, Hans Nicholas!')
        uname_label.pack()
        

if __name__ == '__main__':
    login_window = LoginWindow()
    login_window.mainloop()