#jieba
import jieba as j
print(j.lcut("中国人是"))
print(j._lcut_all("中国人是"))
print(j._lcut_for_search("小米加步枪"))
j.add_word("小米加步枪")
print(j._lcut_for_search("小米加步枪"))
