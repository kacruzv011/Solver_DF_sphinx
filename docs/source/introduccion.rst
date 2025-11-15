Introducción
============

Este proyecto presenta una solución numérica para la Ecuación de Laplace en dos dimensiones utilizando el Método de Diferencias Finitas (MDF).

El software está implementado en Python y se estructura como un paquete instalable con una clara separación entre el motor de cálculo (backend) y la interfaz de usuario (frontend).

El proyecto implementa:

- Un solucionador numérico modular: :class:`~campo_estatico_mdf.solver.LaplaceSolver2D`
- Cálculo del campo eléctrico: :math:`\vec{E} = -\nabla V`
- Rutinas de visualización con `matplotlib`
- Conjunto completo de pruebas con `pytest`
- Interfaz gráfica interactiva vía `Streamlit`
- Documentación generada con `Sphinx`