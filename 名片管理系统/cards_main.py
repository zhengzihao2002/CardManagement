import cards_tools

cards_tools.read_file()
while True:
    # TODO(作者) 显示功能菜单
    cards_tools.showMenu()
    action_str = input("请选择希望执行的操作:")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()
    elif action_str == "0":
        cards_tools.clear_terminal()
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("您输入的不正确，请重新选择")
