import matplotlib.pyplot as plt
import numpy as np
from utils import extract



def plot_route(v_paths, v_points,d_paths,d_points):

    """
    v_path: vehicle's path
    v_points: coordinates for stop-station
    d_path: drone's path
    d_points: coordinates for customer

    """

    plt.figure('Route', figsize=(50, 50))
    v_x = []; v_y = []
    for i in v_paths:
        v_x.append(v_points[i][0])
        v_y.append(v_points[i][1])

    plt.plot(v_x, v_y, 'r*')

    # Set a scale for the arrow heads
    a_scale = float(max(v_x))/float(100)

    plt.arrow(v_x[-1], v_y[-1], (v_x[0] - v_x[-1]), (v_y[0] - v_y[-1]),
             head_width = a_scale, color = 'r',
             length_includes_head = True, ls = 'dashed',
             width = 0.03)
    for i in range(0, len(v_x)-1 ):
        plt.arrow(v_x[i], v_y[i], (v_x[i+1] - v_x[i]), (v_y[i+1] - v_y[i]),
                  head_width = a_scale, color = 'r', length_includes_head = True,
                  ls = 'dashed', width = 0.03)



#draw drone's route
    d_x=[];d_y=[]
    for i in range(len(d_paths)):#对d_paths列表中的每条路径
        d_xi = [];d_yi = []#d_paths列表中的每条路径内节点的x、y坐标值
        d_point=d_points[i]
        for j in d_paths[i]:
            d_xi.append(d_point[int(j)][0])
            d_yi.append(d_point[int(j)][1])
        d_x.append(d_xi)
        d_y.append(d_yi)

    np.seed=1234
    colors = np.random.random((300, 4))
    for k in range(len(d_x)):
        plt.scatter(d_x[k], d_y[k], color=colors[k+60],alpha=0.8)


        plt.arrow(d_x[k][-1], d_y[k][-1], (d_x[k][0] - d_x[k][-1]), (d_y[k][0] - d_y[k][-1]),
                  head_width=0.05, color='gray',ls='dashed',width=0.002 )
        for l in range(0, len(d_x[k]) - 1):
            plt.arrow(d_x[k][l], d_y[k][l], (d_x[k][l + 1] - d_x[k][l]), (d_y[k][l + 1] - d_y[k][l]),
                      head_width=0.05, color='gray', length_includes_head=True,ls='dashed', width=0.002)


    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(0,7)
    plt.ylim(0,7)
    plt.show()

f1=[0,1,  2, 3]
f2=[[3,2],[3,4],[4,4],[4,2]]
f3=[[0,1,3,2,0],[0,2,1,3,0],[0,2,3,1,0],[0,1,2,3,0]]
#f1=[0, 5, 8, 2, 12, 9, 6, 14, 17, 3, 4, 16, 13, 1, 11, 10, 18, 15, 7, 19]
#f1=extract.get_vehicle_order(r"C:\Users\ChenR\results\tsp\tsp20_seed37\tsp20_seed37-zztsp_bs32'_20200415T081158_epoch-89-greedy-t1-0-1")
#f2=extract.get_vehicle_coor('tsp4_seed100')
#f3=extract.get_drone_order(r'C:\Users\ChenR\results\cvrp\vrp10_seed1111\vrp10_seed1111-vrp_bs128_es200_56+124+160_epoch-56-greedy-t1-0-20')
'''f3=[[0,1,6,5,0,2,4,0,3,7,0,8,0,9,0,10,0],[0,1,5,0,2,7,0,9,4,10,0,3,0,6,0,8,0],[0,4,1,5,0,8,2,10,0,3,0,6,0,7,0,9,0],[0,2,4,0,3,7,8,0,5,9,0,1,0,6,0,10,0],[0,2,5,0,3,6,0,8,4,9,0,1,0,7,0,10,0],
    [0,8,1,5,4,10,0,6,0,7,0,9,0,2,0,3,0],[0,2,5,6,8,0,4,9,0,10,0,1,0,3,0,7,0],[0,3,9,8,0,4,5,7,0,2,0,1,0,6,0,10,0],[0,2,4,0,10,3,7,8,0,1,0,5,0,6,0,9,0],[0,1,6,2,0,7,10,8,0,3,0,4,0,5,0,9,0],
    [0,3,5,8,10,4,0,6,0,1,0,2,0,9,0,7,0],[0,1,5,2,0,4,9,0,7,10,0,3,0,6,0,8,0],[0,1,3,0,2,6,0,4,5,9,0,8,0,7,0,10,0],[0,1,6,0,2,4,0,7,9,8,0,5,0,3,0,10,0],[0,2,7,5,6,0,8,10,0,3,0,4,0,1,0,9,0],
    [0,2,6,9,0,3,4,0,5,7,0,1,0,8,0,10,0],[0,1,6,0,3,7,4,8,0,2,0,5,0,9,0,10],[0,3,5,0,4,10,0,6,7,8,0,1,0,2,0,9,0],[0,2,6,9,8,10,0,1,0,4,0,3,0,5,0,7,0],[0,4,7,10,0,5,9,8,0,1,0,3,0,2,0,6,0]]'''

'''#f3=[[0,1,6,5,0,2,4,0,3,7,8,0,9,10,0],[0,1,5,0,2,7,0,9,4,10,0,3,0,6,0,8,0],[0,4,1,5,0,8,2,10,0,3,6,0,7,9,0],[0,2,4,0,3,7,8,0,5,9,0,1,0,6,0,10,0],[0,2,5,0,3,6,0,8,4,9,0,1,0,7,10,0],
    [0,8,1,5,4,10,0,6,0,7,9,0,2,3,0],[0,2,5,6,8,0,4,9,0,10,0,1,0,3,0,7,0],[0,3,9,8,0,4,5,7,0,2,0,1,0,6,0,10,0],[0,2,4,0,10,3,7,8,0,1,0,5,0,6,0,9,0],[0,1,6,2,0,7,10,8,0,3,0,4,0,5,9,0],
    [0,3,5,8,10,4,0,6,0,1,2,0,9,7,0],[0,1,5,2,0,4,9,0,7,10,0,3,0,6,8,0],[0,1,3,0,2,6,0,4,5,9,0,8,0,7,10,0],[0,1,6,0,2,4,0,7,9,8,0,5,0,3,0,10,0],[0,2,7,5,6,0,8,10,0,3,0,4,0,1,9,0],
    [0,2,6,9,0,3,4,0,5,7,0,1,0,8,0,10,0],[0,1,6,0,3,7,4,8,0,2,0,5,0,9,0,10],[0,3,5,0,4,10,0,6,7,8,0,1,0,2,9,0],[0,2,6,9,8,10,0,1,0,4,0,3,5,0,7,0],[0,4,7,10,0,5,9,8,0,1,0,3,0,2,6,0]]'''
f4=extract.get_drone_coor('vrp3_seed56')
print(f1,'\n')
print(f2,'\n')
print(f3,'\n')
print(f4,'\n')
plot_route(f1,f2,f3,f4)
