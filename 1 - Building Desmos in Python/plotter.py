import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

import math

def quadratic_function(x):
    return x**2

start = int(input("Start: "))
end = int(input("End: "))


x_values = []
y_values = []

for i in range(start*100, end*100):

    x_values.append(i/100)
    y_values.append(quadratic_function(i/100))

#Static plot
plt.plot(x_values, y_values)
plt.show()

#interactive plot
import plotly.express as px
fig = px.line(x_values, y_values)
fig.show()
