from validate_all_vrproute import vrpmain
from tsp_gurobi import tspmain
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

pre_cost_Drone=0.2
pre_cost_Truck=5
wait_waste=10
D_speed=60
T_speed=40

vfilename=['vrp10_seed11','vrp10_seed12','vrp10_seed13','vrp10_seed14','vrp10_seed15','vrp10_seed16','vrp10_seed17','vrp10_seed18','vrp10_seed19','vrp10_seed110','vrp10_seed111',
          'vrp10_seed112','vrp10_seed113','vrp10_seed114','vrp10_seed115','vrp10_seed116','vrp10_seed117','vrp10_seed118','vrp10_seed119','vrp10_seed120','vrp10_seed121','vrp10_seed122',
          'vrp10_seed123','vrp10_seed124','vrp10_seed125','vrp10_seed126','vrp10_seed127','vrp10_seed128','vrp10_seed129','vrp10_seed130']

tfilename=['tsp20_seed1','tsp20_seed2','tsp20_seed3','tsp20_seed4','tsp20_seed5','tsp20_seed6','tsp20_seed7','tsp20_seed8','tsp20_seed9','tsp20_seed10','tsp20_seed11','tsp20_seed12',
          'tsp20_seed13','tsp20_seed14','tsp20_seed15','tsp20_seed16','tsp20_seed17','tsp20_seed18','tsp20_seed19','tsp20_seed20','tsp20_seed21','tsp20_seed22','tsp20_seed23','tsp20_seed24',
          'tsp20_seed25','tsp20_seed26','tsp20_seed27','tsp20_seed28','tsp20_seed29','tsp20_seed30']

#vrp by gurobi
aver_vS,vS,vR={},{},{}
for i in vfilename:
    aver_a,a,b=vrpmain(i)
    aver_vS[i]=aver_a
    vS[i]=a
    vR[i]=b
print(aver_vS)

#tsp by gurobi
tS,tR={},{}
for j in tfilename:
    c,d=tspmain(j)
    tS[j]=c
    tR[j]=d

#vrp by model
aver_vSm=[6.230543041229248, 6.224304676055908,6.084807395935059,6.588123321533203,6.325970649719238,5.863704681396484,6.297189521789551,6.557597541809082,6.177675533294678,6.474045658111572,6.423516273498535,
          6.384671688079834,5.994959831237793, 6.218017387390137,6.470587253570557,6.257327938079834,6.449191856384277,6.6073540687561035, 6.337826118469238,6.313145446777344, 5.860690498352051,6.560333156585693,
          6.1846564292907715,6.083653259277344,6.165137119293213,6.42367696762085,6.0695414543151855,5.781892967224121,5.9801948165893555,5.783344650268555]

#tsp by model
tSm=[18.429847717285156,16.05390510559082,18.017466354370117,23.568866729736328,18.483970642089844,20.756900787353516,19.59755516052246,20.323984909057617,20.55538101196289,19.808849334716797,20.549929809570312,
     22.6589298248291,21.9226417541503,18.023155975341797,17.18940544128418,17.014980697631836,20.487241744995117,20.103288650512695,17.787670135498047,18.316121673583984,20.228281021118164,20.01717300415039,
     19.980161666870117,17.09262924194336,17.82257652282715,19.06007194519043,19.28888168334961,19.315969467163086,17.27978401184082,18.86043930053711]


vgaps,tgaps,g_outcomes,m_outcomes,outgaps=[],[],[],[],[]
vSg,tSg=[],[]
for k in range(30):
    vf=vfilename[k]
    tf=tfilename[k]
    vSg.append(aver_vS[vf])
    tSg.append(tS[tf])
    vgap=(aver_vSm[k]-aver_vS[vf])/aver_vSm[k]
    vgaps.append(vgap)
    tgap=(tSm[k]-tS[tf])/tSm[k]
    tgaps.append(tgap)
    g_outcome=tS[tf]*pre_cost_Truck+sum(vS[vf])*pre_cost_Drone+sum(vS[vf])/D_speed*wait_waste
    g_outcomes.append(g_outcome)
    m_outcome=tSm[k]*pre_cost_Truck+20*aver_vSm[k]*pre_cost_Drone+20*aver_vSm[k]/D_speed*wait_waste
    m_outcomes.append(m_outcome)
    outgap=(m_outcome-g_outcome)/m_outcome
    outgaps.append(outgap)

#print
print("\n gaps of drone's path:",vgaps," ; ","average gap:{}%".format(np.mean(vgaps)*100),"\n")
print("gaps of truck's path:",tgaps," ; ","average gap:{}%".format(np.mean(tgaps)*100),"\n")
print("model calculate cost:",m_outcomes,"\n")
print("gurobi calculate cost:",g_outcomes,"\n")
print("gaps of cost:",outgaps," ; ","average gap:{}%".format(np.mean(outgaps)*100),"std gap:{}".format(np.std(outgaps),"\n"))
#draw
x=list(range(1,31))

# 创建画布1
fig11 = plt.figure('Figure1',figsize = (10,15)).add_subplot(131)
fig11.fill_between(x, y1=vSg, y2=0, label="gurobi", alpha=0.3, color='purple', linewidth=0.3)
fig11.fill_between(x, y1=aver_vSm, y2=0, label="gurobi", alpha=0.3, color='blue', linewidth=0.3)
#fig11.plot(x,vSg)
#for a,b in zip(x,vSg):
#    plt.text(a, b-0.12, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "b")
#fig11.plot(x,aver_vSm)
#for a,b in zip(x,aver_vSm):
#    plt.text(a, b+0.02, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "r")
plt.xlim(1, 30)
plt.ylim(5, 10)
plt.legend(["gurobi","model"])

fig12 = plt.figure('Figure1',figsize = (10,15)).add_subplot(132)
fig12.fill_between(x, y1=tSg, y2=0, label="gurobi", alpha=0.3, color='orange', linewidth=0.5)#
fig12.fill_between(x, y1=tSm, y2=0, label="model", alpha=0.3, color='green', linewidth=0.5)
plt.xlim(1, 30)
plt.ylim(15, 30)
plt.legend(["gurobi","model"])

fig13 = plt.figure('Figure1',figsize = (10,15)).add_subplot(133)
fig13.fill_between(x, y1=g_outcomes, y2=0, label="gurobi", alpha=0.3, color='red', linewidth=0.5)#
fig13.fill_between(x, y1=m_outcomes, y2=0, label="model", alpha=0.3, color='gold', linewidth=0.5)
plt.xlim(1, 30)
plt.ylim(100, 200)
plt.legend(["gurobi","model"])

#fig12.plot(x,vgaps,'g',marker='o')
#for a,b in zip(x,vgaps):
#    plt.text(a, b+0.002, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "g")
#plt.ylim(0, 0.05)
#plt.subplots_adjust(hspace = 0.4)

# 创建画布2
fig21 = plt.figure('Figure2',figsize = (10,15)).add_subplot(311)
fig21.vlines(x, ymin=0, ymax=vgaps, color='hotpink', alpha=0.7, linewidth=2)
fig21.scatter(x, y=vgaps, s=30, color='hotpink', alpha=0.9)
fig21.xaxis.set_major_locator(MultipleLocator(1))
for a,b in zip(x,vgaps):
    plt.text(a, b+0.002, '%.3f' % b, ha='center', va= 'bottom',fontsize=6,color = "black")
plt.ylim(0, 0.05)
#fig21.plot(x,tSg)
#for a,b in zip(x,tSg):
#    plt.text(a, b-0.8, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "b")
#fig21.plot(x,tSm)
#for a,b in zip(x,tSm):
#    plt.text(a, b+0.5, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "r")
#plt.ylim(15, 30)
#plt.legend(["gurobi","model"])
fig22 = plt.figure('Figure2',figsize = (10,15)).add_subplot(312)
fig22.vlines(x, ymin=0, ymax=tgaps, color='orchid', alpha=0.7, linewidth=2)
fig22.scatter(x, y=tgaps, s=30, color='orchid', alpha=0.9)
fig22.xaxis.set_major_locator(MultipleLocator(1))
for a,b in zip(x,tgaps):
    plt.text(a, b+0.002, '%.3f' % b, ha='center', va= 'bottom',fontsize=6,color = "black")
plt.ylim(0, 0.05)
#fig22.plot(x,tgaps,'g',marker='s')
#for a,b in zip(x,tgaps):
#    plt.text(a, b+0.002, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "g")
#plt.ylim(0, 0.05)
#plt.subplots_adjust(hspace = 0.4)
fig23 = plt.figure('Figure2',figsize = (10,15)).add_subplot(313)
fig23.vlines(x, ymin=0, ymax=outgaps, color='blueviolet', alpha=0.7, linewidth=2)
fig23.scatter(x, y=outgaps, s=30, color='blueviolet', alpha=0.9)
fig23.xaxis.set_major_locator(MultipleLocator(1))
for a,b in zip(x,outgaps):
    plt.text(a, b+0.002, '%.3f' % b, ha='center', va= 'bottom',fontsize=6,color = "black")
plt.ylim(0, 0.05)
plt.subplots_adjust(hspace = 0.5)

# 创建画布3
#fig31 = plt.figure('Figure3',figsize = (10,15)).add_subplot(211)
#fig31.plot(x,g_outcomes)
#for a,b in zip(x,g_outcomes):
#    plt.text(a, b-3, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "b")
#fig31.plot(x,m_outcomes)
#for a,b in zip(x,m_outcomes):
 #   plt.text(a, b+1, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "r")
#plt.ylim(100, 180)
#plt.legend(["gurobi","model"])
#fig32 = plt.figure('Figure3',figsize = (10,15)).add_subplot(212)
#fig32.plot(x,outgaps,'g',marker='^')
#for a,b in zip(x,outgaps):
#    plt.text(a+0.5, b-0.003, '%.3f' % b, ha='center', va= 'bottom',fontsize=7,color = "g")
#plt.subplots_adjust(hspace = 0.4)
# 创建标签
fig11.set_title("(a)Length of Drone's path:model and gurobi")
fig12.set_title("(b)Length of Truck's path:model and gurobi")
fig13.set_title("(c)Cost: model and gurobi")
fig21.set_title("(a)Gaps of Length of Truck's path:model and gurobi")
fig22.set_title("(b)Gaps of Length of Truck's path:model and gurobi")
fig23.set_title("(c)Gaps of Cost:model and gurobi")
#fig31.set_title('Cost:output of model and gurobi & gaps between them')
#fig32.set_title("Gaps of cost between model and gurobi")
fig11.set_ylabel('Length')
fig11.set_xlabel('Case')
fig12.set_ylabel('Length')
fig12.set_xlabel('Case')
fig13.set_ylabel('Cost')
fig13.set_xlabel('Case')
fig21.set_ylabel('Gap')
fig21.set_xlabel('Case')
fig22.set_ylabel('Gap')
fig22.set_xlabel('Case')
#fig31.set_ylabel('Cost')
#fig31.set_xlabel('Case')
fig23.set_ylabel('Gap')
fig23.set_xlabel('Case')

plt.show()






