Uso Básico
==========

El siguiente ejemplo muestra cómo importar el solver, configurar una simulación, elegir un método y resolver el sistema.

.. code-block:: python

   from campo_estatico_mdf.solver import LaplaceSolver2D
   import numpy as np

   # 1. Crear una instancia del solver para una malla de 50x50
   #    con la frontera izquierda a 10V y las demás a 0V.
   solver = LaplaceSolver2D(N=50, V_left=10.0)

   # 2. Resolver el sistema usando el método de Gauss-Seidel
   iterations = solver.solve(method='gauss-seidel', tol=1e-5)
   print(f"La simulación convergió en {iterations} iteraciones.")

   # 3. El potencial V está disponible en el atributo solver.V
   print("Matriz de potencial V:")
   print(solver.V)

   # 4. Calcular el campo eléctrico
   Ex, Ey = solver.calculate_electric_field()
   print("Componente Ex del campo eléctrico:")
   print(Ex)
