#wechat_data_process
#首先安装itchat包
#>pip install itchat

import itchat
itchat.login()
#自动生成一个二维码，可以扫码登录自己的微信,跟登录网页版微信的形式相同

friends=itchat.get_friends(update=True)[0:]
#查看微信好友之中的好友比例
'''
male=female=other=0
for i in friends[1:]:
	sex=i["Sex"]
	if sex==1:
		male+=1
	elif sex==2:
		female+=1
	else:
		other+=1
total=len(friends[1:])
#打印好友比例
print("男性好友：%.2f%%"%(float(male)/total*100)+"\n"+
	"女性好友：%.2f%%"%(float(female)/total*100)+"\n"+
	"未知：%.2f%%"%(float(other)/total*100))


#查看微信好友的城市分布
def get_var(var):
	variable=[]
	for i in friends:
		value =i[var]
		variable.append(value)
	return variable
#定义了一个可以取变量对应值得函数
NickName=get_var("NickName")
Sex=get_var("Sex")
Province=get_var("Province")
City=get_var("City")
Signature=get_var("Signature")

from pandas import DataFrame
data={'NickName':NickName,'Sex':Sex,'Province':Province,'City':City,'Signature':Signature}
frame=DataFrame(data)
#得到了格式为DataFrame的待处理数据
frame.to_csv('data.csv',index=True)'''

import re
siglist=[]
#sig=d.iloc[:,5]
#sig_str=sig.astype(str)
for i in friends:
	#signature=total[i,5].strip().replace("span","").replace("class","").replace("emoji","")
	signature=i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")#删除数据中非文字的部分
	rep=re.compile("1f\d+\w*|[<>/=]")#预编译正则表达式
	signature=rep.sub("",signature)
	siglist.append(signature)
text="".join(siglist)

import jieba
wordlist=jieba.cut(text,cut_all=True)
word_space_split=" ".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
font=r"E:/study/python/WordCloudLearning/simhei.ttf"
coloring = np.array(Image.open("E:/study/python/WordCloudLearning/onepiece.png"))
my_wordcloud=WordCloud(collocations=False,
	#font_path ="HYQiHei-25J.ttf",
	font_path=font,
	#指定字体
	#font_path =path.join(d,"HYQiHei-25J.ttf"),
	background_color='white',
	#设置背景色
	mask=coloring,
	#词云形状
	max_words=500,
	max_font_size=40).generate(word_space_split)

image_colors=ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))

plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()