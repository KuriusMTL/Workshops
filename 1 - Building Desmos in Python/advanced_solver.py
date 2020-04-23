#pip install sympy, latex
from sympy import *
#init_session()
x = Symbol('x')

import math

function = 1+(math.e)**x/(1-math.e**x)
function.diff(x)
print(function.integrate(x))