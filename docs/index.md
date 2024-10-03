# Bienvenido a la documentación del método RK4

Este documento se refiere a la información con respecto al cálculo de un sistema dinámico usando el método de Runge-Kutta de orden 4.


Los sistemas dinámicos son modelos que describen el movimiento o comportamiento de un sistema bajo ciertas condiciones. Este último usualmente representado de forma funcional.

En algunos casos, podemos modelar la dinámica de un estado genérico $y$ mediante la ecuación dinámica
\begin{equation}
\frac{dy}{dt} = f(t, y),
\end{equation}
sujeta a la condición inicial
\begin{equation}
y(t_0) = y_0.
\end{equation}

En este caso trabajo con un sistema de la forma $f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)]$. Con el detalle que la función $f(t, \mathbf{y})$ no depende explícitamente de la variable temporal.

Se utilizó el método de Runge-Kurtta de orden 4, para resolver este problema. La explicación de este método y del sistema se encuentran en Explicación y Referencias. 


El módulo se encuentra en:
[github.com](https://github.com/Esteban-Porras-UCR/Tarea2)
