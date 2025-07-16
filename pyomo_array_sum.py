import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pandas as pd

dataGen = pd.read_excel('array_sum.xlsx', sheet_name='gen')  # generators data
dataLoad = pd.read_excel('array_sum.xlsx', sheet_name='load')  # generators data
nGen = len(dataGen)

# model
model = pyo.ConcreteModel()
# model variable = production amount per generator
model.Pg = pyo.Var(range(nGen), bounds=(0, None))
Pg = model.Pg

# 2 dimensions - 1 for number of generators, 2 for time domain
#model.Pg = pyo.Var(range(nGen), range(3), bounds=(0, None))


# constraints
# sum of model variable must be with list comprehension
# sum of a data frame which is an array can be done directly
Pg_sum = sum([Pg[g] for g in dataGen.id])
model.balance = pyo.Constraint(expr= Pg_sum == sum(dataLoad.value))
model.condition = pyo.Constraint(expr= Pg[0] + Pg[3] >= dataLoad.value[0])

model.limits = pyo.ConstraintList()
for g in dataGen.id:
    model.limits.add(expr = Pg[g] <= dataGen.limit[g])


# objective function
cost_sum = sum([Pg[g] * dataGen.cost[g] for g in dataGen.id])
model.obj = pyo.Objective(expr= cost_sum, sense=minimize)

opt = SolverFactory('glpk')
results = opt.solve(model)
dataGen['Pg'] = [pyo.value(Pg[g]) for g in dataGen.id]
print(dataGen)
