# Proyecto 2 — Análisis detallado, guía y recomendaciones (formato listo para Notion)

> **Archivo fuente:** `./ICC - Proyecto Final 2.pdf`.

---

## 1. Resumen ejecutivo (¿de qué trata el proyecto?)

Implementar un **sistema de visión artificial** en Python que detecte y clasifique dígitos escritos a mano usando el dataset `digits` de `scikit-learn`. El proyecto combina procesamiento de imágenes (preprocesamiento de fotos manuscritas), cálculo de **distancias euclidianas** frente a las instancias del dataset, y una regla simple de clasificación basada en los **3 vecinos más parecidos.**

---

## 2. Objetivo del Proyecto 2

* **Objetivo principal:** Detectar y clasificar un dígito escrito a mano por el estudiante comparándolo con los 1796 (como indica el enunciado) ejemplos del dataset `datasets.load_digits()` usando distancia euclidiana y un procedimiento de 3 vecinos más parecidos. cite

---

## 3. Instrucciones oficiales (extracto y explicación)

### Requisitos obligatorios (pasos a realizar)

1. **Recolectar imágenes manuscritas**: escribir (a lapicero) números del tamaño de un DNI o de un código de alumno; tomarles foto o escanearlas.
2. **Recortar cada imagen** de modo que:

   * el número esté tocando (chocando) con los límites superior e inferior,
   * la imagen sea cuadrada,
   * evitar grandes bordes blancos (ejemplo provisto en el PDF). cite
3. **Preprocesamiento**: convertir a blanco y negro, reducir a **8×8 píxeles**, invertir la escala, y escalar los valores a un rango de **0 a 16**. Tras esto, su imagen estará en la misma “escala” que las imágenes del dataset. Para cada imagen nueva, **calcular las distancias euclidianas** frente a las 1796 imágenes del dataset. cite
4. **Encontrar los 3 vecinos más parecidos** (las 3 menores distancias) para cada imagen nueva. Imprimir los targets de esos 3 vecinos y la etiqueta real del número nuevo. cite
5. **Regla de clasificación mínima**:

   * Si **2 de los 3 targets** o **los 3** coinciden en un mismo valor `X`, declarar que el dígito nuevo **corresponde a `X`** e imprimir la frase solicitada:
     `“Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número X”`. cite
   * Si los **3 targets son diferentes**, el alumno **decide e implementa** un criterio de clasificación (se permite cualquier método que justifique). cite
6. **Matrices de confusión**:

   * Imprimir **una matriz de confusión de 10 clases** (0–9) y analizarla (no obligatorio calcular métricas de desempeño aquí). cite
   * Para **cada grupo de imágenes del mismo dígito** (por ejemplo: sus 10 ceros, sus 8 unos, etc.) imprimir una **matriz de confusión de 2 clases** y **sí** calcular métricas (precisión) para la binaria. Es obligatorio calcular métricas para estas matrices de 2 clases. cite

---

## 4. Entregables (qué se debe entregar y cómo)

1. **ZIP con el proyecto Python**: incluir todos los archivos fuente, datos generados/usados (las imágenes recortadas del alumno, si es posible), notebooks (si los hay), `requirements.txt` y scripts de ejecución. cite
2. **Informe en PDF**:

   * Debe describir los pasos realizados y demostrar que se cumplieron todos los puntos solicitados.
   * Contenido mínimo esperado: Antecedentes, Fundamento teórico, Métodos y Desarrollo, Resultados y Conclusiones. cite
   * En la carátula: nombres y códigos de los integrantes y porcentaje de participación de cada integrante. Segunda hoja: detalle de actividades realizadas por cada integrante. cite
   * **Conclusiones**: 4 conclusiones escritas por los estudiantes y **4 conclusiones generadas por un asistente de IA** (p. ej. ChatGPT). Después de la conclusión 2 de los humanos, **antes** de las conclusiones 3 y 4, deben escribir “una frase típica que su docente dice en clases” (como comprobante de lectura). Luego se deben comparar recursos usados por la IA vs. los omitidos por el grupo. cite
3. **Presentación oral**: todos los miembros deben conocer completamente el código y el informe; si un miembro no comprende el código, se considerará que no participó y podría recibir 0 puntos.

---

## 5. Reglas, restricciones y criterios de evaluación (rúbrica)

* **Desarrollo de software (10 pts)**: Se espera software ordenado, claro y óptimo para solucionar el problema. Hay niveles: Excelente (10), Adecuado (6), Mínimo (4), Insuficiente (2).
* **Presentación escrita (5 pts)**: Informe con secciones indicadas y conclusiones bien formuladas.
* **Presentación oral (5 pts)**: Calidad de la exposición y capacidad de responder preguntas lógicamente.
* **Importante**: la falta de conocimiento del código por parte de un miembro se sanciona con 0 para ese integrante en la evaluación práctica.

---

## 6. Requisitos técnicos y funcionales (detallado)

### Técnicos (software / librerías mínimas recomendadas)

* Python 3.8+
* `scikit-learn` (`datasets`, `metrics`)
* `numpy`, `scipy` (opcional), `matplotlib` para visualizaciones
* `Pillow` (PIL) o `opencv-python` para cargar y procesar imágenes
* `joblib` o `pickle` para guardar resultados (opcional)
* `jupyter` o `notebook` (opcional) para entregables interactivos

### Funcionales (qué debe hacer el programa)

1. **Cargar dataset**: `datasets.load_digits()` (1796/1797 instancias según el enunciado).
2. **Leer imágenes nuevas** (fotos/escaneos) y aplicar preprocesamiento: escala a B/N, resize a 8×8, invertir escala, mapear valores al rango 0–16 (igual que el dataset).
3. **Comparar**: Para cada nueva imagen, calcular distancias euclidianas frente a cada imagen del dataset → 1796 distancias.
4. **Encontrar 3 menores distancias** (los 3 vecinos). Imprimir sus `targets` y la etiqueta real.
5. **Clasificar** con la regla dada (2/3 o 3/3) y manejar el caso “3 diferentes” con un método razonado.
6. **Generar matrices de confusión**:

   * 10 clases: imprimir y comentar (no obligatorio métricas).
   * Para cada dígito presente en sus dibujos: matriz binaria (2 clases) con cálculo obligatorio de métricas (precisión requerida).
7. **Entregables automatizados**: scripts que generen figuras y archivos necesarios para el informe (tablas, gráficos de vecinos, matrices en PNG, CSV de resultados, etc.)

---

## 7. Guía práctica y camino de pasos (orden lógico, lista numerada—lista para seguir sin tiempos)

> Sigue estos pasos secuencialesmente. Cada paso incluye acciones concretas y artefactos que producir.

1. **Lectura y planificación**

   * Leer el PDF completo (comprobado).
   * Definir integrantes y roles (quién hace preprocesamiento, análisis, informe, presentación). Registrar en la segunda hoja del informe.
2. **Preparar entorno**

   * Crear `venv` o `conda` env; instalar dependencias (`requirements.txt`).
   * Estructura de carpetas recomendada:

     ```
     proyecto-proyecto2/
     ├─ data/
     │  ├─ raw_images/        # fotos originales
     │  └─ processed_images/  # imágenes 8x8 normalizadas
     ├─ src/
     │  ├─ preprocess.py
     │  ├─ classify.py
     │  ├─ metrics_utils.py
     │  └─ run_all.py
     ├─ notebooks/
     ├─ results/
     ├─ report/
     └─ requirements.txt
     ```
3. **Recolectar y preparar imágenes manuscritas**

   * Escribir los dígitos en papel, tomar fotos o escanear.
   * Poner los archivos en `data/raw_images/`.
4. **Implementar `preprocess.py`**

   * Funciones:

     * `load_image(path)` → leer (PIL/OpenCV).
     * `crop_to_digit(img)` → recorte ajustado (hacer automático con detección de contorno o interacción manual).
     * `make_square(img)` → recortar/añadir padding para cuadrado.
     * `to_grayscale(img)` → B/N.
     * `resize_8x8(img)` → redimensionar a 8×8.
     * `invert_and_scale(img)` → invertir colores y mapear [0..255] → [0..16] (int).
   * Guardar cada resultado en `data/processed_images/` y generar un CSV con nombre de archivo y etiqueta real (si se conoce).
5. **Cargar dataset y calcular distancias (`classify.py`)**

   * Cargar `digits = datasets.load_digits()` (los `data` y `target`).
   * Para cada imagen procesada:

     * Aplanar la matriz 8×8 a vector 64.
     * Calcular distancias euclidianas a todas las instancias del dataset: `np.linalg.norm(dataset_vectors - image_vector, axis=1)`.
     * Ordenar distancias y obtener índices de los 3 más pequeños (vecinos).
     * Extraer los `targets` de esos vecinos y el `target` real (si el alumno lo escribió).
     * Aplicar la regla de clasificación (2 de 3 igual → ese valor). Si 3 distintos → aplicar desempate por vecinos (ej.: elegir el target del vecino más cercano) o usar **voto ponderado por 1/d** o entrenar un clasificador simple (SVM / KNN) y justificarlo.
   * **Imprimir** en consola o guardar en CSV los resultados con campos: `filename, true_label, neigh1_label, neigh2_label, neigh3_label, predicted_label, neighbor_distances`.
6. **Generar matrices de confusión y métricas (`metrics_utils.py`)**

   * **Matriz 10 clases**: `confusion_matrix(y_true_all, y_pred_all)` y mostrar imagen/tabla. (No obligatorio calcular métricas, pero recomendable).
   * **Matrices binarias**: Para cada dígito `d` presente en sus dibujos, construir etiquetas binarias `is_d / not_d` y calcular `confusion_matrix`, `precision`, `recall`, `f1`. Guardarlas en `results/` y exportar tabla con métricas. **Obligatorio** calcular precisión para cada binaria.
7. **Informe en PDF**

   * Secciones mínimas: Portada, Resumen ejecutivo, Antecedentes, Fundamento teórico (knn, distancia euclidiana, preprocesamiento, matrices de confusión), Métodos y Desarrollo (detallar cada paso y código), Resultados (tablas, gráficos, matrices), Análisis, Conclusiones (4 humanas + 4 IA), Bibliografía y anexos (código relevante o enlace al ZIP).
   * Incluir en la carátula: nombres y códigos y % de participación. Segunda hoja: detalle de actividades por integrante.
   * Insertar la frase típica del docente **después de la conclusión 2** y antes de conclusiones 3 y 4 (como exige el enunciado).
8. **Preparar la presentación oral**

   * Cada integrante debe dominar una parte (preprocesamiento, clasificación, métricas, informe). Practicar preguntas típicas (por qué 8×8, por qué 0–16, por qué euclidiana, manejo de casos de empate).
9. **Empaquetar y entregar**

   * Crear ZIP con toda la estructura (`src/`, `data/processed_images/`, `results/`, `report/report.pdf`, `requirements.txt`).
   * Verificar que el ZIP incluya archivos generados/usarados tal como pide el enunciado.

---

## 8. Criterios técnicos para "casos especiales" y decisiones a tomar

* **Caso “3 vecinos diferentes”**: opciones válidas (justificar en informe):

  * **Desempate por vecino más cercano** (predicción = label del vecino con menor distancia). *Sencillo y justificado*.
  * **Voto ponderado por distancia**: cada vecino vota con peso `1/d` (o `1/(d+ε)`), sumar pesos por label, escoger mayor. *Más robusto*.
  * **Entrenar un clasificador** (KNN con k=3, SVM, RandomForest) usando `digits` como train y evaluar cómo clasifica la imagen; justificar por comparativa. *Aporta valor si bien explicado*.
* **Rango 0–16**: asegurarse de replicar exactamente el mapeo del dataset `digits` (específico del dataset de sklearn).
* **Número de instancias en dataset**: el PDF menciona `1796` distancias por imagen. Use exactamente la cifra indicada en el enunciado y coméntelo en el informe (el dataset clásico tiene 1797, verificar y comentar cualquier discrepancia en el informe).

---

## 9. Ejemplos (pseudocódigo y fragmentos útiles)

### Pseudocódigo — cálculo de vecinos y predicción

```python
# cargar dataset
digits = load_digits()
X_dataset = digits.data      # shape (n_samples, 64)
y_dataset = digits.target

# para cada imagen procesada
img_vec = imagen_8x8.flatten()   # vector (64,)

# distancias euclidianas
dists = np.linalg.norm(X_dataset - img_vec, axis=1)

# indices de 3 vecinos más cercanos
idx = np.argsort(dists)[:3]
neighbors = y_dataset[idx]       # etiquetas de los 3 vecinos
neighbor_dists = dists[idx]

# regla básica
if neighbors[0] == neighbors[1] or neighbors[0] == neighbors[2]:
    pred = neighbors[0]  # caso de 2 iguales (o 3 iguales)
elif neighbors[1] == neighbors[2]:
    pred = neighbors[1]
else:
    # desempate: elegir label del vecino más cercano
    pred = neighbors[0]

print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {pred}")
```

### Cómo calcular matriz de confusión (10 clases) en sklearn

```python
from sklearn.metrics import confusion_matrix, precision_score, classification_report

cm = confusion_matrix(y_true, y_pred)  # 10x10
# Para binaria (por cada dígito d)
binary_true = [1 if y==d else 0 for y in y_true_subset]
binary_pred = [1 if y==d else 0 for y in y_pred_subset]
cm_bin = confusion_matrix(binary_true, binary_pred)
precision = precision_score(binary_true, binary_pred)
```

---

## 10. Mejoras, ideas y extensiones para destacar (innovación para superar expectativas)

* **Visualización interactiva**: Jupyter Notebook con widgets para cargar una imagen y ver sus 3 vecinos con sus distancias (ideal para la presentación).
* **Interfaz simple (GUI)**: pequeña app con `tkinter` o `streamlit` para cargar foto y mostrar la predicción y vecinos. Muy llamativo en demo.
* **Voto ponderado y benchmarks**: comparar la regla solicitada con un `KNeighborsClassifier` entrenado en el `digits` dataset y presentar resultados comparativos (tablas).
* **Detección de “No pertenece a 0–9”**: definir umbral de distancia máxima; si la imagen está muy lejos de todas las instancias, marcar como “No confident / desconocido”.
* **Aumento de datos (data augmentation)**: rotaciones pequeñas, escalado y ruido sobre las imágenes procesadas para probar robustez (aunque en el enunciado la entrada son fotos manuales y no se requiere entrenar).
* **Informe reproducible**: `Makefile` o `run_all.py` que genere todos los resultados automáticamente (gráficos, matrices, report.pdf).
* **Pruebas automáticas**: tests unitarios (pytest) para las funciones de preprocesamiento y la función que devuelve vecinos.
* **Documentar las decisiones**: anotar por qué se eligió desempate, cómo se mapeó 0–255 → 0–16, etc. Esto mejora notablemente la evaluación escrita.

---

## 11. Ejemplos de contenidos que incluir en el informe (plantilla corta)

* **Portada**: título, curso, profesor, integrantes, códigos, % participación.
* **Resumen**
* **Introducción / Antecedentes**
* **Fundamento teórico**: k-NN, distancia euclidiana, matriz de confusión (10 y 2 clases)
* **Metodología**: preprocesamiento paso a paso con pseudocódigo
* **Resultados**: tablas, gráficos, archivos generados (ej.: `results/summary.csv`)
* **Análisis**: interpretar matriz 10x10 y matrices binarias; comentar precisión en binarias (obligatorio)
* **Conclusiones**: 4 humanas + 4 generadas por IA; después de la conclusión 2 humana, **insertar frase típica del docente**.
* **Anexos**: fragmentos de código, screenshots, imágenes de los vecinos, ZIP con el proyecto.

---

## 12. Riesgos, vacíos y recomendaciones finales

### Riesgos / vacíos

* **Inconsistencia en recortes**: fotos con mucho borde blanco o mal recortadas invalidan la comparación. *Recomendación:* estandarizar recorte mediante detección automática de contornos o instruir a los compañeros cómo fotografiar.
* **Iluminación y contraste**: fotos poco contrastadas pueden producir valores erróneos al mapear 0–16. *Recomendación:* aplicar contraste adaptativo y/o normalización.
* **Discrepancia en tamaño del dataset**: el PDF menciona 1796 (verificar que `load_digits()` devuelve 1797 en su versión particular). Documentar y justificar en el informe.
* **Miembros desconociendo código**: riesgo de sanción (0 pts para no participantes). Asegurarse de que todo integrante entienda su parte.

### Recomendaciones

* Documentar cada decisión técnica en el informe (por ejemplo: cómo se hace el mapeo 0–16).
* Añadir una sección **“Limitaciones y trabajo futuro”** en el informe donde se explique posibles mejoras.
* Incluir scripts reproducibles para facilitar la revisión del docente (esto aumenta la nota en “Desarrollo de software”).

---

## 13. Checklist de entrega (para pegar y revisar antes de subir)

* [ ] `project.zip` contiene `src/`, `data/processed_images/`, `results/`, `report/report.pdf`, `requirements.txt`.
* [ ] `report.pdf` con portada, segunda hoja (detalle de actividades), secciones requeridas y las conclusiones (4 humanas + 4 IA).
* [ ] Mostrar matrices de confusión (10 clases) y matrices binarias con cálculo de precisión por etiqueta.
* [ ] Código para procesar imágenes y explicar la regla usada en caso de 3 vecinos distintos.
* [ ] Preparación para presentación oral: todos los miembros dominan el código.

---

## 14. Notas finales — puntos clave que debes enfatizar en la exposición y el informe

* *Reproducibilidad*: mostrar que ejecutando `run_all.py` se reproducen los resultados.
* *Rigor en preprocesamiento*: demostrar visualmente la transformación desde la foto original hasta la matriz 8×8 y el mapeo 0–16.
* *Justificación de decisiones*: explicar y justificar el método de desempate (si se usó) y cualquier mejora implementada.
* *Cumplimiento formal*: carátula, porcentaje de participación, frase del docente en el lugar indicado, y las 4 conclusiones generadas por IA.
