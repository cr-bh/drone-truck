from anneal import SimAnneal
import matplotlib.pyplot as plt
import random
import pickle

pre_cost_Trcuk=5

def tsp(seedname):
    use_path = r"D:\RL_Attention_Drone+Turck\mydata\tsp_vrp\tsp_vrp200_seed{}.pkl".format(seedname)
    file = open(use_path, "rb")
    tsp = pickle.load(file)[0]
    file.close()
    return tsp

if __name__ == "__main__":
    tsp=tsp('27+127')
    sa = SimAnneal(tsp, stopping_iter=100000)
    best=sa.anneal()
    best_cost=pre_cost_Trcuk*best
    print('Best cost:',best_cost)
        #sa.visualize_routes()
        #sa.plot_learning()


