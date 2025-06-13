import re
import json
import random
import string
import book
import class_object


def captcha(length=6, include_letters=True, include_digits=True, case_sensitive=True):

    chars = ''
    if include_digits:
        chars += string.digits
    if include_letters:
        if case_sensitive:
            chars += string.ascii_letters
        else:
            chars += string.ascii_uppercase

    return ''.join(random.choice(chars) for _ in range(length))


def user_zhu_ce():
    """注册账号"""

    password = input("password-> ")

    if password == '' or password == ' ':
        print("密码不能为空")
        user_zhu_ce()
    elif len(password) < 8:  # 判断密码长度
        print("密码长度不能低于8个字符")
        user_zhu_ce()
    elif not re.search(r'[a-zA-Z]', password):
        print("密码至少包含一个大写字母和一个小写字母")
        user_zhu_ce()
    else:
        username = captcha(length=9, include_letters=False)  # 生成九位数随机账号

        register = class_object.Register(username, password)  # 载入函数
        register_dict = register.user_to_dict()
        register_json = json.dumps(register_dict, ensure_ascii=False)
        with open("user_data.txt", "a", encoding="utf-8") as f:
            f.write(register_json)
            f.write("\n")
        print(f"注册成功！\n您的账号：{username}\n您的密码：{password}")
        book.book_main()


def user_deng():
    """用户登录"""

    username = input("username ->")
    password = input("password ->")

    with open("user_data.txt", "r", encoding="utf-8") as f:
        user_list = []
        for i in f:
            user_data = json.loads(i)
            user_list.append(user_data)

    for i in user_list:
        if username == i["账号"] and password == i["密码"]:  # 验证账号密码
            print("登录成功!")  # 没问题
            book.book_main()
        else:
            print("请检查账号密码是否输入正确")
            user_deng()


def main():
    print("1.\t登录\n2.\t注册\n3.\t退出")
    user_input = input("请输入操作代码 ->")
    if user_input == '1':
        print("请输入您的账号密码登录")
        user_deng()
    elif user_input == '2':
        print("请设置您的密码进行注册")
        user_zhu_ce()
    elif user_input == '3':
        print("退出成功！")
        exit("不知道写啥，新年快乐")
    else:
        print("请检查是否输入有误")
        main()
