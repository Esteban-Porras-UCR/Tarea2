def dyn_generator(oper, state):

    """Nose

    Examples:
        >>> rk4(a,b,c,d)
        7.0

    Args:
        oper (float): First argument

    Returns:
        nose: retorna algo

    """

    return (-1.0 * 1.0j) * (np.dot(oper,state) - np.dot(state,oper))
