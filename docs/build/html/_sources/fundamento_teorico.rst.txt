Fundamento Teórico
==================

Ecuación de Laplace
-------------------

La Ecuación de Laplace describe el potencial eléctrico :math:`V` en una región del espacio libre de cargas. En dos dimensiones cartesianas, la ecuación es:

.. math::
   \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = 0

Método de Diferencias Finitas (MDF)
-----------------------------------

Para resolver esta ecuación numéricamente, discretizamos el dominio en una cuadrícula de puntos con espaciado :math:`h`. La segunda derivada se puede aproximar mediante diferencias centrales, lo que transforma la ecuación diferencial en una ecuación algebraica en cada punto interior :math:`(i, j)`:

.. math::
   V_{i+1, j} + V_{i-1, j} + V_{i, j+1} + V_{i, j-1} - 4 V_{i, j} = 0

Esta ecuación establece que el potencial en un punto es el promedio del potencial de sus cuatro vecinos más cercanos. Este sistema de ecuaciones lineales se resuelve iterativamente usando el método de Jacobi.