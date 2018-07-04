import os,sys,json
from . import credit
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'./database/creditcart'
DIR2=BASE_DIR+r'./database/session.text'
with open(DIR, 'r') as f, open(DIR2, 'r') as h:
    dict_card = json.loads(f.read())
    name = h.read()
def my_creditcard():
        print('账号：%s\n'%name)
        print('卡号：%s\n'%dict_card['%s'%name]['number'])
        print('余额：%s\n'%dict_card['%s'%name]['balance'])
def withdraw():#提现
    rule='''
    提现规则：
    提现将收取5%手续费
    '''
    print(rule)
    with open(DIR, 'r') as f, open(DIR2, 'r') as h:
        dict_card = json.loads(f.read())
        name = h.read()
        balance = dict_card['%s' % name]['balance']
    while True:
        money=input('请输入提现金额,[b]返回上一层：')
        if money.isdigit():
            money=int(money)
            if balance-money-money*0.05>=0:
                balance2=balance-money-money*0.05
                print('提现成功，%s,提现金额：余额为%s，手续费：%s'%(money,balance2,money*0.05))
                with open(DIR, 'w') as f:
                    dict_card['%s' % name]['balance'] = balance2
                    f.write(json.dumps(dict_card))
                continue
        elif money=='b':
                credit.a()
                break
        else:
                print('请输入正确的选择：')

def insert(money):#充值
    with open(DIR, 'r') as f, open(DIR2, 'r') as h:
        dict_card = json.loads(f.read())
        name = h.read()
    with open(DIR,'w')as f:
        dict_card['%s'%name]['balance']+=money
        f.write(json.dumps(dict_card))
        print('充值成功，余额为：%s'%dict_card['%s'%name]['balance'])


