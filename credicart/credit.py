import os,sys,time
from . import mycreditcard
from Main import main
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\database\creditcart.text'
DIR2=BASE_DIR+r'\database\session.text'
def a():
    a='''
    1.      我的信用卡
    2.      提现
    3.      充值
    '''
    while True :
        print(a)
        choose=input('请输入您的选择,[b]返回商城：')
        if choose=='1':
            mycreditcard.my_creditcard()
        if choose=='2':
            mycreditcard.withdraw()
        if choose=='3':
            while True:
               choice=input('请输入您要充值的金额,[b]取消充值：')
               if choice.isdigit():
                    choice=int(choice)
                    mycreditcard.insert(choice)
                    continue
               elif choice=='b':
                   break
               else:
                   print('请输入正确的数字！')
        elif choose=='b':
            main.list()
        else:
            print('请输入正确的选择！')


