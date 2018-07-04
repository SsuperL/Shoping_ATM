'''
信用卡额度为15000
实现还款
可以体现，手续费为5%
买东西加入购物车，调用信用卡结账
'''
"""
分登录和注册
"""
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\Main\list.text'
from credicart import credit
from Bin import center
from Bin import Manager
from Renzheng import Log
from Main import run

def list():
    print('-------欢迎进入信用卡购物商城-------')
    f = open(DIR, 'r', encoding='utf-8')
    a = f.readlines()
    f.close()
    for i in a:
        line = i.strip()
        print(line)
    while True:
        choice = input('请输入您的选择：')
        if choice == '1':  # 进入购物中心
            center.center_list()
        if choice == '2':
            credit.a()
        if choice=='3':
            confirm=input('确认退出？[y]')
            if confirm=='y':
                run.run_run()
        else:
            print('请输入正确的选择！')





