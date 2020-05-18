import pickle
import numpy as np

def get_vehicle_coor(filename):
    use_path=r"D:\RL_Attention_Drone+Turck\mydata\tsp\{}.pkl".format(filename)
    file = open(use_path, "rb")
    tsp_coor = pickle.load(file)[0]
    file.close()
    return tsp_coor

def get_drone_coor(filename):
    use_path = r"D:\RL_Attention_Drone+Turck\mydata\vrp\{}.pkl".format(filename)
    file = open(use_path, "rb")
    cust = pickle.load(file)
    file.close()
    cust_coors=[]
    for i in cust:
        cust_coor=[]
        cust_coor.append(i[0])
        for j in i[1]:
            cust_coor.append(j)
        cust_coors.append(cust_coor)
    return cust_coors

def get_vehicle_order(filename):
    use_path = "{}.pkl".format(filename)
    file = open(use_path, "rb")
    v_order=pickle.load(file)[0][0][1]
    file.close()
    return v_order

def get_drone_order(filename):
    use_path = "{}.pkl".format(filename)
    file = open(use_path, "rb")
    result = pickle.load(file)[0]
    file.close()
    d_order=[]
    for i in result:
        tour=i[1]
        tour.insert(0,0)
        d_order.append(tour)
    return d_order

def v_dorder_align(v_order,d_order):
    return np.array(d_order).take(v_order).tolist()

def v_dcoor_align(v_order,d_coor):
    return np.array(d_coor)[v_order].tolist()


'''f4=get_drone_coor('vrp10_seed608')
f3=get_drone_order('vrp10_seed0-pretrained_cvrp_10-greedy-t1-0-20')
f2=get_vehicle_coor('tsp20_seed2048')
f1=get_vehicle_order('tsp20_seed2048-pretrained_tsp_20-greedy-t1-0-1')
#f5=v_dorder_align(f4,f2)
#f6=v_dcoor_align(f4,f1)
print(len(f1),f1)
print(len(f2),f2)
print(len(f3),f3)
print(len(f4),f4)
#print(f5)
#print(f6)
'''



