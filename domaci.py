from pulp import*
REQUIRE = {1:7, 2:5, 3:3, 4:2, 5:2}
products = [1,2,3,4,5]
locations = [1,2,3,4,5]
capacity = 8
prob = LpProblem('FacilityLocation', LpMinimize)
use_vars = LpVariable.dicts('UseLocation', locations, 0 , 1, LpBinary)
waste_vars = LpVariable.dicts('Waste', locations, 0, capacity)
assign_vars = LpVariable.dicts('AtLocation', [(i,j) for i in locations for j in products], 0 , 1, LpBinary)
prob += lpSum(waste_vars[i] for i in locations)
for j in products: 
    prob += lpSum(assign_vars[(i,j)] for i in locations) == 1
for i in locations:
    prob += lpSum(assign_vars[(i,j)] * REQUIRE[j] for j in products) + waste_vars[i] == capacity * use_vars[i]
prob.solve()
TOL = 0.00001
for i in locations:
    if use_vars[i].varValue > TOL:
        print ('Location', i, 'produces',  [j for j in products if assign_vars[(i,j)].varValue > TOL]) 