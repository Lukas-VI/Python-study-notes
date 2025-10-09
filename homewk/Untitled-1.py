with open("./text.txt", "r", encoding="utf-8") as f:
    # 读取文件的所有行
    lines = f.readlines()
    # （1）计算总行数
    total_lines = len(lines)
    print(f"该文本文件共有 {total_lines} 行")

    # （2）统计以大写字母 P 开头的行数
    count_upper_p = sum(1 for line in lines if line.strip().startswith('P'))
    print(f"文件中以大写字母 P 开头的有 {count_upper_p} 行")

    # （3）找出一行中包含字符最多和最少的分别在第几行
    max_len = 0
    min_len = float('inf')
    max_len_line = 0
    min_len_line = 0
    for i, line in enumerate(lines):
        line_len = len(line.strip())
        if line_len > max_len:
            max_len = line_len
            max_len_line = i + 1
        if line_len < min_len:
            min_len = line_len
            min_len_line = i + 1

    print(f"包含字符最多的是第 {max_len_line} 行")
    print(f"包含字符最少的是第 {min_len_line} 行")
