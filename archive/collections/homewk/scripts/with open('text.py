with open('text.txt', 'r', encoding='utf-8') as file:
    # 读取文件的所有行，存储在 lines 列表中
    lines = file.readlines()
    # 检查文件是否为空，如果为空则输出提示信息并结束程序
    if not lines:
        print("文件为空。")
    else:
        # 使用 max 函数找出最长的行，key=len 表示以行的长度作为比较依据
        longest_line = max(lines, key=len)
        # 去除最长行末尾的换行符
        longest_line = longest_line.strip()
        # 计算最长行的长度
        length = len(longest_line)
        # 输出最长行的长度和内容
        print(f'最长行的长度为: {length}')
        print(f'最长行的内容为: {longest_line}')
