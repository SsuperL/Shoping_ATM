#购物车结算
import os,sys,time,json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\database\card.text'#购物车
DIR2=BASE_DIR+r'\database\creditcart'#信用卡
DIR3=BASE_DIR+r'\database\session.text'

def pay_bill(sum):
    with open(DIR3,'r',encoding='utf-8') as f:
        name=f.read()
    with open(DIR2,'r',encoding='utf-8') as f:
        a=json.loads(f.read())
        balance=a['%s'%name]['balance']
    if a['%s'%name]['number']=='':
        number=input('账号%s'%name+'还没绑定信用卡，请输入卡号绑定信用卡：\n')
        number2=input('请输入支付密码：')
        a['%s'%name]['number']=number
        a['%s'%name]['cardpwd']=number2
        with open(DIR2,'w',encoding='utf-8') as f:
           f.write(json.dumps(a))
    else:
        while True:
            pwd=input('请输入支付密码:')
            cardpwd=a['%s'%name]['cardpwd']
            if pwd==cardpwd:
                if balance<=0:
                    print('opps！余额不足，请先充值！')
                else:
                    balance-=sum
                    print('购物车总价为：%s'%sum,'结算后余额为：%s'%balance)
                    with open(DIR2,'r',encoding='utf-8') as f:
                        a=json.loads(f.read())
                    with open(DIR2,'w',encoding='utf-8') as f:
                       a['%s' % name]['balance'] = balance
                       f.write(json.dumps(a))
                    with open(DIR, 'w') as f:
                        f.truncate()  # 清空购物车
                    break
            else:
                print('密码错误！')
                continue








