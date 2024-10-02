def dyn_generator(oper, state):

    """Se hace la conmutación de oper y state, ambos siendo operadores lineales,y se multiplica por i. Esta es la ecuación que determina el estado del sistema.

    Examples:
        >>> oper = np.array([0,1],[1,0])
        >>> state = np.array([1,0],[0,0])
        >>> rk4(oper,state)
        [ [0.76703615-0.0j  0.0+0.64131106j]
          [0.0-0.64131106j -0.76703615+0.0j] ]

    Args:
        oper (numpy.ndarray): Matriz 2x2 que representa al operador
        state (numpy.ndarray): Matriz 2x2 que representa el estado del sistema

    Returns:
        Resultado (numpy.ndarray): Retorna el resultado de $f(t, \mathbf{y}) = -i[\mathbf{O}, \mathbf{y}(t)]$

    """

    return (-1.0 * 1.0j) * (np.dot(oper,state) - np.dot(state,oper))
