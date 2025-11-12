.. Taller Electrostatica documentation master file.

Solución del Campo Electroestático 2D
======================================

Este proyecto resuelve la Ecuación de Laplace en 2D usando el Método de Diferencias Finitas (MDF).
La ecuación discretizada en un punto (i, j) es:

.. math::
   V_{i+1, j} + V_{i-1, j} + V_{i, j+1} + V_{i, j-1} - 4 V_{i, j} = 0

Se utiliza el método iterativo de Jacobi para encontrar la solución del potencial eléctrico V. A partir de V, se calcula el campo eléctrico E como:

.. math::
   \vec{E} = -\nabla V

Referencia de la API
--------------------

A continuación se detalla la API del módulo de cálculo.

.. automodule:: campo_estatico_mdf.solver
   :members:
   :undoc-members:
   :show-inheritance:

Índices y tablas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
