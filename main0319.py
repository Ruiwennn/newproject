#0319販賣機練習
flag = True
balance = 0

drinks = [
    {'name':'可樂', 'price':20},
    {'name':'雪碧', 'price':20},
    {'name':'茶裏王', 'price':25},
    {'name':'原萃', 'price':25},
    {'name':'純粹喝', 'price':30},
    {'name':'水', 'price':20}

x=0
def deposit():
    global balance
    #global用來取用balance
    value= eval(input('儲值金額:'))
    while value <1:
        print('=====儲值金額需大於零=====')
        value = eval(input('儲值金額:'))
#ctrl按著+滑鼠只到buy會變連結
def buy():
    global.balance, drinks
    print('\n請選擇商品')
    for i in range(0, len(drinks)):
        print(f'({i + 1}')\t
        {drinks[i]['name']}\t
        {drinks[i]}['price']}元
        ')
        choose = eval(input('請選擇:'))

    while choose < 1 or choose > 6:
        print('請輸入1~6之間')
    choose = eval(input('請選擇:'))

    buy_drink = drinks[chose - 1]
    if balance < buy_drink['price']:
        print('===餘額不足===')
    else:
        print(f'已購買{buy_drink['
        name
        ']} {buy_drink['
        price
        ']}元')
        balance -= buy_drink['price']
        print(f'購買餘額為{balance}元')

balance += value
print(f'儲值後餘額為 {balance}元')
while flag:
    print('\n========')
    select = eval(input('1, 儲值\n2, 購買\n3, 查詢餘額\n4, 請選擇:'))
    if select == 1: #儲值
        value = eval(input('儲值金額：'))
        while value < 1:
            print('==儲值金額需大於零===')
            value = eval(input('儲值金額'))
        balance += value
        print(f'儲值後餘額為 {balance}元')
    elif select == 2:
        buy()
    elif select == 3:
        print(f'目前金額為 {balance}元')
    elif select == 4:
        print('bye')
        flag = 0
        break
    else:
        print('===請輸入1~45之間===')
        continue


