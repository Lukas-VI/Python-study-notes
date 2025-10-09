
import csv

# 存储星座信息的字典
constellation_info = {}

# 读取CSV文件
with open('123.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        constellation = row[0]
        date_range = f"{row[1]}-{row[2]}"
        char_form = row[3]
        constellation_info[constellation] = (date_range, char_form)

while True:
    user_input = input("请输入星座名称（输入Q退出）：")
    if user_input.upper() == "Q":
        break
    elif user_input in constellation_info:
        date_range, char_form = constellation_info[user_input]
        print(f"{user_input}的出生日期范围是{date_range}，对应字符形式是{char_form}")
    else:
        print("输入星座名称有误!")
