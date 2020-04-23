import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def function(x, a, b):
    return [float(((1-x**2/a**2) * b**2)**0.5), float(-((1-x**2/a**2) * b**2)**0.5)]

a = int(input("A parameter: "))
b = int(input("B parameter: "))

x_values = []
y_values = []

for i in range(-a, a+1, 1):

    x_values.append(i)
    y_values.append(function(i,a,b)[0])
    x_values.append(i)
    y_values.append(function(i,a,b)[1])

plt.scatter(x_values, y_values)
plt.show()