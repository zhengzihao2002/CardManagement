import os,json

# 记录所有名片的字典
card_list = list()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def any_key():
    input("按任意键继续...")

def read_file():
    global card_list  # Declare card_list as a global variable
    try:
        file = open("data.json","r",encoding="UTF-8")
        loaded_data = json.load(file)
        card_list = loaded_data
    except Exception as e:
        file = open("data.json","w",encoding="UTF-8")
    finally:
        file.close()
def showMenu():
    print("*" * 50)
    print("欢迎使用【名片管理系统v1.0】\n")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片\n")
    print("0. 退出系统")

    print("*" * 50)


def new_card():
    """新增名片"""
    print("*" * 50)
    print("新增名片")

    name_str = input("请输入姓名：")
    phone_str = input("请输入手机号：")
    email_str = input("请输入邮箱：")
    qq_str = input("请输入QQ号码：")

    card_dict = {"name": name_str, "phone": phone_str, "email": email_str, "qq": qq_str}
    card_list.append(card_dict)

    # Write the list of dictionaries to a file
    with open("data.json", "w") as file:
        json.dump(card_list, file)


def show_all():
    """显示所有名片"""
    print("*" * 50)
    print("显示所有名片")
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        any_key()
        return

    for name in ["姓名", "电话", "邮箱", "QQ"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)

    for card_dict in card_list:
        print(f"{card_dict['name']}\t{card_dict['phone']}\t{card_dict['email']}\t{card_dict['qq']}\t")
    any_key()


def search_card():
    """搜索名片"""
    print("*" * 50)
    print("搜索名片")

    target_name = input("请输入要搜索的姓名:")

    for dict in card_list:
        if dict['name'] == target_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print(f"{dict['name']}\t{dict['phone']}\t\t{dict['email']}\t\t{dict['qq']}\t\t")

            edit_card(dict)
            break
    else:
        # 循环如果没有被break那么会完整的跑完并且执行以下这一行代码
        print("抱歉，没有找到此人")
        any_key()

def edit_card(card_dict):
    global card_list
    action = input("请输入对名片对操作: \n[1] 修改\n[2] 删除\n[其他]: 取消操作")
    if action == "1":
        card_dict['name'] = get_info(card_dict["name"],"请输入姓名 (不更改敲回车键)：")
        card_dict['phone'] = get_info(card_dict["phone"],"请输入手机号 (不更改敲回车键)：")
        card_dict['email'] = get_info(card_dict["email"], "请输入邮箱 (不更改敲回车键)：")
        card_dict['qq'] = get_info(card_dict["qq"], "请输入QQ号码 (不更改敲回车键)：")
        
        any_key()

    elif action == "2":
        delete = input("您确定要删除吗？此操作不可撤销！输入 ‘04-19-1996’ 以确认删除 ")
        if delete == "04-19-1996":
            card_list.remove(card_dict)
            print("已删除")
        else:
            print("已撤销")
        any_key()
    else:
        print("操作已经取消！")
        any_key()
    # Write the list of dictionaries to a file
    with open("data.json", "w") as file:
        json.dump(card_list, file)

def get_info(orig_value,message):
    """
    输入名片信息
    :param orig_value:原有值
    :param message:提示信息
    :return:如果用户输入内容就返回新内容，否则返回原有值
    """
    result = input(message)

    if result == "" or len(result)==0:
        return orig_value
    else:
        return result