#管理员
import json,os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\Renzheng\user.text'
DIR2=BASE_DIR+r'\database\creditcart'
from Main import run
def manage():
    while True:
        mname = input('name[b]返回主页:')
        pwd = input('password:')
        if mname=='b':
            run.run_run()
        elif mname=='admin'and pwd=='admin':
            a='''
            1       添加账户
            2       修改额度
            '''
            while True:
                x={
                    '1':add_user,
                    '2':amend_balance
                }#可用字典实现选择判断调用函数
                print(a)
                choose=input('请输入选择[b]返回上一级：')
                if choose in x:
                    x[choose]()
                elif choose=='b':
                    break

        else:
            print('密码错误！')


def add_user():
    name=input('用户名：')
    passwd=input('密码：')
    with open(DIR,'r')as f:
        user=json.loads(f.read())
    with open(DIR,'w')as f:
        user.update({'%s' % name: '%s' % passwd})
        f.write(json.dumps(user))
        print('添加成功！')

def amend_balance():
    balance=int(input('要修改的额度：'))
    with open(DIR2,'r')as f:
        card=json.loads(f.read())
        for i in card.keys():
            card[i]['balance']=balance
    with open(DIR2,'w')as f:
        f.write(json.dumps(card))
        print('修改成功！')