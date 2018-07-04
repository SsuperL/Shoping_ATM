#购物中心主界面
from . import shopping
from . import shop_card
from . import pay
from Main import main
import os,sys,time,json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\database\card.text'#购物车
DIR2=BASE_DIR+r'\database\creditcart'#信用卡
DIR3=BASE_DIR+r'\database\session.text'
DIR4=BASE_DIR+r'\database\Item.text'#流水账
DIR5=BASE_DIR+r'\Renzheng\user.text'
def center_list():
    print('-------欢迎进入购物中心-------')
    while True:
        a = '''
               1       购物商城
               2       购物车
               3       购物结算
               4       个人中心
               '''
        print(a)
        choose = input('请输入您的选择,[b]返回商城主页：')
        if choose=='1':
          shopping.shop()#购物中心
        if choose=='2':
            shop_card.card()
        if choose=='3':
            choose2=input('确认结算？[y]结算[b]退出')
            if choose2=='y':
                card = []
                s=0
                with open(DIR, 'r', encoding='utf-8') as f:
                    a = f.readlines()
                if a==[]:
                    print("购物车是空的噢，请先去购物吧~~")
                else:
                    for i, item in enumerate(a):
                        line = item.strip().split()
                        card.append(int(line[1]))  # 将str的价格转换为int类型
                        s += card[i]  # 购物车总价
                    pay.pay_bill(s)
                continue
            else:
                continue
        if choose=='4':
            x='''
            1       修改密码
            2       查看购物流水记录
            '''
            while True:
                print(x)
                choose3=input('请输入您的选择,[b]返回上一层：')
                if choose3=='1':
                    change_pwd()
                if choose3=='2':
                    with open(DIR4,'r',encoding='utf-8')as f:
                        for i in f.readlines():
                            line=i.strip()
                            print(line)
                if choose3=='b':
                    break
                else:
                    print('请输入正确的选择！')

        if choose=='b':
            main.list()
        else:
         print('请输入正确的编号!')
         continue

def change_pwd():
    with open(DIR2,'r')as f,open(DIR3,'r')as h,open(DIR5,'r')as p:
        name=h.read()
        user_dict=json.loads(f.read())
        user=json.loads(p.read())
        print('原密码：%s'%user_dict['%s'%name]['password'])
        pwd=input('新密码：')
        confirm=input('确认要修改密码？[y][n]')
        if confirm=='y':
            user_dict['%s' % name]['password']=pwd
            user['%s'%name]=pwd
            with open(DIR2,'w')as f,open(DIR5,'w')as p:
                f.write(json.dumps(user_dict))
                p.write(json.dumps(user))
                print('修改成功！')


