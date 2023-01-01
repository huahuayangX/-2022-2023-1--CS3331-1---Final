
from openwindow import openWindow
from openwindow import User, UserStock, read_user_w
from adminwindow import adminwindow
from userwindow import userwindow

import csv


if __name__ == '__main__':
    flag, account = openWindow()


    UserS = UserStock(read_user_w())
    for users in UserS.accounts:
        if users.username == account:
            break


    if flag == 0:
        adminwindow()
    elif flag == 1:
        userwindow(users)