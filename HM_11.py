# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# 1)Определить корни

# 2)Найти интервалы, на которых функция возрастает

# 3)Найти интервалы, на которых функция убывает

# 4)Построить график

# 5)Вычислить вершину

# 6)Определить промежутки, на котором f > 0

# 7)Определить промежутки, на котором f < 0


from math import sqrt
from sympy import *
import matplotlib.pyplot as plt
from sympy.plotting import plot
from sympy.plotting.intervalmath import interval
init_printing(use_unicode = False, wrap_line = False, no_global = True)



x=Symbol('x')
f=-12*sin(cos(x))*(x**4)-18*(x**3)+(5*(x**2)) + (10*x) - 30
f

# построение графика
plot(f)

# поиск корней
# solve(f,x)

# Возрастание интервалов
fun1=plot(f,(x,-6.5,-4.8),show=False)
fun2=plot(f,(x,0,3.7),show=False)
fun3=plot(f,(x,7.5,10),show=False)
fun1.append(fun2[0])
fun1.append(fun3[0])
fun1.show()

#Убывание интервалов
fun1=plot(f,(x,-10,-7.5),show=False)
fun2=plot(f,(x,-4,0),show=False)
fun3=plot(f,(x,3,7),show=False)
fun1.append(fun2[0])
fun1.append(fun3[0])
fun1.show()

# промежутки, где f>0
fun1=plot(f,(x,-10,-7.64),show=False)
fun2=plot(f,(x,-5,0),show=False)
fun3=plot(f,(x,3,4.45),show=False)
fun4=plot(f,(x,8.02,10),show=False)
fun1.append(fun2[0])
fun1.append(fun3[0])
fun1.append(fun4[0])
fun1.show()

#промежутки, где f<0
fun1=plot(f,(x,-7.65,-5.03),show=False)
fun2=plot(f,(x,4.4,8),show=False)

fun1.append(fun2[0])

fun1.show()