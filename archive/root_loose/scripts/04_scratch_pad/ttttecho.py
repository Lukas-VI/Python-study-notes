import time

def stream_print(text, interval=0.2):
    for char in text:
        print(char, end='', flush=True)  # end='' 避免换行，flush=True 强制立即输出
        time.sleep(interval)

# 示例
stream_print("老天保佑金山银山全都有\n")
time.sleep(1)
stream_print("老天教唆莫管江湖龙虎斗\n")