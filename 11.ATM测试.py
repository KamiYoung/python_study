money = 1000000
name = None

name = input("请输入您的姓名")


def query(is_show):
    if is_show:
        print("-----------查询余额-----------")
    print(f"{name}，您好，您的余额剩余为：{money}元")


def save(num):
    global money
    money += float(num)
    print("-----------存款-----------")
    print(f"{name}，您好，存款{num}元成功")
    query(False)


def get_money(num):
    global money
    money -= float(num)
    print("-----------取款-----------")
    print(f"{name}，您好，取款{num}元成功")
    query(False)


def main():
    print("-----------主菜单-----------")
    print(f"{name}，您好，欢迎来到中国银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")


def check(num):
    if num != '1' and num != '2' and num != '3' and num != '4':
        return False
    return True


while True:
    main()
    menu = input("请输入您的选择：")
    if check(menu):
        print(f"您选择了{menu}操作")
    else:
        print("您的输入不合法，程序退出！")
        break
    if menu == '1':
        query(True)
        continue
    if menu == '2':
        save(input("请输入您要存款的金额："))
        continue
    if menu == '3':
        get_money(input("请输入您要取款的金额："))
        continue
    if menu == '4':
        break
