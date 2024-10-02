def rk4(func, oper, state, h):
   
    """Calculo de las ecuaciones de Runge-Kutta orden 4, mediante definir los valores de k1, k2, k3 y k4 para posterior calcular el valor y_n+1 y devolver este valor. 

    Examples:
        >>> rk4(a,b,c,d)
        7.0

    Args:
        func (función): First argument
        oper (numpy.ndarray): Second argument
        state (numpy.ndarray): Third argument
        h (numpy.float64): Fourth argument 

    Returns:
       result (numpy.ndarray): Retorna el valor de y_n+1 obtenido mediante el método Rk4  

    """

    k1 = h * func(oper, state)
    k2 = h * func(oper, state + 0.5 * k1)
    k3 = h * func(oper, state + 0.5 * k2)
    k4 = h * func(oper, state + k3)

    return state + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

