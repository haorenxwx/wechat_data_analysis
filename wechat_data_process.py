#wechat_data_process
#首先安装itchat包
#>pip install itchat

import itchat
itchat.login()
#自动生成一个二维码，可以扫码登录自己的微信,跟登录网页版微信的形式相同

friends=itchat.get_friends(update=True)[0:]
#查看微信好友之中的好友比例
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
frame.to_csv('data.csv',index=True)
