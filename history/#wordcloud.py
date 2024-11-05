#wordcloud
import imageio.v2 as i
import jieba as j
#mask=i.imread("CSR.jpg")'''mask=mask'''
import wordcloud as w
import os as o
tstate=0
ps=0
fo=0
def wcreat():      #创建对象
        global c
        c=w.WordCloud(width=1000,height=800,min_font_size=10,max_font_size=200,font_step=20,font_path="msyh.ttc",max_words=2000,\
              stopwords={'的', '得', '地', '不但', '不仅', '着', '似的', '一样', '一般', '的', '了', '吧', '呢', '啊', '着', '嘛', '呗', '罢了', '而已', '也罢', \
                     '也好', '啦', '嘞', '喽', '着呢', '了', '过', '虽然', '但是', '然而', '如果', '与其', '因为', '所以', '从', '自从', '自', '打', '到', '往', \
                    '在', '由', '向', '于', '至', '趁', '当', '给', '连', '们', '所', '当着', '沿着', '顺着', '按', '吗', '么', '呢', '啊', '吧', '按照', '遵照', \
                    '依照', '靠', '本着', '用', '吧', '了', '啊', '通过', '根据', '据', '拿', '比', '因', '因为', '由于', '为', '为了', '为着', '被', '给', '让', '叫', \
                    '归', '由', '把', '将', '而', '而且', '并', '并且', '或者', '管', '对', '对于', '关于', '跟', '和', '给', '替', '向', '同','也','是', '除了', '同',\
                    '和', '跟','与', '及', '或', '以及','我','自己','上','他们','一个','不',"有","他","她","它"},\
           background_color="white")
def pgen():           #处理文字,生成图片
    global fname
    global phname
    fo=open("{}.txt".format(fname),"r",encoding="utf-8")
    t=fo.read()
    fo.close()
    pt=j.lcut(t)
    txt=" ".join(pt)
    c.generate(txt)
    c.to_file("{}.png".format(phname))
'''def natest():                                                   #检测生成图是否重名    
    global phname
    while tstate==0:
        try:
            i.imread(phname +".png")      #若不存在重名图片,读不到文件就会发生错误,则说明文件没有重名,并进入except执行正常的程序.多么巧妙的方法!
        except:                  #正常则跳出循环检测1正常0异常
            break;return 1'''
def chfile(name):
    if o.path.isfile(name+'.png')==False:
        return 1
    else:
        return 0
fname=input('文件名.txt:')            
while tstate==0:    #输入文件名的
    try:              #检测文件是否存在的
        n=open("{}.txt".format(fname),"r",encoding="utf-8")
        break                       #能运行至此步则文件存在,跳出循环
    except FileNotFoundError:   #找不到文件
        print("not found file")
        fname=input('文件名.txt:')      #重输文件,循环检测是否输对^
wcreat()       #完成文件输入后创建对象
phname=input("save photo name:")                                 #检测图片是否覆盖
while chfile(phname)==0:                               #重名要么覆盖要么等到输对为止                             
    print('已有相同图名,确定覆盖回车,否则重新输入')
    phname=input()                      #重输图名
    chfile(phname)
    if phname=="":          #输入为''则覆盖
        break          
    elif chfile(phname)==0:    #如果杠精再输一次重名重新循环 
       pass
    else:            
       break
pgen()

    