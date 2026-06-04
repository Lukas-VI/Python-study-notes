#TK
import tkinter as tk
from tkinter import messagebox

# 预设用户名和密码
USERNAME = "admin"
PASSWORD = "114514"

def login():
    user = entry_user.get()
    pwd = entry_pwd.get()
    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("提示", "欢迎进入")
    else:
        messagebox.showerror("错误", "用户名和密码错误")

def reset():
    entry_user.delete(0, tk.END)
    entry_pwd.delete(0, tk.END)

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("用户登录")
root.geometry("300x180")

tk.Label(root, text="用户名:").place(x=40, y=40)
entry_user = tk.Entry(root)
entry_user.place(x=110, y=40)

tk.Label(root, text="密码:").place(x=40, y=80)
entry_pwd = tk.Entry(root, show="*")
entry_pwd.place(x=110, y=80)

btn_login = tk.Button(root, text="登录", width=8, command=login)
btn_login.place(x=40, y=130)

btn_reset = tk.Button(root, text="重置", width=8, command=reset)
btn_reset.place(x=120, y=130)

btn_quit = tk.Button(root, text="退出", width=8, command=quit_app)
btn_quit.place(x=200, y=130)

root.mainloop()