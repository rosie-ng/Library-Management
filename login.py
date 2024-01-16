# login.py
from Viewqltv import NewWindow, CustomEntry
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import main

class Login(NewWindow):
    def __init__(self):
        super().__init__()
        self.login_successful = False
        self.title("Login")
        self.resizable(False, False)

        self.top_image = PhotoImage(file='icons/library.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text='  Đăng nhập ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)
        # Create username label and entry
        username_label = ttk.Label(self.bottomFrame, text="Tài khoản:")
        username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = CustomEntry(self.bottomFrame, placeholder="Tài khoản")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create password label and entry
        password_label = ttk.Label(self.bottomFrame, text="Mật khẩu:")
        password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = CustomEntry(self.bottomFrame, placeholder="Mật khẩu")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create login button
        login_button = ttk.Button(self.bottomFrame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.login_successful = True
            messagebox.showinfo("Success", "Đang đăng nhập", icon='info')
            self.destroy()
            main.Viewqltv().start() # Vấn đề nằm ở đây
        else:
            messagebox.showerror("Error", "Tài khoản hoặc mật khẩu không đúng", icon='warning')


if __name__ == '__main__':
    login_window = Login()
    login_window.mainloop()