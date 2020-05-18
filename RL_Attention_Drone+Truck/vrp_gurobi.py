"""
vrp.py:  model for the vehicle routing problem using callback for adding cuts.

approach:
    - start with assignment model
    - add cuts until all components of the graph are connected
reference: Prof. KUBO's code
"""

import networkx
from gurobipy import *
import pickle
import numpy as np


def vrp(V, c, m, q, Q):
    """solve_vrp -- solve the vehicle routing problem.
       - start with assignment model (depot has a special status)
       - add cuts until all components of the graph are connected
    Parameters:
        - V: set/list of nodes in the graph
        - c[i,j]: cost for traversing edge (i,j)
        - m: number of vehicles available
        - q[i]: demand for customer i
        - Q: vehicle capacity
    Returns the optimum objective value and the list of edges used.
    """

    def vrp_callback(model, where):
        """vrp_callback: add constraint to eliminate infeasible solutions
        Parameters: gurobi standard:
            - model: current model
            - where: indicator for location in the search
        If solution is infeasible, adds a cut using cbLazy
        """
        # remember to set     model.params.DualReductions = 0     before using!
        # remember to set     model.params.LazyConstraints = 1     before using!
        if where != GRB.callback.MIPSOL:
            return
        edges = []
        for (i, j) in x:
            if model.cbGetSolution(x[i, j]) > .5:
                if i != V[0] and j != V[0]:
                    edges.append((i, j))
        G = networkx.Graph()
        G.add_edges_from(edges)
        Components = networkx.connected_components(G)
        for S in Components:
            S_card = len(S)
            q_sum = sum(q[i] for i in S)
            NS = int(math.ceil(float(q_sum) / Q))
            S_edges = [(i, j) for i in S for j in S if i < j and (i, j) in edges]
            if S_card >= 3 and (len(S_edges) >= S_card or NS > 1):
                model.cbLazy(quicksum(x[i, j] for i in S for j in S if j > i) <= S_card - NS)
                print("adding cut for", S_edges)
        return

    model = Model("vrp")
    x = {}
    for i in V:
        for j in V:
            if j > i and i == V[0]:  # depot
                x[i, j] = model.addVar(ub=2, vtype="I", name="x(%s,%s)" % (i, j))
            elif j > i:
                x[i, j] = model.addVar(ub=1, vtype="I", name="x(%s,%s)" % (i, j))
    model.update()

    model.addConstr(quicksum(x[V[0], j] for j in V[1:]) == 2 * m, "DegreeDepot")
    for i in V[1:]:
        model.addConstr(quicksum(x[j, i] for j in V if j < i) +
                        quicksum(x[i, j] for j in V if j > i) == 2, "Degree(%s)" % i)

    model.setObjective(quicksum(c[i, j] * x[i, j] for i in V for j in V if j > i), GRB.MINIMIZE)

    model.update()
    model.__data = x
    return model, vrp_callback


def distance(x1, y1, x2, y2):
    """distance: euclidean distance between (x1,y1) and (x2,y2)"""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def make_data(n,filename,k):
    """make_data: compute matrix distance based on euclidean distance"""
    use_path = r"D:\RL_Attention_Drone+Turck\mydata\vrp\{}.pkl".format(filename)
    file = open(use_path, "rb")
    vrp = pickle.load(file)[k]##change
    file.close()
    V = range(1, n + 1)
    tem_x = [vrp[0][0]]
    tem_y = [vrp[0][1]]
    for i in vrp[1]:
        tem_x.append(i[0])
        tem_y.append(i[1])
    x= dict([(i,tem_x[i-1]) for i in V])
    y= dict([(i,tem_y[i-1]) for i in V])
    c, q = {}, {}
    tem_q=vrp[2]
    Q = 20
    for i in V:
        if i==1:
            q[i] = 0
        else:
            q[i]=tem_q[i-2]
        for j in V:
            if j > i:
                c[i, j] = distance(x[i], y[i], x[j], y[j])
    return V, c, q, Q


def main(filename,k):


    n = 11
    m = 6
    #seed = 1
    #random.seed(seed)
    V, c, q, Q = make_data(n,filename,k)
    model, vrp_callback = vrp(V, c, m, q, Q)

    # model.Params.OutputFlag = 0 # silent mode
    model.params.DualReductions = 0
    model.params.LazyConstraints = 1
    model.optimize(vrp_callback)
    x = model.__data

    edges = []
    for (i, j) in x:
        if x[i, j].X > .5:
            if i != V[0] and j != V[0]:
                edges.append((i, j))

    return model.ObjVal,sorted(edges)


#调用
S,R=[],[]
for i in range(20):
    best_object,best_route=main('vrp10_seed1111',i)
    S.append(best_object)
    R.append(best_route)
print(S)
print(np.mean(S))
print(R)
#print("Optimal solution:", best_object)
#print("Edges in the solution:")
#print(best_route)
