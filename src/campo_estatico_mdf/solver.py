import numpy as np

class LaplaceSolver2D:
    """
    Resuelve la Ecuación de Laplace en 2D en una región cuadrada
    utilizando el Método de Diferencias Finitas (MDF) con algoritmos
    iterativos de Jacobi o Gauss-Seidel.
    """

    def __init__(self, N, V_top=0.0, V_bottom=0.0, V_left=0.0, V_right=0.0):
        """
        Inicializa el solver con las dimensiones de la malla y las condiciones de contorno.
        """
        if N < 3:
            raise ValueError("N debe ser al menos 3 para tener puntos interiores.")
        self.N = N
        self.V = np.zeros((N, N))

        self.V[0, :] = V_top
        self.V[-1, :] = V_bottom
        self.V[:, 0] = V_left
        self.V[:, -1] = V_right

    def solve(self, method='jacobi', tol=1e-5, max_iter=20000):
        """
        Método principal para resolver la Ecuación de Laplace.
        Permite seleccionar entre el método de Jacobi y Gauss-Seidel.

        Args:
            method (str): El método a utilizar ('jacobi' or 'gauss-seidel').
            tol (float): Criterio de convergencia.
            max_iter (int): Límite de iteraciones.

        Returns:
            int: Número de iteraciones realizadas.
        """
        if method.lower() == 'jacobi':
            return self._solve_jacobi(tol, max_iter)
        elif method.lower() == 'gauss-seidel':
            return self._solve_gauss_seidel(tol, max_iter)
        else:
            raise ValueError("Método no válido. Elija 'jacobi' o 'gauss-seidel'.")

    def _solve_jacobi(self, tol, max_iter):
        """Resuelve usando el método de Jacobi."""
        V_old = self.V.copy()
        for i in range(max_iter):
            self.V[1:-1, 1:-1] = 0.25 * (V_old[2:, 1:-1] + V_old[:-2, 1:-1] +
                                        V_old[1:-1, 2:] + V_old[1:-1, :-2])
            
            diff = np.max(np.abs(self.V - V_old))
            if diff < tol:
                return i + 1
            
            V_old = self.V.copy()
        
        return max_iter

    def _solve_gauss_seidel(self, tol, max_iter):
        """Resuelve usando el método de Gauss-Seidel."""
        for i in range(max_iter):
            V_old = self.V.copy()  # Copia para la comprobación de convergencia

            # Itera sobre los puntos interiores, actualizando V "in-place"
            for row in range(1, self.N - 1):
                for col in range(1, self.N - 1):
                    self.V[row, col] = 0.25 * (self.V[row+1, col] + self.V[row-1, col] +
                                              self.V[row, col+1] + self.V[row, col-1])
            
            diff = np.max(np.abs(self.V - V_old))
            if diff < tol:
                return i + 1
        
        return max_iter

    def calculate_electric_field(self):
        """Calcula el campo eléctrico E = -grad(V)."""
        Ey, Ex = np.gradient(-self.V)
        return Ex, Ey