#da 
TemperStr = input("intput temperture with  unit:")
#          键入信息    (提示信息)
if TemperStr[-1] in ['F','f']:                 #[序号] 或 [] 
   '''   正向:  0  1  2  3  4  5 
 #     字符串:  1  2  3  4  5  6
         反向: -6 -5 -4 -3 -2 -1
        字符串操作:索引[序号(正向或反向)]:获取单个字符                                                                                                                                 
                  切片[M:N]:获取一段字符 '''  
   C= (eval(TemperStr[0:-1]) - 32)/1.8
   #                        整数^   ^浮点数
   print("the tempertue tranformed is {:.2f}C".format(C))
elif TemperStr[-1] in  ['C',"c"]:
   # ^条件

   # in判断是否在列表内^    元素   ^列表类型
   # 变量 in [a,x,c,v,......]  输出 Ture/Flase
   F= eval(TemperStr[0:-1])*1.8+32
   #^赋值语句
   #eval()  评估函数 去掉最外侧的引号变语句
   #        eval("1+2")=3    eval("'a'")='a'   eval(print(a))=a
   print("the tempertue tranformed is {:.2f}F".format(F))
   #                       print的格式化:用大括号:槽{}用于输出后面.变量的值
   #                                    {   .   2f}表示输出小数点后两位
else :
   print("format incorrect")
#if/elif/else  : 分支语句
#input/print/eval()函数
   