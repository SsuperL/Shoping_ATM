#用户登录认证
import json,os,sys,json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\Renzheng\user.text'
DIR2=BASE_DIR+r'\database\session.text'
DIR3=BASE_DIR+r'\database\creditcart'
def renzheng(func):
    def deco(*args,**kwargs):
       # f = open(DIR, 'r')
       # result = {}
       # for line in f.readlines():
       #     line = line.strip()
       #     if not len(line):
       #         continue
       #     result[line.split(':')[0]] = line.split(':')[1]#将数据读取成字典形式
       # f.close()
       with open(DIR,'r')as f:
           username=json.loads(f.read())
       while True:
            name=input('请输入用户名：')
            password=input('请输入密码：')
            if  name in username.keys() :
                if password==username['%s'%name] :
                    with open(DIR2,'w',encoding='utf-8') as f:
                        f.write(name)
                    card={'%s'%name:{'name':'%s'%name,'password':'%s'%password,'number':'','balance':15000,'cardpwd':''}}#二维字典的写入
                    with open(DIR3, 'r', encoding='utf-8') as f:
                        a=f.read()
                        card2=json.loads(a)
                    with open(DIR3, 'w', encoding='utf-8') as f:
                        if name not in card2:
                            card2.update({'%s'%name:{'name':'%s'%name,'password':'%s'%password,'number':'','balance':15000,'cardpwd':''}})
                            f.write(json.dumps(card2))
                        else:
                            f.write(json.dumps(card2))
                    func()
                    break
                    break
                else:
                        print('用户名密码不匹配,请重新输入')
            else:
               print('用户不存在，请先注册!')
               regist()
               break
    return deco

def reg_renzheng(func):
    def deco():
        print('-----注册-----')
        f = open(DIR, 'r')
        result = {}
        with open(DIR, 'r')as f:
            username = json.loads(f.read())
        while True:
            name1 = input('请输入用户名：')
            password = input('请输入密码：')
            password1=input('确认密码:')
            if name1=='':
                print('用户名不能为空！')
            if name1 in username.keys():
                print('用户已存在，请重新输入！')
            elif password1!=password:
                print('两次密码不一致,请重新输入！')
            else:
                username.update({'%s'%name1:'%s'%password})
                with open(DIR,'w')as f:
                    f.write(json.dumps(username))
                func()
                log()
                break
    return deco
@renzheng
def log():
    print('登录成功!')

@reg_renzheng
def regist():
    print('注册成功!')
    print('------登录------')

# f=open('user.text','r')
# result={}
# for line in f.readlines():
#     line=line.strip()
#     if not len(line):
#         continue
#     result[line.split(':')[0]]=line.split(':')[1]
# f.close()
# print(result)
