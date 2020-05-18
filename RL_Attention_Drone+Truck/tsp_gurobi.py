#!/usr/bin/python

# Copyright 2017, Gurobi Optimization, Inc.

# Solve a traveling salesman problem on a set of
# points using lazy constraints.   The base MIP model only includes
# 'degree-2' constraints, requiring each node to have exactly
# two incident edges.  Solutions to this model may contain subtours -
# tours that don't visit every city.  The lazy constraint callback
# adds new constraints to cut them off.


from gurobipy import *
from utils import extract


def solve_euclidian_tsp(points, threads=0, timeout=None, gap=None):
    """
    Solves the Euclidan TSP problem to optimality using the MIP formulation 
    with lazy subtour elimination constraint generation.
    :param points: list of (x, y) coordinate 
    :return: 
    """

    n = len(points)

    # Callback - use lazy constraints to eliminate sub-tours

    def subtourelim(model, where):
        if where == GRB.Callback.MIPSOL:
            # make a list of edges selected in the solution
            vals = model.cbGetSolution(model._vars)
            selected = tuplelist((i, j) for i, j in model._vars.keys() if vals[i, j] > 0.5)
            # find the shortest cycle in the selected edge list
            tour = subtour(selected)
            if len(tour) < n:
                # add subtour elimination constraint for every pair of cities in tour
                model.cbLazy(quicksum(model._vars[i, j]
                                      for i, j in itertools.combinations(tour, 2))
                             <= len(tour) - 1)

    # Given a tuplelist of edges, find the shortest subtour

    def subtour(edges):
        unvisited = list(range(n))
        cycle = range(n + 1)  # initial length has 1 more city
        while unvisited:  # true if list is non-empty
            thiscycle = []
            neighbors = unvisited
            while neighbors:
                current = neighbors[0]
                thiscycle.append(current)
                unvisited.remove(current)
                neighbors = [j for i, j in edges.select(current, '*') if j in unvisited]
            if len(cycle) > len(thiscycle):
                cycle = thiscycle
        return cycle

    # Dictionary of Euclidean distance between each pair of points

    dist = {(i,j) :
        math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(2)))
        for i in range(n) for j in range(i)}

    m = Model()
    m.Params.outputFlag = False

    # Create variables

    vars = m.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='e')
    for i,j in vars.keys():
        vars[j,i] = vars[i,j] # edge in opposite direction

    # You could use Python looping constructs and m.addVar() to create
    # these decision variables instead.  The following would be equivalent
    # to the preceding m.addVars() call...
    #
    # vars = tupledict()
    # for i,j in dist.keys():
    #   vars[i,j] = m.addVar(obj=dist[i,j], vtype=GRB.BINARY,
    #                        name='e[%d,%d]'%(i,j))


    # Add degree-2 constraint

    m.addConstrs(vars.sum(i,'*') == 2 for i in range(n))

    # Using Python looping constructs, the preceding would be...
    #
    # for i in range(n):
    #   m.addConstr(sum(vars[i,j] for j in range(n)) == 2)


    # Optimize model

    m._vars = vars
    m.Params.lazyConstraints = 1
    m.Params.threads = threads
    if timeout:
        m.Params.timeLimit = timeout
    if gap:
        m.Params.mipGap = gap * 0.01  # Percentage
    m.optimize(subtourelim)

    vals = m.getAttr('x', vars)
    selected = tuplelist((i,j) for i,j in vals.keys() if vals[i,j] > 0.5)

    tour = subtour(selected)
    assert len(tour) == n

    return m.objVal, tour


def solve_all_gurobi(dataset):
    results = []
    for i, instance in enumerate(dataset):
        #print ("Solving instance {}".format(i))
        result = solve_euclidian_tsp(instance)
        results.append(result)
    return results

def tspmain(filename):
    dataset=[extract.get_vehicle_coor(filename)]
    #print(dataset)
    r=solve_all_gurobi(dataset)
    #print(r)
    return r[0][0],r[0][1]

a,b=tspmain('tsp4_seed30')
print(a)
print(b)
'''filename=['tsp20_seed1','tsp20_seed2','tsp20_seed3','tsp20_seed4','tsp20_seed5','tsp20_seed6','tsp20_seed7','tsp20_seed8','tsp20_seed9','tsp20_seed10','tsp20_seed11','tsp20_seed12',
          'tsp20_seed13','tsp20_seed14','tsp20_seed15','tsp20_seed16','tsp20_seed17','tsp20_seed18','tsp20_seed19','tsp20_seed20','tsp20_seed21','tsp20_seed22','tsp20_seed23','tsp20_seed24',
          'tsp20_seed25','tsp20_seed26','tsp20_seed27','tsp20_seed28','tsp20_seed29','tsp20_seed30']

S,R={},{}
for j in filename:
    a,b=tspmain(j)
    S[j]=a
    R[j]=b

print('\n',S)
print('\n',R)'''