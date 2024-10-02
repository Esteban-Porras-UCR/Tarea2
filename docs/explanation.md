#Explicación

En esta notación, $y$ corresponde a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal. En la ecuación anterior, $t$ corresponde a la variable temporal.

Las ecuaciones del método numérico que vamos a utilizar son:

\begin{equation}
y_{n+1} = \rightarrow y_n \frac{1}{6}(k_1 + k_2 + k_3 + k_4)
\end{equation}

\begin{equation}
k_1 = hf(t,y)
\end{equation}

\begin{equation}
k_2 = hf( t + \frac{h}{2}, y + \frac{k_1}{2})
\end{equation}

\begin{equation}
k_3 = hf( t + \frac{h}{2}, y + \frac{k_2}{2})
\end{equation}

\begin{equation}
k_4 = hf(t + h, y +k_3)
\end{equation}


Armados con esta metodología vamos a estudiar la solución de un problema dinámico genérico.

Asumamos que queremos estudiar la evolución temporal de un estado $\mathbf{y}(t)$. Este estado será representado mediante una matriz 2x2 que corresponde a algún operador lineal. La función que genra la dinámica del problema es
$$
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
$$
donde $\mathbf{O}$ es otro operador lineal, ${\rm{i}}$ es la constante compleja y $[A, B] = AB - BA$ es un operación de conmutación. Note que **la función $f(t, \mathbf{y})$ no depende explícitamente de la variable temporal**.
