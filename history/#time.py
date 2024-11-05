#time
import time as t
print(t.time())        #获取时间戳
print(t.ctime())            #获取易读的时间
print(t.gmtime())           #生成计算机读取的时间
#格式化
#        strftime(tpl       ,       ts        )
#                 模板字符串, 内部时间类型
print(t.strftime("%Y-%m-%d %H:%M:%S",t.gmtime()))
#格式化字符串      ^^^^^^^^^^^^^^^^^            用strftime
#%Y 年份（0000~9999）%m月（01~12） %B/b月份名/缩写   %d日期(01~31) %A/a星期英文/缩写 %H/h24/12小时(00~23)/(00~12) %p上下午(A/PM)  %S秒

#解析字符串中的时间:strptime(str,tpl)  变成浮点数
#                        字符串,模板
print(t.strptime(t.strftime("%Y-%m-%d %H:%M:%S",t.gmtime()),"%Y-%m-%d %H:%M:%S"))
#测量时间:perf_counter()
s=t.perf_counter()
t.sleep(9)                  #THE WORLD!
e=t.perf_counter()
print(e-s)
