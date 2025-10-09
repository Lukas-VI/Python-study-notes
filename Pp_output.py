#写一个程序实现在鼠标光标处输出字符，并将光标移动到下一行。
from pynput import keyboard

import time as t
for i in range(10):
    string_to_type = "Hello! How are you?"
    c = keyboard.Controller()
    for char in string_to_type:
        c.tap(char)
    c.press(keyboard.Key.enter)
    t.sleep(5)