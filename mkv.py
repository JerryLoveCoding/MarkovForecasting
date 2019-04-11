import csv
import numpy as np
import matplotlib as mp
#names = globals()

filename = 'E:\markov\mydata.csv'
nodes ={}
with open(filename) as f:
    reader = csv.reader(f)#render是节点的data
    i = 1
    for row in reader:
        nodes["N"+str(i)] = row
        i = i+1
    print("风险值字典nodes")
    print(nodes)#nodes是一个节点进行20次的检测的风险值

def judgedata(score):  #这里处理的是，每行是20次轮询，然后对20个轮询计算一个平均值
    L = 20  #L是轮询次数20
    a = ""
    if score <3.9:
        a = "d1"
    elif 4.0<score<6.9:
        a = "d2"
    elif 7.0<score<10.0:
        a = "d3"
    return a
nodes2 ={}
def dealmartax():  #处理风险值字典成为风险状态字典
    global nodes
    for key in nodes:#遍历整个字典
        mylist = []
        mylist = list(map(float, nodes[key]))#把原本的str类型的风险值列表变为float类型的风险值列表
        nodestate=[]
        for score in mylist:#遍历每个字典项的列表
            myword = judgedata(score)
            nodestate.append(myword)
        nodes2[key] = nodestate
    return nodes2

nodes2 = dealmartax()
print("风险状态字典nodes2")
print(nodes2)

def judgelist(mynodes):  #计算风险字典d1，d2，d3的数量
    d11node = 0
    d12node = 0
    d13node = 0
    d21node = 0
    d22node = 0
    d23node = 0
    d31node = 0
    d32node = 0
    d33node = 0
    lenth = len(mynodes)
    for i in range(0,lenth):
        if i < lenth-1:#如果没有遍历到最后一个节点
            if mynodes[i] == "d1":
                nexti = mynodes[i + 1]
                if nexti == "d1": #如果节点的当前状态是d1，下一个状态还是d1，则P(d1-d1)=d11node/len(nodes)
                    d11node += 1
                elif nexti == "d2":
                    d12node += 1
                elif nexti == "d3":
                    d13node += 1

            elif mynodes[i] == "d2":
                nexti = mynodes[i + 1]
                if nexti =="d1":
                    d21node += 1
                elif nexti == "d2":
                    d22node += 1
                elif nexti == "d3":
                    d23node += 1
            elif mynodes[i] == "d3":
                nexti = mynodes[i + 1]
                if nexti == "d1":
                    d31node += 1
                elif nexti == "d2":
                    d32node += 1
                elif nexti == "d3":
                    d33node += 1
    state = [d11node, d12node, d13node, d21node, d22node, d23node, d31node, d32node, d33node]
    return state

nodes3 = {}
def dealstate():  #处理风险状态字典成为风险状态总览字典，即将每个节点的风险状态进行统计
    global nodes2
    for key in nodes2:
        listsum = judgelist(nodes2[key])
        nodes3[key] = listsum
    return nodes3

nodes3 = dealstate()
print("风险状态总览字典nodes3")
print(nodes3)

def ever(nod):#求字典的状态转移概率字典
    i = 0
    sum = 0
    pmar = 0
    pnodes = []
    for node in nod:
        sum += node
    for node in nod:
        p = round(node/sum, 2)
        pnodes.append(p)
    return pnodes

#使用定义6的状态转移概率公式
marnodes = {}
def markv():
    global nodes3
    for key in nodes3:
        marnodes[key] = ever(nodes3[key])
    return marnodes
marnodes = markv()
print("状态转移概率矩阵marnodes")
print(marnodes)

nextmarnodes = {}
def nextmarkv():#第一步的马氏预测概率,每个一步概率就是把状态转移概率矩阵的对应的列向量元素相加
    global marnodes
    nextmarnodes = marnodes
    p1=float()
    p2=float()
    p3=float()
    for key in marnodes:
        callist = marnodes[key]
        p1 = callist[0]+callist[3]+callist[6]
        p2 = callist[1]+callist[4]+callist[7]
        p3 = callist[2]+callist[5]+callist[8]
        nextmarnodes[key] = [p1, p2, p3]
    print("一步状态转移概率nextmarnodes")
    print(nextmarnodes)
    return nextmarnodes
nextmarnodes = nextmarkv()

onemarnodes ={}
def finish():
    global nextmarnodes
    onemarnodes = nextmarnodes.copy()
    for key in nextmarnodes:
        max = str()
        callist = nextmarnodes[key]
        if callist[0]>callist[1]:
            if callist[0]>callist[2]:
                max = "d1"
            else:
                max = "d3"
        else:
            if callist[1]>callist[2]:
                max = "d2"
            else:
                max = "d3"
        onemarnodes[key] = max
    print("一步马氏预测onemarnodes")
    print(onemarnodes)
    return onemarnodes
onemarnodes = finish()

sxnodes =[]#预测的第21次为d3的节点
realnodes = []#真实中的第20次为d3的节点
def shaixuan():
    global nodes2
    global onemarnodes
    for key in onemarnodes:
        if onemarnodes[key] == "d3":
            sxnode = key
            sxnodes.append(sxnode)
    for key in nodes2:
        jg = nodes2[key]
        if jg[19] == "d3":
            realnode = key
            realnodes.append(realnode)

    print("筛选节点")
    print(sxnodes)
    print("真实筛选节点")
    print(realnodes)
    return sxnodes, realnodes

shaixuan()

#求[11,12,21,22]这种形式表达的矩阵的N次方

#def judgerp(onemarnodes,nodes):



