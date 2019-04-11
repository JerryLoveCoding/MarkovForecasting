import matplotlib.pyplot as plt
import mkv

shaixuannodes, zhenshinodes = mkv.shaixuan()
print("shaixuan")
print(shaixuannodes)
print("zhenshi")
print(zhenshinodes)

thisnodes = mkv.nodes.copy()
print("samplemarkov下的nodes")
print(thisnodes)

shaixuanscore = float()#定义筛选序列高危风险值
zhenshiscore = float()#定义真实序列高危风险值
shaixuanlist =[]
zhenshilist = []
def dealgaowei():#处理shaixuannodes和zhenshinodes的高危风险值
    sum1 = float()#sum1是筛选序列高危风险总和，sum2是真实序列的
    sum2 = float()
    for i in shaixuannodes:
        thisnodeslist = thisnodes[i].copy() #取到每个预测高危节点对应的轮询list
        sum1 += float(thisnodeslist[19])
        shaixuanlist.append(float(thisnodeslist[19]))
    for i in zhenshinodes:
        thisnodeslist = thisnodes[i].copy()
        sum2 += float(thisnodeslist[19])
        zhenshilist.append(float(thisnodeslist[19]))
    global shaixuanscore
    global zhenshiscore
    for i in shaixuanlist:
        shaixuanscore += (i*i)/sum1
    for i in zhenshilist:
        zhenshiscore += (i*i)/sum2

    return shaixuanscore, zhenshiscore

shaixuanscore, zhenshiscore=dealgaowei()
print("筛选分")
print(shaixuanscore)
print("真实分")
print(zhenshiscore)

#creat new figure
# plt.subplot(2,3,6)
# plt.scatter(x,y)
# plt.show()