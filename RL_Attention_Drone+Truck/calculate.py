import pickle
import numpy as np

file_tsp=open(r"C:\Users\ChenR\results\tsp\tsp20_clip40_greedy.pkl","rb")
file_cvrp=open(r"C:\Users\ChenR\results\cvrp\vrp10_seed147\vrp10_seed147-'vrp10_rollout'_20200411T144751_epoch-135-greedy-t1-0-20.pkl","rb")
tsp_result=pickle.load(file_tsp)[0][0]
cvrp_result=pickle.load(file_cvrp)[0]
file_tsp.close()
file_cvrp.close()

pre_cost_Drone=0.2
pre_cost_Truck=5
wait_waste=10
D_speed=60
T_speed=40

#def open_pkl(tfilename,vfilename):
 #   file_tsp = open(tfilename, "rb")
  #  file_cvrp = open(vfilename,"rb")
   # tsp_result = pickle.load(file_tsp)[0][0]
    #cvrp_result = pickle.load(file_cvrp)[0]
    #file_tsp.close()
    #file_cvrp.close()
    #return tsp_result,cvrp_result

def r_split(order):
    if len(order)==3:
        tsp_length=order[0]
        tsp_tour=order[1]
        tsp_time=order[2]
        return tsp_length,tsp_tour,tsp_time
    else:
        cvrp_length,cvrp_tour,cvrp_time=[],[],[]
        for i in order:
            cvrp_length.append(i[0])
            cvrp_tour.append(i[1])
            cvrp_time.append(i[2])
        return cvrp_length,cvrp_tour,cvrp_time

def total_cost(L_TSP,L_CVRP):
    return L_TSP*pre_cost_Truck+sum(L_CVRP)*pre_cost_Drone+sum(L_CVRP)/D_speed*wait_waste

def total_time(tsp_time,cvrp_time):
    return tsp_time+sum(cvrp_time)

def relate_route(tsp_tour,vrp_tour):
    integration={}
    indices=tsp_tour
    vrp_route=list(np.array(vrp_tour).take(indices))
    for node in tsp_tour:
        integration[node]=vrp_tour[node]
    return tsp_tour,vrp_route,integration


if __name__ == "__main__":
    tsp_length,tsp_tour,tsp_time=r_split(tsp_result)
    cvrp_length,cvrp_tour,cvrp_time=r_split(cvrp_result)
    tsp_route,vrp_route,integration=relate_route(tsp_tour,cvrp_tour)
    totalcost=total_cost(tsp_length,cvrp_length)
    totaltime=total_time(tsp_time,cvrp_time)
    print('total cost:',totalcost)
    print('duration:',totaltime)
    print('Truck and Drone paths:',integration)

