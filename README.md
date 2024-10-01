# Análisis de Telecomunicaciones en Argentina

En este proyecto se busca analizar el panorama de las telecomunicaciones en Argentina durante el primer trimestre de 2024. El objetivo es comparar las tendencias de crecimiento, ingresos y tecnologías más utilizadas en los servicios de internet y televisión durante el periodo evaluado, partiendo de la siguiente hipótesis:

> A raiz de la pandemia y el aumento de los servicios de streaming como Netflix, Disney+, HBO Max, entre otros, el uso de Internet aumentó, pero la Televisión ha decaído en número de usuarios e ingresos.

## Preview

_[Dashboard Desplegado con Streamlit](https://telecomunicaciones-argentina.streamlit.app)_

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
