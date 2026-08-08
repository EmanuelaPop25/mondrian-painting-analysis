# Mondrian Painting Analysis

Este proyecto consiste en analizar un conjunto de datos sobre pinturas de Piet Mondrian utilizando Python.

El objetivo es calcular la complejidad de cada pintura a partir del número de elementos que contiene y comparar esos resultados con una pintura atribuida al año 1926 para comprobar si presenta diferencias respecto a las obras originales.

## Objetivos

- Cargar y explorar los datos.
- Calcular la complejidad de cada pintura.
- Crear gráficos para representar los resultados.
- Comparar la pintura fp26 con las obras de Mondrian.
- Obtener estadísticas básicas.

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Estructura del proyecto

data/
- fp26-features.csv
- mondrian-painting-features.csv
- mondrian-painting-info.csv

images/
- complexity_comparison.png
- Figure_1.png

notebooks/
- mondrian_painting_analysis.ipynb

src/
- mondrian_analysis.py

README.md

.gitignore

## Cómo ejecutar el proyecto

Clona el repositorio.

```bash
git clone https://github.com/TU-USUARIO/mondrian-painting-analysis.git
```

Entra en la carpeta.

```bash
cd mondrian-painting-analysis
```

Instala las dependencias.

```bash
pip install pandas matplotlib
```

Ejecuta el programa.

```bash
python src/mondrian_analysis.py
```

## Análisis realizado

Durante el proyecto se han realizado las siguientes tareas:

- Carga y exploración de los datos.
- Cálculo de la complejidad de cada pintura.
- Unión de los datos utilizando Pandas.
- Creación de gráficos.
- Comparación de la pintura fp26 con las pinturas originales.
- Obtención de estadísticas básicas.

## Resultados

La pintura fp26 presenta una complejidad superior a la media de las obras analizadas.

Este resultado no demuestra que la pintura sea falsa, pero sí indica que presenta un comportamiento diferente respecto a muchas pinturas del mismo periodo.

## Lo que he aprendido

Con este proyecto he seguido practicando el análisis de datos con Python.

He trabajado con Pandas para cargar y transformar datos, con Matplotlib para crear gráficos y con funciones para organizar mejor el código.

## Imágenes

images/Figure_1.png

images/complexity_comparison.png

---

Realizado por **Emanuela Pop**