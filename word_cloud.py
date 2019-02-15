import re#正则库
import collections#词频统计
import numpy as np #numpy数据处理库
import jieba#结巴分词
import wordcloud#词云展示库
from PIL import Image#图像处理库
import matplotlib.pyplot as plt#import matplotlib.pyplot as plt#图像展示库

#1、读取文件
#打开
txt=open("谈判是什么.txt",'r',encoding='gb18030',errors='ignore')
#读取
str_txt=txt.read()
#关闭
txt.close()

#2、文本预处理
#正则compile得pattern
my_pattern=re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"|\!|"\s|\xa0|\u3000|：')
#正则sub去除
str_txt=re.sub(my_pattern,'',str_txt)
#3、文本分词
#结巴分词
list_jieba=jieba.cut(str_txt)
#for去除stopwords
list_except=[u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要',u'不',u'就',u'也',u'他',u'你',u'我',u'有',u'这',u'而',u'人',u'：',u'“',u'”',u'!',u'要',u'镑',u'时',u'说']
list_OK=[]
for word in list_jieba:
    if word not in list_except:
        list_OK.append(word)
#4、词频统计
#collection统计
listCounter=collections.Counter(list_OK)
#获取最高频词
listCounterTop10=listCounter.most_common(10)
#可打印展示下
print(listCounterTop10)
#5、词频展示
#取背景图
mask=np.array(Image.open('wordcloudbg.jpg'))
#创建词云对象
my_wc=wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/msyh.ttf',
    mask=mask,
    max_words=50,
    max_font_size=100
)
#生成词云
my_wc.generate_from_frequencies(listCounter)
#获取背景配色方案
bg=wordcloud.ImageColorGenerator(mask)
#对词云执行背景配色方案
my_wc.recolor(color_func=bg)
#显示词云
plt.imshow(my_wc)
#关闭坐标
#plt.axis('off')
#显示图像
plt.show()























"""
# 读取文件
fn = open('谈判是什么.txt','r',encoding='gb18030',errors='ignore') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"|\!|"\s|\xa0|\u3000|：') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要',u'不',u'就',u'也',u'他',u'你',u'我',u'有',u'这',u'而',u'人',u'：',u'“',u'”',u'!',u'要',u'镑',u'时',u'说'] # 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('wordcloudbg.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/msyh.ttf', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=200, # 最多显示词数
    max_font_size=100 # 字体最大值
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像
"""