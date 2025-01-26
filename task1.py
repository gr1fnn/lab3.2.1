from pulp import LpVariable, LpProblem, LpMaximize, value, LpMinimize
import time

start = time.time()
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
problem = LpProblem('0', LpMinimize)
problem += 1200*x1 + 1000*x2 + 1500*x3 + 1200*x4, "Функция цели"
problem += 18*x1 + 26*x2 + 16* x3 + 10*x4 <= 110000, "1"
problem += 150*x1 + 140*x2 + 50* x3 + 80*x4 <= 950000, "2"
problem += 170*x1 + 230*x2 + 280*x3 + 120*x4 <= 1200000, "3"
problem += 31*x1 + 42*x2 + 30*x3 + 20*x4 <= 180000, "4"
problem += 200*x1 + 150*x2 + 170*x3 + 50*x4 >= 750000, "5"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print (variable.name, "=", round(variable.varValue, 2))
print("Объем ресурса:")
print(round(value(problem.objective),2))
stop = time.time()
print ("Время :")
print(stop - start)
print ("первое :")


start = time.time()
t1 = LpVariable("t1", lowBound=0)
t2 = LpVariable("t2", lowBound=0)
t3 = LpVariable("t3", lowBound=0)
t4 = LpVariable("t4", lowBound=0)
secondproblem = LpProblem('0', LpMinimize)
secondproblem += 120*t1 + 50*t2 + 30*t3 + 100*t4, "Функция цели"
secondproblem += 18*t1 + 26*t2 + 16* t3 + 10*t4 <= 110000, "1"
secondproblem += 150*t1 + 140*t2 + 50* t3 + 80*t4 <= 950000, "2"
secondproblem += 170*t1 + 230*t2 + 280*t3 + 120*t4 <= 1200000, "3"
secondproblem += 31*t1 + 42*t2 + 30*t3 + 20*t4 <= 180000, "4"
secondproblem += 200*t1 + 150*t2 + 170*t3 + 50*t4 >= 750000, "5"
secondproblem += 1200*t1 + 1000*t2 + 1500*t3 + 1200*t4 >= round(value(problem.objective),2), "6"
secondproblem.solve()
print("Результат:")
for var in secondproblem.variables():
    print (var.name, "=", round(var.varValue, 2))
print("Объем ресурса:")
print(round(value(secondproblem.objective),2))
stop = time.time()
print ("Время :")
print(stop - start)
print ("второе :")
