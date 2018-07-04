#购物车，查看购物车，清空购物车
import os,sys,time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\database\card.text'
from . import center
def card():
    while True:
        a = '''
           1       查看购物车
           2       清空购物车
           '''
        print(a)
        choice=input('请输入您的选择 [b]返回上一级：')#返回购物中心
        if choice=='1':
            view_card()
            while True:
                choice2=input('[b]返回上一级:')#购物车选择页面
                if choice2=='b':
                    break
                else:
                    print('请输入正确的选择！')
        elif choice=='2':
            while True:
                confirm=input('确定清空购物车？(y/n)')
                if confirm=='y':
                   with open(DIR,'w') as f:
                       f.truncate()#清空购物车
                       print('成功清空购物车')
                       break
                else:
                    break
        else:
            if choice=='b':
               center.center_list()
            else:
                print('请输入正确的编号')


def view_card():#查看购物车
    with open(DIR,'r',encoding='utf-8') as f:
        a=f.readlines()
        if a==[]:
            print("购物车是空的噢")
        else:
            for i in a:
                line=i.strip()
                print(line)

