#!/bin/bash

# upload_to_testpypi.sh
#
# Script para empaquetar y subir un proyecto Python a TestPyPI.
#
# INSTRUCCIONES:
# 1. Guarda este archivo como "upload_to_testpypi.sh" en la raíz de tu proyecto.
# 2. Reemplaza el valor de TEST_PYPI_API_TOKEN con tu token real.
# 3. Abre una terminal y dale permisos de ejecución al script con:
#    chmod +x upload_to_testpypi.sh
# 4. Ejecuta el script desde la raíz de tu proyecto con:
#    ./upload_to_testpypi.sh
#

# --- CONFIGURACIÓN ---
# Pega aquí tu token de API de TestPyPI. Asegúrate de que comience con "pypi-"
TEST_PYPI_API_TOKEN="pega-aqui-tu-token-de-test-pypi"

# --- INICIO DEL SCRIPT ---

# Colores para la salida
GREEN='\033[0;32m'
NC='\033[0m' # Sin color

echo -e "${GREEN}Paso 1: Instalando/actualizando herramientas de empaquetado...${NC}"
python3 -m pip install --upgrade setuptools wheel twine

# Verifica si la instalación fue exitosa
if [ $? -ne 0 ]; then
    echo "Error: Falló la instalación de las herramientas de empaquetado."
    exit 1
fi

echo -e "${GREEN}Paso 2: Limpiando compilaciones anteriores...${NC}"
rm -rf dist/ build/ *.egg-info

echo -e "${GREEN}Paso 3: Creando los paquetes de distribución (sdist y wheel)...${NC}"
python3 setup.py sdist bdist_wheel

# Verifica si la creación de paquetes fue exitosa
if [ $? -ne 0 ]; then
    echo "Error: Falló la creación de los paquetes de distribución."
    exit 1
fi

echo -e "${GREEN}Paso 4: Subiendo los paquetes a TestPyPI...${NC}"
python3 -m twine upload --repository testpypi dist/* --username __token__ --password $TEST_PYPI_API_TOKEN

# Verifica si la subida fue exitosa
if [ $? -ne 0 ]; then
    echo "Error: Falló la subida a TestPyPI. Verifica tu token y la versión del paquete."
    exit 1
fi

echo -e "${GREEN}¡Éxito! El proyecto ha sido subido a TestPyPI.${NC}"
echo "Puedes verificarlo en: https://test.pypi.org/project/$(python3 setup.py --name)/"