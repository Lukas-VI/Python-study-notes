"""
输入两个字符串，求两个字符串共有的最长子串。所谓的子串是原字符串中的一段连续的字符。
​请上传源程序截图与验证截图。
​验证结果，例如：
​字符串1：qwertyui
​字符串2：ertyuioipo
​最长共有的子串：ertyui
"""

def co(str1: str, str2: str) -> str:
    costr = ''
    str1 = str2 if str1 < str2 else str1
    for char1 in str1:
        for char2 in str2:
            if char1 == char2:
                costr += char1
                break
    return costr

if __name__ == "__main__":
    print(co("qwertyui", "ertyuioipo"))
