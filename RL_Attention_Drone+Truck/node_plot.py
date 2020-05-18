import pickle
import pprint
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
np.random.seed(55)

file1=open(r"D:\RL_Attention_Drone+Turck\mydata\tsp\tsp4_seed30.pkl","rb")
file2=open(r"D:\RL_Attention_Drone+Turck\mydata\tsp_vrp\tsp_vrp12_seed30+130.pkl","rb")
tsp=pickle.load(file1)[0]
all_node=pickle.load(file2)[0]
file1.close()
file2.close()
print(all_node)

tsp_x,tsp_y,all_node_x,all_node_y=[],[],[],[]
for loc1 in tsp:
    tsp_x.append(loc1[0])
    tsp_y.append(loc1[1])
for loc2 in all_node:
    all_node_x.append(loc2[0])
    all_node_y.append(loc2[1])

x_major_locator=MultipleLocator(0.2)
y_major_locator=MultipleLocator(0.2)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
colors=np.random.random((100, 4))
for i in range(len(tsp_x)):
    plt.scatter(tsp_x[i],tsp_y[i],s=150,color=colors[i+58],marker='*')
    plt.scatter(all_node_x[i*10:(i+1)*10],all_node_y[i*10:(i+1)*10],s=70,color=colors[i+58],alpha=0.5)
plt.show()




