import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import csv
from openwindow import User, UserStock

def read_type_c():
    with open('types.csv', encoding='gbk', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        type_dict = {}
        for row in csv_reader:
            cha_l = row[1].split(sep='，')
            type_dict[row[0]] = cha_l
    return type_dict

def update_a(t, Users):
    for child in t.get_children():
        t.delete(child)
    for item in Users.accounts:
        t.insert('', tk.END, values=(item.id, item.username, item.password, item.sex, item.address, item.tel))

def update_ty(t, type_dict):
    for child in t.get_children():
        t.delete(child)
    for type in list(type_dict.keys()):
        t.insert('', tk.END, values=(type, type_dict[type]))

def read_user_w():
    with open("UserdataReg.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        user_w_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            user_cur = User(row[0], row[1], row[2], row[3], row[4], row[5])
            user_w_list.append(user_cur)
    return user_w_list

def read_last_id(filename):
    with open(filename, encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)
        li = []
        for row in csv_reader:
            li.append(row[0])
        if li == ['id']:
            return 0
        else:
            return int(li[-1])

def write_in_csv(filename, user):
    with open(filename, "a", encoding='gbk', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([read_last_id('Userdata.csv') + 1, user.username, user.password, user.sex, user.address, user.tel])

def write_in_type(ty_cur, cha_cur):
    with open('types.csv', "a", encoding='gbk', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([ty_cur, cha_cur])

def delete_item_csv(item_index, filename):
    r = csv.reader(open(filename, encoding='gbk', newline=''))
    lines = list(r)
    for line in lines:
        if line[0] == str(item_index):
            lines.remove(line)
            break
    writer = csv.writer(open(filename, 'w', encoding='gbk', newline=''))
    writer.writerows(lines)

def adminwindow():
    adminWindow = tk.Tk()
    adminWindow.title('你帮我助疫情物品交换平台管理界面')
    adminWindow.geometry("800x700")

    tk.Label(adminWindow, text='等待审核通过用户', font=("黑体",20)).place(x=400,y=390, anchor=tk.CENTER)
    columns = ['ID','用户名','密码','性别','住址','电话']
    tree = ttk.Treeview(adminWindow, show="headings", height=10, columns=columns)
    tree.column('ID', width=40, anchor=tk.CENTER,stretch=False)
    tree.column('用户名', width=120, anchor=tk.CENTER)
    tree.column('密码', width=120, anchor=tk.CENTER)
    tree.column('性别', width=40, anchor=tk.CENTER)
    tree.column('住址', width=145, anchor=tk.CENTER)
    tree.column('电话', width=145, anchor=tk.CENTER)
    tree.heading('ID', text='ID')
    tree.heading('用户名', text='用户名')
    tree.heading('密码', text='密码')
    tree.heading('性别', text='性别')
    tree.heading('住址', text='住址')
    tree.heading('电话', text='电话')
    tree.place(x=50, y=420)

    UserS = UserStock(read_user_w())
    update_a(tree, UserS)
    def agree_ac():
        res = tk.messagebox.askyesnocancel('确认', '是否通过该用户注册？')
        if res:
            item_index = tree.item(tree.selection()[0], "values")[0]
            for user_cur in UserS.accounts:
                if user_cur.id == item_index:
                    break
            user_append = user_cur
            UserS.accounts.remove(user_cur)
            update_a(tree, UserS)
            write_in_csv('Userdata.csv', user_append)
            delete_item_csv(item_index, 'UserdataReg.csv')

    ag_button = tk.Button(adminWindow, text='通过注册', background='white',command=agree_ac).place(x=200, y=660)

    def refuse_ac():
        res = tk.messagebox.askyesnocancel('警告！', '是否拒绝该用户注册？')
        if res:
            item_index = tree.item(tree.selection()[0], "values")[0]
            for user_cur in UserS.accounts:
                if user_cur.id == item_index:
                    break
            UserS.accounts.remove(user_cur)
            update_a(tree, UserS)
            delete_item_csv(item_index, 'UserdataReg.csv')

    refu_button = tk.Button(adminWindow, text='拒绝注册', background='white',command=refuse_ac).place(x=500, y=660)

    tk.Label(adminWindow, text='更改物品类型', font=("黑体",20)).place(x=400,y=45, anchor=tk.CENTER)

    tk.Label(adminWindow,text="新的类型名称：", font=("宋体",14)).place(x=50, y=75)
    type_entry = tk.Entry(adminWindow,width=15)
    type_entry.place(x=175, y=75)

    tk.Label(adminWindow,text="新的类型属性：", font=("宋体",14)).place(x=350, y=75)
    addr = tk.StringVar()
    cha_entry = tk.Entry(adminWindow,width=27, textvariable=addr)
    cha_entry.place(x=500, y=75)
    tk.Label(adminWindow,text="（用中文逗号隔开不同的属性）", font=("宋体",10)).place(x=480, y=105)


    tree2 = ttk.Treeview(adminWindow, show="headings", height=8, columns=['物品类型', '物品属性'])
    tree2.column('物品类型', width=170, anchor=tk.CENTER)
    tree2.column('物品属性', width=460, anchor=tk.CENTER)
    tree2.heading('物品类型', text='物品类型')
    tree2.heading('物品属性', text='物品属性')
    tree2.place(x=50, y=160)
    type_dic_s = read_type_c()
    update_ty(tree2, type_dic_s)

    def add_type():
        ty_cur = type_entry.get()
        char_cur = cha_entry.get()
        if not ty_cur:
            tk.messagebox.showerror('未输入类型', '请输入要添加的物品类型！')
        elif ty_cur in list(type_dic_s.keys()):
            tk.messagebox.showerror('类型已存在', '该物品类型已存在！')
        else:
            if char_cur == "（用'，'区分不同属性）":
                tk.messagebox.showerror('未输入属性', '请输入该类型的属性！')
            elif '。' in char_cur or ',' in char_cur or '.' in char_cur or '？' in char_cur or '!' in char_cur:
                tk.messagebox.showerror('分隔符错误', '请使用中文逗号作为属性间的分隔符！')
            else:
                type_dic_s[ty_cur] = char_cur.split(sep='，')
                write_in_type(ty_cur, char_cur)
                update_ty(tree2, type_dic_s)

    type_e_button = tk.Button(adminWindow, text='确认添加',command=add_type).place(x=705, y=70)

    def corr_type():
        item_index = tree2.item(tree2.selection()[0], "values")[0]
        newWin =tk.Tk()
        newWin.title('修改 {} 类型'.format(item_index))
        newWin.geometry("600x300")

        tk.Label(newWin, text="修改后的类型名称：", font=("宋体", 14)).place(x=50, y=40)
        ty_entry = tk.Entry(newWin, width=18)
        ty_entry.place(x=185, y=40)
        tk.Label(newWin, text="修改后的类型属性：", font=("宋体", 14)).place(x=50, y=80)
        c_entry = tk.Entry(newWin, width=18)
        c_entry.place(x=185, y=80)

        def return_ty():
            type_n = ty_entry.get()
            c_n = c_entry.get()
            if not type_n:
                tk.messagebox.showerror('未输入类型', '请输入要修改的物品类型！')
            elif type_n in list(type_dic_s.keys()) and type_n != item_index:
                tk.messagebox.showerror('类型已存在', '该物品类型已存在！')
            else:
                if not c_n:
                    tk.messagebox.showerror('未输入属性', '请输入该类型的属性！')
                elif '。' in c_n or ',' in c_n or '.' in c_n or '？' in c_n or '!' in c_n:
                    tk.messagebox.showerror('分隔符错误', '请使用中文逗号作为属性间的分隔符！')
                else:
                    del type_dic_s[item_index]
                    delete_item_csv(item_index, 'types.csv')
                    type_dic_s[type_n] = c_n.split(sep='，')
                    write_in_type(type_n, c_n)
                    update_ty(tree2, type_dic_s)
                    newWin.destroy()

        check_bu = tk.Button(newWin, text='确认修改',command=return_ty).place(x=200,y=150, anchor=tk.CENTER)

    correct_button = tk.Button(adminWindow, text='修改该类型',command=corr_type).place(x=715, y=155)

    def delete_type():
        item_index = tree2.item(tree2.selection()[0], "values")[0]
        del type_dic_s[item_index]
        delete_item_csv(item_index, 'types.csv')
        update_ty(tree2, type_dic_s)

    delete_button = tk.Button(adminWindow, text='删除该类型',command=delete_type).place(x=715, y=185)


    def exit_window():
        res = tk.messagebox.askyesnocancel('警告','是否退出软件？')
        if res:
            adminWindow.destroy()

    exit_button = tk.Button(adminWindow, text='退出软件',command=exit_window).place(x=800, y=700, width=100, height=36, anchor=tk.SE)
    adminWindow.mainloop()