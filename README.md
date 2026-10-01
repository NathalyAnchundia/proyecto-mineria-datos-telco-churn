# Proyecto de Minería de Datos: Predicción de Churn en Clientes de Telecomunicaciones

## 1. Descripción del proyecto

Este proyecto tiene como finalidad analizar el comportamiento de los clientes de una empresa de telecomunicaciones y desarrollar modelos de minería de datos capaces de predecir la probabilidad de abandono del servicio, conocido como *Customer Churn*.

Para el análisis se utilizó el conjunto de datos **Telco Customer Churn**, que contiene información relacionada con las características de los clientes, los servicios contratados, el tiempo de permanencia y los cargos realizados.

El proyecto comprende las etapas de exploración, limpieza, transformación, ingeniería de características, modelado y evaluación de resultados.

## 2. Problema

Las empresas de telecomunicaciones necesitan identificar a los clientes que presentan mayor probabilidad de abandonar sus servicios. La pérdida de clientes puede afectar los ingresos y dificultar la planificación de estrategias de retención.

Mediante técnicas de minería de datos se busca analizar los patrones existentes en los datos históricos y construir modelos de clasificación que permitan identificar los casos asociados al abandono de clientes.

## 3. Objetivos

### Objetivo general

Analizar los datos de clientes de una empresa de telecomunicaciones mediante técnicas de minería de datos para identificar patrones asociados al abandono del servicio y evaluar modelos de clasificación para su predicción.

### Objetivos específicos

* Explorar y caracterizar las variables del conjunto de datos para identificar patrones relacionados con el abandono de clientes.
* Preprocesar los datos mediante técnicas de limpieza, codificación, normalización e ingeniería de características.
* Implementar y evaluar diferentes modelos de clasificación para identificar su comportamiento en la predicción del abandono de clientes.

## 4. Dataset

El conjunto de datos utilizado es **Telco Customer Churn**.

Características principales:

* Registros originales: aproximadamente 7043 clientes.
* Registros utilizados después del tratamiento de valores faltantes: 7032.
* Variable objetivo: `Churn`.
* Tipo de problema: clasificación binaria.
* Clases:

  * `0`: cliente que no abandona.
  * `1`: cliente que abandona.

La fuente del dataset corresponde a IBM Sample Data Sets. El conjunto de datos se encuentra disponible en Kaggle como "Telco Customer Churn":

https://www.kaggle.com/blastchar/telco-customer-churn
## 5. Preprocesamiento

Durante el proyecto se realizaron las siguientes actividades:

1. Identificación y tratamiento de valores faltantes.
2. Revisión de registros duplicados.
3. Análisis de valores atípicos mediante el rango intercuartílico (IQR).
4. Eliminación de la variable identificadora `customerID`.
5. Conversión de la variable `Churn` a valores binarios.
6. Codificación de variables categóricas mediante One-Hot Encoding.
7. Creación de variables derivadas.
8. Normalización de variables numéricas mediante `StandardScaler`.
9. División de los datos en entrenamiento y prueba.

## 6. Variables derivadas

Se generaron dos variables mediante ingeniería de características:

* `AverageMonthlyCharge`: representa el cargo mensual promedio calculado a partir de los cargos totales y el tiempo de permanencia.
* `TotalServices`: representa la cantidad de servicios contratados por cada cliente.

## 7. Modelos utilizados

Se implementaron tres técnicas de clasificación:

### Regresión Logística

Parámetro principal:

* `max_iter = 1000`
* `random_state = 42`

### Árbol de Decisión

Parámetros principales:

* `max_depth = 5`
* `random_state = 42`

### Random Forest

Parámetros principales:

* `n_estimators = 100`
* `max_depth = 10`
* `random_state = 42`

## 8. División de datos

El conjunto de datos se dividió utilizando:

* 80 % para entrenamiento.
* 20 % para prueba.
* `random_state = 42`.
* `stratify = y`.

Resultados:

* Entrenamiento: 5625 registros.
* Prueba: 1407 registros.

## 9. Evaluación

Se utilizaron las siguientes métricas:

* Accuracy
* Precision
* Recall
* F1-Score

Además, se aplicó validación cruzada de **5 particiones (5-fold cross-validation)** utilizando F1-Score.

### Resultados

| Modelo              | Accuracy | Precision | Recall | F1-Score | CV F1-Score |
| ------------------- | -------: | --------: | -----: | -------: | ----------: |
| Regresión Logística |   0.8045 |    0.6514 | 0.5695 |   0.6077 |      0.5957 |
| Árbol de Decisión   |   0.7775 |    0.5818 | 0.5802 |   0.5810 |      0.5538 |
| Random Forest       |   0.7903 |    0.6376 | 0.4893 |   0.5537 |      0.5658 |

## 10. Matrices de confusión

También se calcularon las matrices de confusión para cada modelo con el propósito de analizar los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos.

## 11. Estructura del proyecto

proyecto-mineria-datos-telco-churn/
│
├── proyecto_mineria_datos.ipynb
├── Telco-Customer-Churn.csv
└── README.md

## 12. Ejecución

El análisis fue desarrollado en Python utilizando un entorno de Jupyter Notebook/Google Colab.

Las principales bibliotecas utilizadas fueron:

* pandas
* numpy
* matplotlib
* scikit-learn

## 13. Resultados

Los modelos presentaron diferentes comportamientos en las métricas de evaluación. La comparación entre los resultados obtenidos en el conjunto de prueba y la validación cruzada permitió analizar la consistencia del desempeño de cada técnica.

El análisis completo, incluyendo el código, procesamiento, visualizaciones, entrenamiento y evaluación de los modelos, se encuentra disponible en el notebook incluido en este repositorio.

## 14. Autor

**Nathaly Anchundia**

Proyecto académico de Minería de Datos.
2026.
