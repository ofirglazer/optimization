''' ortools is a solver from Google
ortools are only useful for linear programming '''

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')  # there is also Gurobi solver

x = solver.NumVar(0, 10, 'x')
y = solver.NumVar(0, 10, 'y')

solver.Add(-x+2*y<=8)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

solver.Maximize(x+y)

results = solver.Solve()
if results == pywraplp.Solver.OPTIMAL: print('optimal found')
print('x: ', x.solution_value())
print('y: ', y.solution_value())