import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import csv
import ast
from openwindow import User, UserStock

class Product:
    def __init__(self, id, name, intro, address, phonenumber, type, charact, master):
        self.id = id
        self.name = name
        self.intro = intro
        self.address = address
        self.phonenumber = phonenumber
        self.type = type
        self.charact = charact
        self.master = master

class Stock(object):
    def __init__(self, goods):
        self.goods = goods

    def Add(self, product):
        self.goods.append(product)

    def Search(self):
        name = input('What product do you want to search for?')
        flag = False
        for i in range(len(self.goods)):
            if self.goods[i].name == name:
                flag = True
                break
        if flag == True:
            print('The product you want to search is here:')
            print('-' * 50)
            for i in range(len(self.goods)):
                if self.goods[i].name == name:
                    print('Product:' + self.goods[i].name + '     Supplier:' + self.goods[i].master)
        else:
            print('There is no such product.')

    def ListAll(self):
        if len(self.goods) == 0:
            print('There is nothing!')
        else:
            print('-' * 20 + 'The Stock List' + '-' * 20)
            for i in range(len(self.goods)):
                    print('Product:'+ self.goods[i].name + '     Supplier:' + self.goods[i].master)

    def UserAdd(self):
        name = input('please enter product:')
        master = input('please enter your name:')
        p = Product(name, master)
        self.Add(p)

    def UserDelete(self):
        print('Please enter the information of product which you want to delete.')
        name = input('please enter your product:')
        master = input('please enter your name:')
        for item in self.goods:
            if name == item.name and master == item.master:
                self.goods.remove(item)


def read_user_w():
    with open("Username.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # ??????csv.reader??????csvfile????????????
        user_w_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            user_cur = User(row[0], row[1], row[2], row[3], row[4], row[5])
            user_w_list.append(user_cur)
    return user_w_list

def read_stock():
    with open("stock.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # ??????csv.reader??????csvfile????????????
        project_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            if row[6]:
                chara = ast.literal_eval(row[6])
            pro_cur = Product(row[0], row[1], row[2], row[3], row[4], row[5], chara, row[7])
            project_list.append(pro_cur)
    return project_list

def read_types():
    with open('types.csv', encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)
        type_list = []
        type_dict = {}
        for row in csv_reader:
            type_list.append(row[0])
            type_dict[row[0]] = row[1]
        return type_list, type_dict

def write_csv(filename, product):
    with open(filename, "a", encoding='gbk', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([product.id, product.name, product.intro, product.address, product.phonenumber, product.type, product.charact, product.master])

def search_product(stock, index):
    for pro in stock.goods:
        if pro.id == index:
            goal_pro = pro
            return goal_pro
        else:
            return None

project_list = read_stock()
stockIni = Stock(project_list)
def update_stock(t, stock):
    for child in t.get_children():
        t.delete(child)
    for item in stock.goods:
        t.insert('', tk.END, values=(item.id, item.name, item.intro, item.address,item.type, item.master, item.phonenumber))


def userwindow(user):
    mainWindow = tk.Tk()
    mainWindow.title("??????????????????????????????????????????")
    mainWindow.geometry("900x600")

    columns = ['??????id','????????????','????????????','????????????','????????????','???????????????','???????????????']
    tree = ttk.Treeview(mainWindow, show="headings", height=24, columns=columns)
    tree.column('??????id', width=40, anchor=tk.CENTER,stretch=False)
    tree.column('????????????', width=60, anchor=tk.CENTER)
    tree.column('????????????', width=100, anchor=tk.CENTER)
    tree.column('????????????', width=80, anchor=tk.CENTER)
    tree.column('????????????', width=80, anchor=tk.CENTER)
    tree.column('???????????????', width=80, anchor=tk.CENTER)
    tree.column('???????????????', width=120, anchor=tk.CENTER)

    tree.heading('??????id', text='ID')
    tree.heading('????????????', text='????????????')
    tree.heading('????????????', text='??????')
    tree.heading('????????????', text='????????????')
    tree.heading('????????????', text='????????????')
    tree.heading('???????????????', text='???????????????')
    tree.heading('???????????????', text='???????????????')
    update_stock(tree, stockIni)

    tree.place(x=340, y=0)

    tk.Label(mainWindow,text="???????????????", font=("??????",14)).place(x=50, y=60)
    tk.Label(mainWindow,text="???????????????", font=("??????",14)).place(x=50, y=90)
    tk.Label(mainWindow, text="??????????????????", font=("??????", 14)).place(x=50, y=120)
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()
    v4 = tk.StringVar()
    name_entry = tk.Entry(mainWindow,width=20,textvariable=v1)
    name_entry.place(x=160, y=60)
    dri_entry = tk.Entry(mainWindow,width=20,textvariable=v2)
    dri_entry.place(x=160, y=90)
    add_entry = tk.Entry(mainWindow, width=20,textvariable=v3)
    add_entry.place(x=160, y=120)

    type_list, type_dict = read_types()
    tk.Label(mainWindow, text="???????????????", font=("??????", 14)).place(x=50, y=30)
    type_Box = ttk.Combobox(mainWindow, height=5, width=13, state='readonly', font=("??????", 14),
                              values=type_list)
    type_Box.place(x=160, y=30)
    #??????????????????

    chara_dic = {}

    def upda():
        update_stock(tree,stockIni)
        v1.set("")
        v2.set("")
        v3.set("")
        v4.set("")

    updatee_Button = tk.Button(mainWindow, text='????????????',command=upda).place(x=900, y=560, width=100, height=36, anchor=tk.SE)


    def fill_chara():
        chara_dic.clear()
        if not type_Box.get():
            tk.messagebox.showerror('?????????????????????', '????????????????????????')

        else:
            new_win = tk.Tk()
            new_win.title('??????????????????')
            chara_l = type_dict[type_Box.get()].split(sep='???')

            new_win.geometry("350x300")
            entry_list = []
            for i in range(len(chara_l)):
                tk.Label(new_win, text="{}???".format(chara_l[i]), font=("??????", 14)).place(x=50, y=20+30*i)
                ch_entry = tk.Entry(new_win, width=15)
                ch_entry.place(x=120, y=20+30*i)
                entry_list.append(ch_entry)

            def check():
                j = 0
                for char in chara_l:
                    if not entry_list[j].get():
                        tk.messagebox.showwarning('????????????', '?????????????????????{}??????'.format(chara_l[j]))
                        fill_chara()
                        break
                    else:
                        chara_dic[char] = entry_list[j].get()
                        j = j + 1
                new_win.destroy()

            en_button = tk.Button(new_win, text='??????', command=check)
            en_button.place(x=155, y=80+30*i, anchor=tk.CENTER)
    element_button = tk.Button(mainWindow, text='??????????????????',command=fill_chara)
    element_button.place(x=900, y=440, width=150, height=36, anchor=tk.E)

    def show_detail():

        try:
            item_index = tree.item(tree.selection()[0], "values")[0]
        except IndexError:
            tk.messagebox.showerror('?????????', '??????????????????????????????????????????')
        else:
            stockIni = Stock(read_stock())
            for pro in stockIni.goods:
                if pro.id == item_index:
                    break
            new_win = tk.Tk()
            new_win.title('{} ????????????'.format(pro.name))
            new_win.geometry("350x300")
            for i in range(len(pro.charact)):
                tk.Label(new_win, text="{}???".format(list(pro.charact.keys())[i]), font=("??????", 14)).place(x=80, y=20 + 30 * i)
                tk.Label(new_win, text="{}".format(pro.charact[list(pro.charact.keys())[i]]), font=("??????", 14)).place(x=180, y=20 + 30 * i)
    detail_button = tk.Button(mainWindow, text='???????????????????????????',command=show_detail)
    detail_button.place(x=900, y=480, width=150, height=36, anchor=tk.E)

    #????????????
    def add_in_stock():
        name_cur = name_entry.get()
        ari_cur = dri_entry.get()
        add_cur = add_entry.get()
        type_cur = type_Box.get()
        if len(stockIni.goods) == 0:
            id_cur = 1
        else:
            id_cur = int(stockIni.goods[-1].id) + 1
        product_cur = Product(id_cur, name_cur, ari_cur, add_cur, user.tel,type_cur,chara_dic, user.username)
        stockIni.Add(product_cur)
        update_stock(tree, stockIni)
        write_csv('stock.csv', product_cur)

    add_button = tk.Button(mainWindow,text='????????????',command=add_in_stock)
    add_button.place(x=50, y=150)

    #???csv????????????????????????
    def delete_item_csv(item_index, filename):
        r = csv.reader(open(filename, encoding='gbk', newline=''))
        lines = list(r)
        for line in lines:
            if line[0] == str(item_index):
                lines.remove(line)
                break
        writer = csv.writer(open(filename, 'w', encoding='gbk', newline=''))
        writer.writerows(lines)
    #????????????
    def delete_stock():
        try:
            item_index = tree.item(tree.selection()[0], "values")[0]
        except IndexError:
            tk.messagebox.showerror('error', '??????????????????????????????')
        else:

            for pro in stockIni.goods:
                if pro.id == item_index:
                    break
            if pro.master != user.username:
                tk.messagebox.showerror('error', '???????????????????????????????????????')
            else:
                res = tk.messagebox.askyesnocancel('warning???','???????????????????????????')
                if res:
                    stockIni.goods.remove(pro)
                    update_stock(tree, stockIni)
                    delete_item_csv(item_index, 'stock.csv')

    delete_button = tk.Button(mainWindow,text='????????????',command=delete_stock)
    delete_button.place(x=50, y=180)

    #????????????
    def search_in_tree():
        ty_C = type_Box.get()
        if not ty_C:
            tk.messagebox.showerror('???????????????', '???????????????????????????????????????')
        else:
            charac = search_Box.get()
            if not charac:
                for child in tree.get_children():
                    tree.delete(child)
                infor_cur = search_entry.get()
                for cur_pro in stockIni.goods:
                    if (infor_cur == cur_pro.id or (infor_cur in cur_pro.name) or (infor_cur in cur_pro.intro) or (infor_cur in cur_pro.master) or (infor_cur in cur_pro.address)) and cur_pro.type == ty_C:
                        tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber,
                            cur_pro.email))
            else:
                if charac == '??????ID':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur == cur_pro.id and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber))

                elif charac == '????????????':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur in cur_pro.name and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber))

                elif charac == '????????????':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur in cur_pro.intro and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(
                                cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address, cur_pro.type, cur_pro.master,cur_pro.phonenumber))

                elif charac == '????????????':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur in cur_pro.address and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber))

                elif charac == '???????????????':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur in cur_pro.master and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber))

                elif charac == '???????????????':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur == cur_pro.phonenumber and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber))

                elif charac == '???????????????':
                    for child in tree.get_children():
                        tree.delete(child)
                    infor_cur = search_entry.get()
                    for cur_pro in stockIni.goods:
                        if infor_cur in cur_pro.email and cur_pro.type == ty_C:
                            tree.insert('', tk.END, values=(cur_pro.id, cur_pro.name, cur_pro.intro, cur_pro.address,cur_pro.type, cur_pro.master, cur_pro.phonenumber))

    tk.Label(mainWindow,text="???????????????", font=("??????",14)).place(x=50, y=240)
    search_entry = tk.Entry(mainWindow,width=15, textvariable=v4)
    search_entry.place(x=140, y=240)
    search_button = tk.Button(mainWindow,text='??????',command=search_in_tree)
    search_button.place(x=50, y=300)
    tk.Label(mainWindow, text="????????????????????????", font=("??????", 14)).place(x=50, y=270)
    search_Box = ttk.Combobox(mainWindow, height=6, width=10, state='readonly', font=("??????", 14),
                             values=['??????ID','????????????','????????????','????????????','???????????????','???????????????'])  # ???????????????
    search_Box.place(x=200, y=270)

    #??????????????????
    def show_all():
        update_stock(tree, stockIni)
    search_button = tk.Button(mainWindow,text='????????????????????????',command=show_all)
    search_button.place(x=50, y=400)

    def exit_window():
        res = tk.messagebox.askyesnocancel('??????','?????????????????????')
        if res:
            mainWindow.destroy()
    exit_button = tk.Button(mainWindow, text='????????????',command=exit_window).place(x=900, y=600, width=100, height=36, anchor=tk.SE)

    mainWindow.mainloop()