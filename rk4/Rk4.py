import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    return (-1.0 * 1.0j) * (np.dot(oper,state) - np.dot(state,oper))


def rk4(func, oper, state, h):
   
    """Calculo de RK4.
    Examples:
    >>> rk4(a,b,c,d)
    7.0

    Args:
    func (funcion): First argument
    oper (): Second argument

    Returns:
        nose: Resturns the sum of the `state  


    """
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + 0.5 * k1)
    k3 = h * func(oper, state + 0.5 * k2)
    k4 = h * func(oper, state + k3)

    return state + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

times = np.linspace(0.0, 10.0, 100)
h = times[1] - times[0]
yCopy = yInit.copy()
stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)


for tt in range(times.size):
    stateQuant00[tt] = yInit[0,0].real
    stateQuant11[tt] = yInit[1,1].real

    yN = rk4(dyn_generator,oOper,yInit,h)

    yInit = yN


plt.plot(times, stateQuant00, label="State Quant 00")
plt.plot(times, stateQuant11, label="State Quant 11")
plt.xlabel("Time")
plt.ylabel("State Quant")
plt.legend()
plt.show()
