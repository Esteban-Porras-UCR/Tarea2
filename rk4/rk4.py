def rk4(func, oper, state, h):
   
    """Calculo de las ecuaciones de Runge-Kutta orden 4, mediante definir los valores de k1, k2, k3 y k4 para posterior calcular el valor $y_{n+1}$ y devolver este valor. 

    Examples:
        >>> oper = np.array([0,1],[1,0])
        >>> state = np.array([1,0],[0,0])
        >>> h = 0.10
        >>> rk4(dyn,oper,state,h)
        [ [0.01381194+0.0j    0.0+0.11650741j]
          [0.0-0.11650741j    0.98618806+0.0j]   ]
        

    Args:
        func (función): Función a utilizar para obtener los k
        oper (numpy.ndarray): Matriz 2x2 que representa al operador
        state (numpy.ndarray): Matriz 2x2 que representa al estado del sistema
        h (numpy.float64): Variable con el valor del paso temporal

    Returns:
       result (numpy.ndarray): Retorna el valor del estado en el estado $y_{n+1}$ obtenido mediante el método Rk4  

    """

    k1 = h * func(oper, state)
    k2 = h * func(oper, state + 0.5 * k1)
    k3 = h * func(oper, state + 0.5 * k2)
    k4 = h * func(oper, state + k3)

    return state + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

