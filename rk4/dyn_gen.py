def dyn_generator(oper, state):

    """Se hace la conmutación de oper y state, ambos siendo operadores lineales,y se multiplica por i. Esta es la ecuación que determina el estado del sistema.

    Examples:
        >>> rk4(a,b)
        7.0

    Args:
        oper (numpy.ndarray): First argument
        state (numpy.ndarray): Second argument

    Returns:
        Resultado (numpy.ndarray): retorna el resultado del cálculo realizado

    """

    return (-1.0 * 1.0j) * (np.dot(oper,state) - np.dot(state,oper))
