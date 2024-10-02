# Análisis de Telecomunicaciones en Argentina

En este proyecto se busca analizar el panorama de las telecomunicaciones en Argentina durante el primer trimestre de 2024. El objetivo es comparar las tendencias de crecimiento, ingresos y tecnologías más utilizadas en los servicios de internet y televisión durante el periodo evaluado, partiendo de la siguiente hipótesis:

> A raiz de la pandemia y el aumento de los servicios de streaming como Netflix, Disney+, HBO Max, entre otros, el uso de Internet aumentó, pero la Televisión ha decaído en número de usuarios e ingresos.

## Preview

_[Dashboard Desplegado con Streamlit](https://telecomunicaciones-argentina.streamlit.app)_

![image](https://github.com/user-attachments/assets/7431f406-007c-444c-bce9-fb0f0c051631)

Además se hizo una breve presentación con los datos obtenidos, la cual puede encontrarse aquí: _[Evolución de Internet y Televisión en Argentina](https://www.canva.com/design/DAGSXt08Lfw/edoCEBk4TAXwlu6lL9WTQg/edit?utm_content=DAGSXt08Lfw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)_

## Objetivos

1. **Medir el crecimiento y los ingresos** de los servicios de internet y televisión.
2. **Identificar las tecnologías más utilizadas** en cada servicio.
3. **Analizar las tendencias** observadas en el primer trimestre de 2024 en relación con el año anterior.
4. **Evaluar KPIs clave** para determinar el éxito de las metas establecidas en el sector de telecomunicaciones.
5. **Presentar un dashboard** para visualizar la información y los KPIs definidos

## Fases del Proyecto

- **Análisis Exploratorio de Datos (EDA)**: Se realizaron análisis detallados en los archivos `television_EDA.ipynb` e `internet_EDA.ipynb` con el fin de entender la estructura de los datos, identificar valores atípicos, valores faltantes y determinar distribuciones de variables clave.
  
- **Análisis de Crecimiento Anual**: Se evaluaron las tasas de crecimiento anual de ingresos y usuarios en cada servicio, comparando los resultados reales con las metas establecidas.

- **Análisis de Penetración**: Se analizaron los indicadores de penetración de internet y televisión en Argentina, tanto en el año actual como a lo largo del periodo 2014-2023, para entender la evolución de ambos mercados.

- **Crecimiento de Ingresos**: Se compararon los ingresos generados por cada tecnología y servicio para evaluar la contribución económica de cada uno.

- **Dashboard publicado**: Se creó el dashboard con la información de la TV y el Internet, en el cual se puede ver la información de manera gráfica y se tienen presentes los KPIs que se establecerán a continuación

## Limpieza de los datos

### Explicación de las Transformaciones Realizadas en internet_EDA.ipynb

El archivo `internet_EDA.ipynb` contiene un análisis de los datos de acceso a Internet en Argentina. Se trabajó con varios conjuntos de datos y se realizaron diversas transformaciones para limpiar y preparar los datos antes de hacer el análisis y las visualizaciones. A continuación se resumen las transformaciones realizadas:

1. **Dataset de Velocidad de Internet**

- Se cargó un dataset que contiene información sobre la velocidad de Internet en las diferentes provincias de Argentina.
- Se limpiaron los datos eliminando filas con valores faltantes para asegurar la integridad del análisis.
- Se agruparon los datos por año y provincia para obtener un panorama de las velocidades de conexión en diferentes períodos.
- Se calcularon estadísticas como la velocidad promedio y la mediana de las velocidades de bajada (Mbps) para realizar un análisis descriptivo de la situación de conectividad.

2. **Dataset de Accesos por Tecnología**

- Este dataset se utilizó para conocer cuántos accesos existen para cada tipo de tecnología de Internet en las provincias.
- Se agruparon los datos por año y provincia para observar el comportamiento y evolución de las diferentes tecnologías a lo largo del tiempo.
- Se limpiaron y consolidaron las tecnologías en categorías más manejables para facilitar la interpretación de los resultados.

3. **Dataset de Velocidades (Media de Bajada)**

- Se creó un dataset adicional con el propósito de calcular la media y la mediana de las velocidades de bajada (Mbps) en el año 2023, para comparar el estado actual de la conectividad en las provincias.
- Este análisis permitió identificar qué provincias tienen mejores o peores velocidades de conexión y cómo varía la calidad del servicio en distintas regiones.

4. **Dataset de Penetración de Internet**

- Se trabajó con un dataset que contiene información sobre la penetración de Internet (porcentaje de hogares conectados) en cada provincia.
- Se realizó un análisis de la evolución de la penetración a lo largo del tiempo, agrupando por año y provincia.
- Se unificaron trimestres para realizar un análisis anual más completo.

5. **Dataset de Ingresos por Internet**

- Este dataset se utilizó para analizar los ingresos anuales generados por el servicio de Internet en las provincias.
- Se agruparon los datos por año y provincia para obtener la suma de ingresos totales.
- Se visualizó la evolución de los ingresos a lo largo del tiempo, lo cual permitió observar cómo crece o decrece el mercado de Internet en Argentina.

6. **Limpieza y Consolidación de Datos**

- En todos los datasets se realizaron operaciones de limpieza, como la eliminación de duplicados y la corrección de inconsistencias en nombres de provincias.
- Los datos se normalizaron y estandarizaron para asegurar que todas las observaciones estuvieran correctamente alineadas.

7. **Exportación de Resultados**

- Una vez procesados y limpios, los datos se exportaron a archivos CSV para su almacenamiento y futura utilización.
- Esto incluyó la exportación de datos limpios de velocidades, accesos por tecnología y penetración anual por provincia.

8. **Visualizaciones y Análisis**

- Se realizaron visualizaciones de las velocidades promedio y medianas de conexión por provincia, así como de la evolución de la penetración y los ingresos.
- Estas visualizaciones permitieron una mejor comprensión de la situación de acceso a Internet en Argentina y ayudaron a resaltar las diferencias entre las provincias.

### Explicación de las Transformaciones Realizadas en television_EDA.ipynb

De igual forma, el archivo `television_EDA.ipynb` contiene un análisis de los datos relacionados con el acceso a servicios de televisión en Argentina. Se trabajó con varios conjuntos de datos y se llevaron a cabo transformaciones para preparar y analizar la información. A continuación se describen los pasos realizados:

1. **Dataset de Accesos por Provincia a TV**

- Se cargó un dataset que contiene la cantidad de accesos a servicios de televisión en cada provincia de Argentina.
- Se realizó una limpieza de datos para eliminar filas con valores faltantes y asegurar la calidad del análisis.
- Se agruparon los datos por año y provincia para obtener una visión general de cómo ha evolucionado el acceso a este servicio en las diferentes regiones.
- Se renombraron las columnas y se verificaron los datos para garantizar consistencia en los nombres de las provincias y evitar duplicados o errores de escritura.

2. **Dataset de Ingresos de TV por Suscripción**

- Este dataset se utilizó para conocer los ingresos generados por la televisión por suscripción en Argentina.
- Se agruparon los datos por año, provincia y trimestre para evaluar la evolución de los ingresos a lo largo del tiempo.
- Se normalizaron los datos y se ajustaron los nombres de las provincias para asegurar que coincidieran con el resto de los datasets y se pudieran hacer análisis cruzados.

3. **Dataset de Penetración de TV por Suscripción**

- Se utilizó un dataset que contiene la información de la penetración de la televisión por suscripción en cada provincia, es decir, el porcentaje de hogares con acceso a este servicio.
- Se analizaron las tasas de penetración a lo largo de los años, agrupando los datos por año y provincia.
- Se verificó la consistencia de los datos y se ajustaron los nombres de las provincias para alinear este dataset con el resto de los datos.

4. **Limpieza y Consistencia de Datos**

- Se realizaron procesos de limpieza en todos los datasets para eliminar duplicados, valores faltantes y posibles errores de escritura en los nombres de las provincias.
- Se unificaron listas de nombres de provincias y se normalizaron los nombres para asegurar consistencia a lo largo de todos los datasets.
- Se verificó si existían provincias con diferentes nombres o abreviaturas que pudieran generar inconsistencias en los análisis.

5. **Análisis de Accesos y Crecimiento**

- Se creó un DataFrame para analizar el total de accesos por provincia y año, y se estudió cómo ha cambiado el número de suscriptores a lo largo del tiempo.
- Se generaron visualizaciones para entender la evolución de los accesos a la televisión por suscripción en cada provincia.

6. **Análisis de Penetración**

- Se estudió la evolución de la penetración del servicio de televisión por suscripción en cada provincia a lo largo del tiempo.
- Se identificaron provincias con mayores y menores tasas de penetración y se analizaron los factores que pueden influir en estos resultados.

7. **Exportación de Datos**

- Se guardaron los resultados obtenidos y los datos limpios en archivos CSV para su uso posterior.
- Esto incluyó la exportación de accesos anuales por provincia y otras métricas relevantes relacionadas con la televisión por suscripción.

8. **Visualizaciones y Observaciones**
- Se realizaron gráficos y visualizaciones para ilustrar las tendencias de crecimiento de accesos, ingresos y penetración de la televisión por suscripción.
- Estas visualizaciones permitieron entender de manera más clara cómo ha cambiado el mercado de la televisión por suscripción en Argentina, destacando las provincias con mayor crecimiento y aquellas con menor penetración.

## KPIs establecidos

Para este proyecto se definieron 4 KPIs, los cuales se crearon alineados con la información presente en los datasets. Siendo que el análisis se hizo originalmente para verificar la hipótesis planteada, la cual era si los usuarios de Internet crecian mientras que los TV caían, se consideró adecuado tener estos 4 KPIs como parte del proyecto.

### Crecimiento de Ingresos de TV
- **Meta de Crecimiento Anual**: 5%
- **Crecimiento Real**: 11.32%
- **Conclusión**: ¡Meta alcanzada! 🎉

### Crecimiento de Ingresos de Internet
- **Meta de Crecimiento Anual**: 10%
- **Crecimiento Real**: 54.86%
- **Conclusión**: ¡Meta alcanzada! 🎉

### Incremento de Penetración de Internet (2014 - 2023)
- **Meta de Crecimiento de Internet**: 15%
- **Crecimiento Real**: 54.86%
- **Conclusión**: ¡Meta alcanzada! 🎉

### Incremento de Penetración de TV (2014 - 2023)
- **Meta de Crecimiento de TV**: 10%
- **Crecimiento Real**: 11.32%
- **Conclusión**: ¡Meta alcanzada! 🎉

## Conclusiones

El análisis sugiere que el mercado de las telecomunicaciones en Argentina ha experimentado un crecimiento significativo en el sector de internet, con un crecimiento real que supera ampliamente las metas establecidas. El sector de televisión también ha logrado alcanzar sus objetivos, aunque con un crecimiento menor en comparación con internet. Ambos sectores parecen estar en transición hacia tecnologías más avanzadas y buscan adaptarse a un entorno digital más competitivo.

Con la información obtenido y lo que se logra ver en los KPIs, puede decirse que la hipótesis inicial es incorrecta, pues aunque la TV ha crecido de forma más lenta, sigue subiendo su base de usuarios así como sus ingresos, por lo que no, ningún servicio de streaming parece haber afectado realmente la industria de la Televisión en argentina, o por lo menos así ha sido hasta ahora.

## Repositorio de Archivos

- `.data/`: Carpeta con los datasets originales utilizados.
- `.EDA_CSV_Limpios/`: Carpeta con los datasets creados a partir de la limpieza de los datos.
- `television_EDA.ipynb`: Análisis Exploratorio de Datos del servicio de televisión.
- `internet_EDA.ipynb`: Análisis Exploratorio de Datos del servicio de internet.
-  `dashboard.py`: Archivo desde el cual se despliega el dashboard con `Streamlit`.
