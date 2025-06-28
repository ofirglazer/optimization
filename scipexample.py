''' SCIP framework selects solver
it is not possible to select solvers manually
linear and non-linear may be solved
'''

from pyscipopt import Model

model = Model('ex_model')

x = model.addVar('x')
y = model.addVar('y')
model.setObjective(x+y, sense='maximize')

model.addCons(-x+2*y<=8)
# model.addCons(-x+2*x*y<=8)

model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

model.optimize()
solution = model.getBestSol()

print('x=', solution[x])
print('y=', solution[y])
