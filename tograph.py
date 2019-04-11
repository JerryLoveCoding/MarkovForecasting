#不同数量下的节点的真实高危节点风险值和预测高危节点风险值
import matplotlib.pyplot as plt
import numpy as np

#x = [1,2,3,4,5,6,7,8,9,10]
x=['100', '200', '400', '600', '800', '1000']
y = [7.51, 7.9553,  8.0272,  8.1064, 8.1604, 8.1422]#预测高危节点风险值序列
y1 = [8.5674, 8.6392, 8.5880, 8.6397, 8.6253, 8.6327]#真实高危节点风险值序列
#creat new figure
ax1 = plt.subplot()
#ax1.set_title('', fontsize=15)

plt.xlabel("Node")
plt.ylabel("Level")
yzhou = range(5,10)
xzhou = range(len(x))

p1 = plt.scatter(x, y, marker='x')
p2 = plt.scatter(x, y1, marker='>')
plt.plot(x, y)
plt.plot(x, y1)
plt.legend([p1, p2], ['predictive risk score', 'real risk score'], loc=7)
plt.xticks(xzhou, x)
plt.yticks(yzhou)
plt.show()