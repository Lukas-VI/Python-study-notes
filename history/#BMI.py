#BMI
h,w=eval(input("input hight(m) and wight(kg)(divide them with','):"))
BMI=w/pow(h,2)
w,c="",""
if BMI<18.5:                                        #读代码先读分支结构
    w,c="thin","thin"
elif 18.5<=BMI<24:                                  #不
    w,c="nomal","nomal"
elif 24<=BMI<25:                                    #重
    w,c="nomal","little fat"
elif 25<=BMI<28:                                    #不
    w,c="lf","lf"
elif 28<=BMI<30:                                    #漏
    w,c="fat","fat"
print("BMI:{:.2f},international:{},national:{}".format(BMI,w,c))