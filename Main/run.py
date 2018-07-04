import os,sys
import main
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Renzheng import Log
from Bin import Manager
def run_run():
    while True:
        a='''
        1       普通用户
        2       管理员
        '''
        print(a)
        choose=input('登录的身份：')
        if choose=='1':
            Log.log()  # 用户登录和验证
            main.list()
        if choose=='2':
            Manager.manage()
