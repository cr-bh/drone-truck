n200=[336.6285421430624,270.4109892998506,319.72339328336363,343.35384818219694,349.98605453772535,324.4199160376232,336.62011739428806,345.6061905161024,321.4625643671158,368.378088182341,
      349.6947934185305,341.59281866027914,341.8005797539147, 299.4363910039686,316.5189245239892,297.4966315935723,370.79442998435303, 333.52508230851913,285.32966056302814,316.67158544568053,317.3666724189706,
      353.4644522644799,345.2847221612188,310.6766660145798,302.33920530654984,319.7765934724334, 331.79752997653725,337.48926695659645,289.2724759298329,288.9875075284238]

DT=[136.76282110991878, 123.93311581729282, 129.63728519053615, 164.91412532803275, 138.15126200490587, 142.84420714342326, 142.56683707642955, 147.9729344819827, 145.51195507876773, 144.71234272147748,
    147.29468312139642, 158.2721737951041, 151.54514674035613, 132.52484434334949, 130.74794603426918, 129.8644890093296, 149.7200227738323, 146.68475327637245, 132.51397569165255, 136.8943651668567,
    143.175578872132, 145.42782532105258, 141.2615263230788, 127.56713948503767, 130.33394671185968, 139.57830096717203, 138.4823200485036, 137.52806272608925, 127.93990677446338, 133.90695251017004]


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from matplotlib.pyplot import MultipleLocator

T_speed=40
D_speed=60
x=list(range(1,31))
cgap=[]
for i in x:
    cgap.append((n200[i-1]-DT[i-1])/n200[i-1])
print(cgap)
print(np.mean(cgap),np.std(cgap))

#draw
'''x_index = np.arange(30)  # 确定label的位置
bar_width = 0.4  # 定义一个数字代表独立柱的宽度

plt.xticks(x_index + bar_width/2, x)  # 设定x轴
plt.legend()  # 显示图例
plt.title('Cost between different pattern')
plt.tight_layout()
# plt.grid(axis="y")
plt.grid(ls='-.')  # 绘制背景线
plt.show()'''

# 创建画布1
x_index = np.arange(1,31)
bar_width = 0.4
fig= plt.figure('Figure1',figsize = (10,15))
ax =fig.add_subplot(111)
ax.bar(x_index-bar_width/2, n200, width=bar_width, alpha=0.4, color="limegreen")
ax.bar(x_index+bar_width/2, DT, width=bar_width, alpha=0.4, color="forestgreen")
ax.xaxis.set_major_locator(MultipleLocator(1))
plt.legend(["truck","drone+truck"])
plt.ylim(0, 1000)
ax1=ax.twinx()
x_new = np.linspace(1,30,300) #300 represents number of points to make between T.min and T.max
y_smooth = spline(x,cgap,x_new)
ax1.plot(x_index,cgap,c='seagreen',linewidth=2)
#ax1.scatter(x, cgap, c='g',alpha = 0.3,s=150)
plt.ylim(0, 0.8)
plt.xlim(0.6,30.4)


'''fig11.plot(x_index,n200, alpha=0.4, color="b",marker='*')
for a,b in zip(x,n200):
    plt.text(a, b-0.12, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "b",alpha = 0.8)
fig11.plot(x_index+0.4,DT, alpha=0.4, color="r",marker='.')
for a,b in zip(x,DT):
    if a%2==0:
        plt.text(a, b+10, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "r",alpha = 0.8)
    else:
        plt.text(a, b-10, '%.3f' % b, ha='center', va='bottom', fontsize=7, color="r",alpha = 0.8)
rects1 = fig11.bar(x_index, n200, width=bar_width, alpha=0.4, color="b")
rects2 = fig11.bar(x_index+bar_width, DT, width=bar_width, alpha=0.4, color="r")
plt.xticks(x_index + bar_width/2, x)
plt.grid(ls='-.')
plt.ylim(100, 450)
plt.legend(["truck","drone+truck"])
fig12 = plt.figure('Figure1',figsize = (10,15)).add_subplot(212)
x_new = np.linspace(1,30,300) #300 represents number of points to make between T.min and T.max
y_smooth = spline(x,cgap,x_new)
fig12.plot(x_new,y_smooth,c='g')
fig12.scatter(x, cgap, c='g',alpha = 0.5)
for a,b in zip(x,cgap):
    plt.text(a, b+0.002, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "g")
plt.grid(ls='-.')
plt.ylim(0, 1)
plt.subplots_adjust(hspace = 0.4)'''

ax.set_title("Cost between different pattern")
'''fig12.set_title("Gaps of Cost between different pattern")
fig11.set_ylabel('Cost')
fig11.set_xlabel('Case')
fig12.set_ylabel('Gap')
fig12.set_xlabel('Case')'''


plt.show()