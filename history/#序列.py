#序列
#元组是序列类型的一种扩展一元组是一种序列类型，一旦创建就不能被修改。一使用小括号 0 或 tuple0 创建，元素间用逗号，分隔一。可以使用或不使用小括号
ls=[1,2,3,4]
ls+=[1,2,3,4,5]

del ls[1]
ls.remove(1)
print(list(ls))
