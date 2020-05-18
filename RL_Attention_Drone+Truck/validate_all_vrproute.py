from vrp_gurobi import main
import numpy as np


def vrpmain(filename):
    solutions=[]
    routes=[]
    k=20


    for i in range(k):
        solution,route=main(filename,i)
        solutions.append(solution)
        routes.append(route)


    average_length=np.mean(solutions)
    print(average_length)
    print("{}'s solutions:".format(filename),solutions)
    print("{}'s routes:".format(filename),routes)
    return average_length,solutions,routes


'''filename=['vrp10_seed11','vrp10_seed12','vrp10_seed13','vrp10_seed14','vrp10_seed15','vrp10_seed16','vrp10_seed17','vrp10_seed18','vrp10_seed19','vrp10_seed110','vrp10_seed111',
          'vrp10_seed112','vrp10_seed113','vrp10_seed114','vrp10_seed115','vrp10_seed116','vrp10_seed117','vrp10_seed118','vrp10_seed119','vrp10_seed120','vrp10_seed121','vrp10_seed122',
          'vrp10_seed123','vrp10_seed124','vrp10_seed125','vrp10_seed126','vrp10_seed127','vrp10_seed128','vrp10_seed129','vrp10_seed130']
aver_S,S,R={},{},{}
for j in filename:
    aver_a,a,b=vrpmain(j)
    aver_S[j]=aver_a
    S[j]=a
    R[j]=b

print('\n',aver_S)
print('\n',S)
print('\n',R)
'''