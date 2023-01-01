import tkinter as tk
import tkinter.messagebox
import csv

class User:
    def __init__(self, id, username, password, sex, address, tel):
        self.id = id
        self.username = username
        self.password = password
        self.sex = sex
        self.address = address
        self.tel = tel
class UserStock:
    def __init__(self, account_list):
        self.accounts = account_list

def read_user_w():
    with open("Userdata.csv", "r", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        user_w_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            user_cur = User(row[0], row[1], row[2], row[3], row[4], row[5])
            user_w_list.append(user_cur)
    return user_w_list

def read_account():
    with open("Userdata.csv", "r", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        account_dict = {}
        for row in csv_reader:
            if row[1] == "用户名":
                continue
            account_dict[row[1]] = row[2]

    return account_dict

def read_admin_account():
    with open("Admindata.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)
        admin_account_dict = {}
        for row in csv_reader:
            if row[1] == "用户名":
                continue
            admin_account_dict[row[1]] = row[2]

    return  admin_account_dict

def readUsername():
    with open('Userdata.csv', encoding='gbk') as csvfile:
        data = csv.reader(csvfile)
        Userdata = {}
        for row in data:
            Userdata[row[1]] = 0
    return Userdata

def readUsernameReg():
    with open('UserdataReg.csv', encoding='gbk') as csvfile:
        data = csv.reader(csvfile)
        UserdataReg = {}
        for row in data:
            UserdataReg[row[1]] = 0
    return UserdataReg

def read_last_id(filename):
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        li = []
        for row in csv_reader:
            li.append(row[0])
        if li == ['id']:
            return 0
        else:
            return int(li[-1])

def write_in_csv(filename, username, password, sex, address, tel):
    with open(filename,mode='w',newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([read_last_id("Userdata.csv")+1, username, password, sex, address, tel])

def openWindow():
    window = tk.Tk()
    window.title("你帮我助疫情物品交换平台")
    window.geometry("1000x500")
    tk.Label(window, text="你帮我助疫情物品交换平台",font=("黑体", 28)).place(relx=0.5, rely=0.18, anchor=tk.CENTER)
    tk.Label(window, text="用户名：", font=("宋体",18)).place(relx=0.35, rely=0.35)
    tk.Label(window, text="密码：", font=("宋体",18)).place(relx=0.35, rely=0.52)
    tk.Label(window, text="开发者：杨桦\nversion:2.0",font=("宋体", 14)).place(relx=1, rely=1, anchor=tk.SE)
    username = tk.Entry(window,width=30)
    username.place(relx=0.44, rely=0.35)
    password = tk.Entry(window,width=30)
    password.place(relx=0.44, rely=0.52)

    account_d = {'acc':''}
    dict_a = {}
    def login():
        dict_a['state'] = ad_v.get()
        account_dict = read_account()
        ad_account_dict = read_admin_account()
        account_cur = username.get()
        password_cur = password.get()
        if ad_v.get() == 1:
            if account_cur == "":
                tk.messagebox.showerror('error', '用户名不能为空')
            else:
                if password_cur == "":
                    tk.messagebox.showerror('error', '密码不能为空')
                else:
                    if account_cur not in account_dict.keys():
                        tk.messagebox.showerror('error', '用户名未注册或等待审核通过')
                    else:
                        if account_dict[account_cur] != password_cur:
                            tk.messagebox.showerror('error', '密码错误')
                        else:
                            account_d['acc'] = account_cur
                            window.destroy()


        elif ad_v.get() == 0:
            if account_cur == "":
                tk.messagebox.showerror('error', '用户名不能为空')
            else:
                if password_cur == "":
                    tk.messagebox.showerror('error', '密码不能为空')
                else:
                    if account_cur not in ad_account_dict.keys():
                        tk.messagebox.showerror('error', '用户名未注册')
                    else:
                        if ad_account_dict[account_cur] != password_cur:
                            tk.messagebox.showerror('error', '密码错误')
                        else:
                            account_d['acc'] = account_cur
                            window.destroy()

    def register():
        regwindow = tk.Tk()
        regwindow.title("注册系统")
        regwindow.geometry("800x400")
        tk.Label(regwindow, text="你帮我助疫情物品交换平台\n注册系统",font=("黑体", 28)).place(relx=0.5, rely=0.18, anchor=tk.CENTER)
        tk.Label(regwindow, text="用户名：", font=("宋体",14)).place(relx=0.25, rely=0.35)
        tk.Label(regwindow, text="密码：", font=("宋体",14)).place(relx=0.25, rely=0.45)
        tk.Label(regwindow, text="性别：", font=("宋体",14)).place(relx=0.25, rely=0.55)
        tk.Label(regwindow, text="住址：", font=("宋体",14)).place(relx=0.25, rely=0.65)
        tk.Label(regwindow, text="联系方式：", font=("宋体",14)).place(relx=0.25, rely=0.75)
        usernameRegEntry = tk.Entry(regwindow,width=25)
        usernameRegEntry.place(relx=0.5, rely=0.35)
        passwordRegEntry = tk.Entry(regwindow,width=25)
        passwordRegEntry.place(relx=0.5, rely=0.45)
        sexRegEntry = tk.Entry(regwindow,width=25)
        sexRegEntry.place(relx=0.5, rely=0.55)
        addressRegEntry = tk.Entry(regwindow,width=25)
        addressRegEntry.place(relx=0.5, rely=0.65)
        telRegEntry = tk.Entry(regwindow,width=25)
        telRegEntry.place(relx=0.5, rely=0.75)

        usernameDic = readUsername()
        usernameRegDic = readUsernameReg()
        def registerButton():
            usernameReg = usernameRegEntry.get()
            passwordReg = passwordRegEntry.get()
            sexReg = sexRegEntry.get()
            addressReg = addressRegEntry.get()
            telReg = telRegEntry.get()
            if usernameReg in usernameDic.keys():
                tk.messagebox.showerror('error', '用户名已被注册')
            elif usernameReg in usernameRegDic.keys():
                tk.messagebox.showerror('error', '该账号正在等待管理员审核通过')
            elif not usernameReg:
                tk.messagebox.showerror('error', '用户名不能为空')
            else:
                if not passwordReg:
                    tk.messagebox.showerror('error', '密码不能为空')
                else:
                    if not sexReg:
                        tk.messagebox.showerror('error', '性别不能为空')
                    else:
                        if not addressReg:
                            tk.messagebox.showerror('error', '地址不能为空')
                        else:
                            if not telReg:
                                tk.messagebox.showerror('error', '联系方式不能为空')
                            else:
                                write_in_csv("UserdataReg.csv", usernameReg, passwordReg, sexReg, addressReg, telReg)
                                tk.messagebox.showinfo('通知', '已提交注册申请，请等待管理员审核通过')
                                regwindow.destroy()

        tk.Button(regwindow, text='注册', command=registerButton).place(relx=0.5, rely=0.9, width=100, height=36, anchor=tk.CENTER)

    ad_v = tk.IntVar()
    tk.Radiobutton(window, text="管理员", variable=ad_v, value=0).place(relx=0.43, rely=0.65, anchor=tk.CENTER)
    tk.Radiobutton(window, text="普通用户", variable=ad_v, value=1).place(relx=0.58, rely=0.65, anchor=tk.CENTER)
    tk.Button(window, text='登录', command=login).place(relx=0.4, rely=0.8, width=100, height=36, anchor=tk.CENTER)
    tk.Button(window, text='注册', command=register).place(relx=0.6, rely=0.8, width=100, height=36, anchor=tk.CENTER)

    window.mainloop()

    return dict_a['state'], account_d['acc']