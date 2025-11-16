# Solución del Campo Electroestático 2D por Diferencias Finitas

<!-- 
================================================================================
IMPORTANTE: Reemplaza los siguientes valores con los tuyos:
- Reemplaza "Solver_campoelectrico_kevin" con el nombre final de tu paquete en PyPI.
- Reemplaza la URL de la app de Streamlit con el enlace que te dio Streamlit Cloud.
================================================================================
-->

[![PyPI version](https://img.shields.io/pypi/v/Solver_campoelectrico_kevin.svg)](https://pypi.org/project/Solver_campoelectrico_kevin/)
[![GitHub Actions Workflow Status](https://github.com/kacruzv011/Solver_DF_sphinx/actions/workflows/docs.yml/badge.svg)](https://github.com/kacruzv011/Solver_DF_sphinx/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este proyecto proporciona una solución numérica para la **Ecuación de Laplace en 2D** utilizando el Método de Diferencias Finitas (MDF). El software está desarrollado en Python y encapsulado en un paquete instalable, acompañado de una interfaz de usuario interactiva para la visualización y experimentación de resultados.

---

## 🚀 Demos en Vivo

*   **📖 Documentación Completa:** [**kacruzv011.github.io/Solver_DF_sphinx/**](https://kacruzv011.github.io/Solver_DF_sphinx/)
*   **🖥️ Aplicación Interactiva (Streamlit):** <!-- Reemplaza esta URL con el enlace de tu app en Streamlit Cloud --> [**Enlace a la App de Streamlit**](https://f8grfnh8fa38mv6rqwkgtg.streamlit.app/)

---

## ✨ Características Principales

*   ⚛️ **Solucionador Numérico Modular:** Implementa los métodos iterativos de **Jacobi** y **Gauss-Seidel** para resolver el sistema de ecuaciones lineales.
*   ⚡ **Cálculo del Campo Eléctrico:** Calcula el campo eléctrico (`E = -∇V`) a partir del potencial convergido usando `numpy.gradient`.
*   📈 **Visualización de Datos:** Genera mapas de calor (heatmaps) para el potencial y gráficos de vectores (quiver plots) para el campo eléctrico con `matplotlib`.
*   ✅ **Pruebas Unitarias:** Incluye un conjunto de pruebas con `pytest` para garantizar la correctitud del backend (caso trivial, convergencia y cálculo del campo).
*   🖥️ **Interfaz Gráfica Interactiva:** Una aplicación web construida con **Streamlit** que permite a los usuarios configurar y ejecutar simulaciones en tiempo real sin escribir código.
*   📚 **Documentación Profesional:** Documentación completa generada con **Sphinx**, incluyendo la teoría matemática, guías de uso y una referencia de la API autogenerada.
*   📦 **Paquete Distribuible:** El backend está empaquetado y publicado en **PyPI**, lo que permite su fácil instalación y reutilización en otros proyectos.

---

## 🖼️ Captura de Pantalla

<!-- 
Crea una captura de pantalla de tu aplicación de Streamlit mostrando los gráficos y reemplaza la siguiente línea.
Puedes subir la imagen a la raíz de tu repositorio de GitHub y enlazarla.
-->
![Captura de la App de Streamlit](<img width="1819" height="894" alt="image" src="https://github.com/user-attachments/assets/b23fb0b0-cb2f-435f-97c8-a4c59f56cd39" />
)

---

## 🛠️ Instalación

Puedes instalar el paquete directamente desde PyPI:

```bash
pip install Solver_campoelectrico_kevin
```
⚙️ Uso

El proyecto se puede utilizar de dos maneras: como una aplicación web interactiva o como una librería de Python en tus propios scripts.
1. Como Aplicación Web Interactiva

Para ejecutar la interfaz de usuario en tu máquina local:

    Clona el repositorio:
    code Bash

    
git clone https://github.com/kacruzv011/Solver_DF_sphinx.git
cd Solver_DF_sphinx

  

Instala las dependencias necesarias:
code Bash

    
pip install -e .[dev]

  

Ejecuta la aplicación:
code Bash

        
    streamlit run app.py

      

2. Como Librería de Python

Puedes importar LaplaceSolver2D en tus propios proyectos para realizar cálculos.
code Python

    
from campo_estatico_mdf.solver import LaplaceSolver2D
import numpy as np

# 1. Crear una instancia del solver para una malla de 50x50
solver = LaplaceSolver2D(N=50, V_left=10.0)

# 2. Resolver el sistema usando el método de Gauss-Seidel
iterations = solver.solve(method='gauss-seidel', tol=1e-5)
print(f"La simulación convergió en {iterations} iteraciones.")

# 3. Acceder al potencial V y calcular el campo eléctrico
potential_matrix = solver.V
Ex, Ey = solver.calculate_electric_field()

print("¡Cálculo completado!")

  

🧑‍💻 Desarrollo y Pruebas

Para contribuir al proyecto, sigue los pasos de instalación desde la fuente.

    Para ejecutar las pruebas unitarias:
    code Bash

    
pytest

  

Para construir la documentación localmente:
code Bash

        
    make -C docs html

      

    Luego, abre docs/build/html/index.html en tu navegador.

Solver_DF_sphinx/
├── .github/workflows/      # Automatización CI para documentación
├── docs/                   # Documentación Sphinx
├── src/
│   └── campo_estatico_mdf/ # Paquete instalable (backend)
│       └── solver.py
├── tests/                  # Pruebas unitarias
├── app.py                  # Interfaz Streamlit
├── pyproject.toml          # Configuración del paquete PyPI
└── requirements.txt        # Dependencias para la app


📄 Licencia

Este proyecto está bajo la Licencia MIT.

Autor: Kevin Andrés Cruz Velandia
