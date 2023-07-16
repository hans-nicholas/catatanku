from tkinter import *
from PIL import ImageTk



def USER_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def PASS_enter(event):
    if newpasswordEntry.get() == 'New Password':
        newpasswordEntry.delete(0, END)

def CONFIRM_enter(event):
    if confirmpassEntry.get() == 'Confirm Password':
        confirmpassEntry.delete(0,END)

resetpass_window = Tk()
resetpass_window.geometry('990x660+50+50')
resetpass_window.resizable(0, 0)
resetpass_window.title('Reset Password')
bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(resetpass_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(resetpass_window, text='RESET PASSWORD', font=('Times New Roman', 15, 'bold'), bg='white')
heading.place(x=605, y=120)


#Username Entry
usernameEntry = Entry(resetpass_window, width=30, font=('', 11, 'bold'), bd=0)
usernameEntry.place(x=605, y= 200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', USER_enter)

frame1 = Frame(resetpass_window, width=250, height=2, bg='black')
frame1.place(x=580, y=222)


#New Password Entry
newpasswordEntry = Entry(resetpass_window, width=30, font=('', 11,'bold'), bd=0)
newpasswordEntry.place(x=605, y=260)
newpasswordEntry.insert(0, 'New Password')

newpasswordEntry.bind('<FocusIn>', PASS_enter)

frame2 = Frame(resetpass_window, width=250, height=2, bg='black')
frame2.place(x=580, y=282)


#Confirm Password
confirmpassEntry = Entry(resetpass_window, width=30, font=('', 11, 'bold'), bd=0)
confirmpassEntry.place(x=605, y=320)
confirmpassEntry.insert(0, 'Confirm Password')

confirmpassEntry.bind('<FocusIn>', CONFIRM_enter)

frame3 = Frame(resetpass_window, width=250, height=2, bg='black')
frame3.place(x=580, y=342)


#Submit Button
submitButton = Button(resetpass_window, text='Submit', font=('Open Sans', 16, 'bold'), 
                      fg='white', bg='firebrick1', activebackground='firebrick1', activeforeground='white', cursor='hand2', bd=0, width=19)
submitButton.place(x=575, y=400)

resetpass_window.mainloop()