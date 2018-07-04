#购物商城，实现购物，加入购物车
import os,sys,time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DIR=BASE_DIR+r'\Bin\products.txt'
DIR2=BASE_DIR+r'\database\card.text'
DIR3=BASE_DIR+r'\database\Item.text'
from . import center
def shop():
    print('=======欢迎进入购物商城=======')
    print('------------------------------')
    print('           在售商品           ')
    print('------------------------------')
    print('编号\t 商品 \t\t价格 \t\t')
    with open(DIR, 'r', encoding='utf-8') as f:
        products = f.readlines()  # 数据以列表形式存储
        for i, item in enumerate(products):
            line = item.strip()
            print(' ', i+1, '\t\t', line)
    f = open(DIR, 'r', encoding='utf-8')
    result = []
    result1 = []
    for line in products:
        line = line.strip()
        result1.append(line.strip('\n').split())
    f.close()

    product = []  # 商品名
    price = []  # 商品价格
    for i, item in enumerate(result1):
        product.append(result1[i][0])
        price.append(result1[i][1])

    total_price = []
    buyed_product = []

    while True:
        choice1 = input('请选择你想要加入购物车的商品编号：')
        if choice1.isdigit():
            choice1=int(choice1)
            if choice1>len(product)or choice1>len(price):
                print("不存在此商品，请重新选择！")
            else:
                total_price.append(price[choice1-1])#商品总价
                buyed_product.append(product[choice1-1])#购买的商品
                print("%s成功"%product[choice1-1],"加入购物车","价格%s"%price[choice1-1])
                f=open(DIR2,'a',encoding='utf-8')
                f.write(product[choice1-1]+'\t\t'+price[choice1-1]+'\n')
                f.close()
                f = open(DIR3, 'a', encoding='utf-8')
                f.write(product[choice1-1] + '\t\t' + price[choice1-1] + time.ctime()+'\n')
                f.close()
                while True:
                    choice2=input("是否继续购物？[y]继续购物 [b]返回上一级")
                    if choice2=='y':
                        break
                    elif choice2=='b':
                       center.center_list()
                    else:
                        print("请输入正确的选项！")
        else:
            print("请输入正确的编号！")

