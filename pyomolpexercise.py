import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(None, 3))
model.y = pyo.Var(bounds=(0, None))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= x+y<=8)
model.C2 = pyo.Constraint(expr= 8*x+3*y>=-24)
model.C3 = pyo.Constraint(expr= -6*x+8*y<=48)
model.C4 = pyo.Constraint(expr= 3*x+5*y<=15)

model.obj = pyo.Objective(expr= -4*x-2*y, sense=minimize)
opt = SolverFactory('glpk')

start_time = time.time()
opt.solve(model)

model.pprint()
print(f'calculation time ={time.time() - start_time}')
x_value = pyo.value(x)
y_value = pyo.value(y)
print('x= ', x_value)
print('y= ', y_value)
