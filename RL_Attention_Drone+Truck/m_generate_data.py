import numpy as np
import os
from utils.data_utils import check_extension, save_dataset

tsp_seed=60
cvrp_seed=10
tsp_cvrp_seed='{}+{}'.format(tsp_seed,cvrp_seed)

def generate_tsp_data(dataset_size, tsp_size):
    np.random.seed(tsp_seed)
    return np.random.uniform(1,6,size=(dataset_size, tsp_size, 2)).tolist()

def generate_cvrp_data(tsp_list, vrp_size,capacity,cov):
    np.random.seed(cvrp_seed)
    vrp_data=[]
    for loc in tsp_list:
        #print('@',coors,'\n')
        #vrp_data.append(coors)
    #print('*',vrp_data,len(vrp_data),'\n')
        vrp_data.append(np.random.multivariate_normal(loc, cov, size=vrp_size).tolist())
    cvrp_data = list(zip(
        tsp_list,  # Depot location
        vrp_data,  # Node locations
        np.random.randint(1, 10, size=(len(tsp_list), vrp_size)).tolist(),  # Demand, uniform integer 1 ... 9
        np.full(len(tsp_list), capacity).tolist()  # Capacity, same for whole dataset
    ))
    return cvrp_data

def generate_total_tsp_data(cvrp_list):
    nodes=[]
   # demands=[]
    for unit in cvrp_list:
        for i in unit[1]:
            nodes.append(i)
       # for j in unit[2]:
        #    demands.append(j)
   # total_cvrp_data=[([0,0],nodes,demands,capacity)]
    return [nodes]

def named(problem,list,data_dir='mydata'):
    datadir = os.path.join(data_dir, problem)
    os.makedirs(datadir,exist_ok=True)
    if problem=='tsp':
        graph_size=len(list[0])
        seed=tsp_seed
    elif problem=='vrp':
        graph_size=len(list[0][1])
        seed=cvrp_seed
    else:
        graph_size=len(list[0])
        seed=tsp_cvrp_seed
    filename = os.path.join(datadir, "{}{}_seed{}.pkl".format(problem,graph_size,seed))
    return filename

if __name__ == "__main__":
    tsp_data=generate_tsp_data(1,20)
    cvrp_data=generate_cvrp_data(tsp_data[0],10,20,[[0.2,0],[0,0.2]])
    total_tsp_data=generate_total_tsp_data(cvrp_data)
    file={'tsp':tsp_data,'vrp':cvrp_data,'tsp_vrp':total_tsp_data}
    for problem,list in file.items():
        print(list)
        filename=named(problem,list)
        save_dataset(list, filename)

'''c=generate_tsp_data(1,3)
a=generate_cvrp_data([[1,2],[3,4],[5,6]],5,10,[[0.1,0],[0,0.1]])
print(a)
print(c)

   for loc in tsp_list:
        coors=[]
        if 3<=loc[0]<=4 and 5<=loc[1]<=6:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.35)
                vrp_y=np.random.normal(loc[1],0.5)
                coors.append([vrp_x,vrp_y])
        elif 4<=loc[0]<=5 and 1<=loc[1]<=1.5:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.3)
                vrp_y=np.random.normal(loc[1],1)
                coors.append([vrp_x,vrp_y])
        elif 1<=loc[0]<=2 and 2<=loc[1]<=3:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.4)
                vrp_y=np.random.normal(loc[1],0.5)
                coors.append([vrp_x,vrp_y])
        elif 1<=loc[0]<=2 and 1<=loc[1]<=2:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.4)
                vrp_y=np.random.normal(loc[1],0.5)
                coors.append([vrp_x,vrp_y])
        elif 1<=loc[0]<=2 and 3<=loc[1]<=4:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.25)
                vrp_y=np.random.normal(loc[1],0.4)
                coors.append([vrp_x,vrp_y])
        elif 1<=loc[0]<=2 and 5<=loc[1]<=6:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.4)
                vrp_y=np.random.normal(loc[1],0.3)
                coors.append([vrp_x,vrp_y])
        else:
            for i in range(10):
                vrp_x=np.random.normal(loc[0],0.2)
                vrp_y=np.random.normal(loc[1],0.3)
                coors.append([vrp_x,vrp_y])'''