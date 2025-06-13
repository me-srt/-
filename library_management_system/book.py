import os
import json
import class_object


def os_name():
    os.remove('book_shelf.txt')
    os.rename('book_shelf_copy.txt', 'book_shelf.txt')


def book_entry():
    """图书录入"""

    book_name = input("写入图书名-> ")
    book_author = input("写入图书作者-> ")
    book_price = input("写入图书价格-> ")
    book_type = input("写入图书类型-> ")

    gxt = class_object.Gxt(book_name, book_author, book_price, book_type)
    gxt_dict = gxt.to_dict()  # 创建容器，将数据放入
    gxt_json = json.dumps(gxt_dict, ensure_ascii=False)  # 将数据转换成json格式, 追加不转换文字为ASCII码
    print(gxt_json)

    with open("book_shelf.txt", "a", encoding="UTF-8") as f:
        f.write(gxt_json)
        f.write("\n")
    y_n_input = input("是否继续添加图书(y/任意) ->")
    if y_n_input == 'y':
        book_entry()


def book_delete():
    enter_data_delete = input("请输入要删除的图书名 -> ")
    """图书删除"""

    book_list = []
    with open("book_shelf.txt", "r", encoding="utf-8") as f:
        for i in f:
            book_data = json.loads(i)
            book_list.append(book_data)

    for i in book_list:
        if f"{i['书名']}" == enter_data_delete:
            continue
        else:
            gxt_json = json.dumps(i, ensure_ascii=False)  # 将数据转换成json格式, 追加不转换文字为ASCII码
            with open('book_shelf_copy.txt', 'a', encoding='utf-8') as f:
                f.write(gxt_json)
                f.write("\n")

    os_name()
    print("图书删除成功！")


def book_modify():
    """图书修改"""

    book_list = []
    with open("book_shelf.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():  # 确保不是空行
                book_data = json.loads(line)
                book_list.append(book_data)

    enter_modify = input("请输入要修改的图书名 -> ")
    found = False

    for book in book_list:
        if book['书名'] == enter_modify:
            found = True
            print("1.\t书名\n2.\t作者\n3.\t价格\n4.\t图书类型")
            ke = input("请输入操作编号 -> ")
            vl = input("输入修改后内容 -> ")
            if ke == '1':
                book['书名'] = vl
            elif ke == "2":
                book['作者'] = vl
            elif ke == "3":
                book['价格'] = vl
            elif ke == "4":
                book['图书类型'] = vl
            else:
                print("无效的操作编号")
                return
            break

    if not found:
        print("未找到该图书")
        return

    with open('book_shelf_copy.txt', 'w', encoding='utf-8') as f:
        for book in book_list:
            json_str = json.dumps(book, ensure_ascii=False)
            f.write(json_str + "\n")

    os_name()
    print("图书信息修改成功！")


def book_query():
    """图书查询"""

    book_list = []
    with open("book_shelf.txt", "r", encoding="utf-8") as f:
        for i in f:
            book_data = json.loads(i)
            book_list.append(book_data)

    print("\t书名\t\t\t\t作者\t\t\t价格\t\t图书类型")
    for i in book_list:
        print(f"{i['书名']:<15}\t{i['作者']:<8}\t{i['价格']:<6}\t{i['图书类型']:<5}")


def book_main():
    n = 3
    while n != 0:
        print("1.\t图书录入\n2.\t图书删除\n3.\t图书修改\n4.\t图书查询\n5.\t退出")
        user_input = input("请输入操作编号 ->")
        if user_input == '1':
            book_entry()  # 录入图书
        elif user_input == '2':
            book_delete()  # 删除
        elif user_input == '3':
            book_modify()  # 修改
        elif user_input == '4':
            book_query()  # 查询全部图书
        elif user_input == '5':
            print("已安全退出")
            exit(1)
        else:
            print("请检查是否输入正确")
            book_main()