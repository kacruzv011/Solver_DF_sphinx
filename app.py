import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from campo_estatico_mdf.solver import LaplaceSolver2D

st.set_page_config(layout="wide")

st.title("Taller: Solución del Campo Electroestático 2D por Diferencias Finitas")
st.markdown("Visualizador interactivo para la Ecuación de Laplace en una región cuadrada.")

# --- Barra lateral para los inputs ---
st.sidebar.header("Parámetros de Simulación")

# ¡NUEVO WIDGET PARA SELECCIONAR EL MÉTODO!
method = st.sidebar.selectbox(
    "Método de Resolución",
    ("Jacobi", "Gauss-Seidel")
)

N = st.sidebar.slider("Tamaño de la malla (N x N)", min_value=10, max_value=100, value=50, step=5)
tol = st.sidebar.select_slider(
    "Tolerancia de convergencia (ε)",
    options=[1e-2, 1e-3, 1e-4, 1e-5, 1e-6],
    value=1e-4,
    format_func=lambda x: f"{x:.0e}"
)

st.sidebar.subheader("Condiciones de Contorno (Voltaje)")
V_top = st.sidebar.number_input("Voltaje Superior (V_top)", value=0.0)
V_bottom = st.sidebar.number_input("Voltaje Inferior (V_bottom)", value=0.0)
V_left = st.sidebar.number_input("Voltaje Izquierdo (V_left)", value=10.0)
V_right = st.sidebar.number_input("Voltaje Derecho (V_right)", value=0.0)

# --- Botón para ejecutar la simulación ---
if st.sidebar.button("Resolver y Visualizar", type="primary"):
    
    with st.spinner(f"Calculando con el método {method} para una malla de {N}x{N}..."):
        # 1. Crear y resolver el sistema
        solver = LaplaceSolver2D(N, V_top, V_bottom, V_left, V_right)
        
        # ¡USAMOS EL NUEVO MÉTODO 'SOLVE' Y LE PASAMOS LA ELECCIÓN DEL USUARIO!
        iterations = solver.solve(method=method.lower(), tol=tol)
        
        # 2. Calcular el campo eléctrico
        Ex, Ey = solver.calculate_electric_field()

    st.success(f"¡Cálculo completado con {method}! Convergencia alcanzada en **{iterations}** iteraciones.")
    
    # --- Visualización de resultados (sin cambios aquí) ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Mapa de Potencial Eléctrico (V)")
        fig_v, ax_v = plt.subplots(figsize=(8, 8))
        im = ax_v.imshow(solver.V, cmap='viridis', origin='lower')
        fig_v.colorbar(im, ax=ax_v, label="Potencial (V)")
        ax_v.set_title(f"Distribución de Potencial V(x, y)")
        ax_v.set_xlabel("x")
        ax_v.set_ylabel("y")
        st.pyplot(fig_v)
        
    with col2:
        st.header("Campo Eléctrico (E)")
        fig_e, ax_e = plt.subplots(figsize=(8, 8))
        
        skip = max(1, N // 20)
        y, x = np.mgrid[0:N:skip, 0:N:skip]
        Ex_skip = Ex[y, x]
        Ey_skip = Ey[y, x]
        
        magnitude = np.sqrt(Ex_skip**2 + Ey_skip**2)
        
        ax_e.quiver(x, y, Ex_skip, Ey_skip, magnitude, cmap='autumn')
        ax_e.set_title("Vectores del Campo Eléctrico E(x, y)")
        ax_e.set_xlabel("x")
        ax_e.set_ylabel("y")
        ax_e.set_aspect('equal', adjustable='box')
        ax_e.set_xlim(-1, N)
        ax_e.set_ylim(-1, N)
        st.pyplot(fig_e)

else:
    st.info("Ajusta los parámetros en la barra lateral y haz clic en 'Resolver y Visualizar' para comenzar.")