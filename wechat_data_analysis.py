#wechat_data_analysis

import numpy as np
import pandas as pd
import matplotlib.pylab as pyl

d=pd.read_csv("E:/study/python/wechatdata.csv",encoding='gbk')#导入之前爬取的数据
total=d.as_matrix()#转化为可处理数据
#1查看好友中的男女比例
male=female=other=0#初始化
for i in range(0,len(d)):
	if total[i,4]==2:
		female+=1
	elif total[i,4]==1:
		male+=1
	else:
		other+=1
male_perc=float(male)/len(total)*100
female_perc=float(female)/len(total)*100
other_perc=float(other)/len(total)*100

#2整理好友的签名
import re
siglist=[]
sig=d.iloc[:,5]
sig_str=sig.astype(str)
for i in range(0,len(total)):
	#signature=total[i,5].strip().replace("span","").replace("class","").replace("emoji","")
	signature=sig_str[i].strip().replace("span","").replace("class","").replace("emoji","")
	rep=re.compile("1f\d+\w*|[<>/=]")
	signature=rep.sub("",signature)
	siglist.append(signature)
text="".join(siglist)

import jieba
wordlist=jieba.cut(text,cut_all=True)
word_space_split=" ".join(wordlist)