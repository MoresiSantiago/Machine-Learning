# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>


<p align="center">
<img src="https://edimar.com/wp-content/uploads/2021/03/Que-es-Machine-Learning-Industria.jpg"  height=300>
</p>

¡ Bienvenidos a mi proyecto de machine learning. Mi nombre es **`Santiago Moresi`**, por si les gusta mi proyecto les dejo mi mail santiagomoresi@gmail.com !
<hr>


En este proyecto se uso una base de datos de 'STEAM GAMES' que es una platafroma de videojuegos. 




<p align="center">
<img src="https://images.ladbible.com/resize?type=webp&quality=70&width=720&fit=contain&gravity=null&url=https://images.ladbiblegroup.com/v3/assets/bltbc1876152fcd9f07/bltab7a7cd3fa00201f/65083138fa17d27f31096188/steam_(2).png"  height=300>
</p>

Y la idea era que atraves de esta base de datos se genere un trabajo de 
**`Ingenieria de datos`** y otra de **`Machine Learning`**. 


## **INGENIERIA DE DATOS** 
 
En esta sección, se llevó a cabo un proceso de Extracción, Transformación y Carga (ETL) de varios archivos, 
* **`Reviews`** -  **`Items`** - **`Steam`** - **`Genre`**

Este proceso implicó la carga inicial de archivos en formato JSON, seguida de una transformación necesaria para facilitar el manejo de los datos. En particular, se optó por convertirlos en archivos CSV para reducir el peso y mejorar la manejabilidad. Además, en ciertos casos, se elige el formato '.parquet' debido a la gran cantidad de datos y su capacidad para manejar estructuras complejas de manera eficiente.

Durante la transformación, se realizaron ajustes en los datos, como la consolidación de las fechas, que originalmente se encontraban distribuidas en columnas separadas, en una única columna para mejorar la estructura y el registro de los datos. Asimismo, se eliminarán datos innecesarios para reducir el tamaño del archivo y mejorar su eficiencia.

Cada uno de los archivos de  '**`ETL - ...`**' contiene un detalle paso a paso de las acciones realizadas durante el proceso de ETL.

Además del proceso de ETL, se llevó a cabo un análisis de sentimiento (PNL) que se encuentra detallado en el archivo 'ETL-reviews'. En este archivo, se asignan valores numéricos (0 para 'MALO', 1 para 'NEUTRO' y 2 para 'POSITIVO') para reemplazar las palabras en las reseñas. Esta transformación permitió establecer una representación binaria que facilite el trabajo con modelos de aprendizaje automático en análisis de sentimiento. 



## **MACHINE LEARNING**

En esta segunda parte se realizo un **`Analisis exploratorio de los datos (EDA)`**.  

Se buscaron: 
             
**`Datos faltantes`**.: En el análisis exploratorio de datos, uno de los primeros pasos es identificar si hay datos faltantes en el conjunto de datos. Los datos faltantes pueden afectar  la calidad del análisis y los resultados. Para abordar este problema, se llevaron a cabo las siguientes acciones,
        
-  Identificación de variables con datos faltantes: Se examinaron todas las variables en busca de valores nulos o ausentes.
- Tratamiento de datos faltantes: Dependiendo de la cantidad y la naturaleza de los datos faltantes, se tomaron medidas para lidiar con ellos. Esto podría incluir eliminar registros con datos faltantes, mediana, o utilizar técnicas más avanzadas como el uso de modelos predictivos para rellenar los valores faltantes.

             
 **`Datos duplicados`**: Los datos duplicados pueden distorsionar el análisis y generar resultados erróneos. Para abordar este problema, se llevaron a cabo las siguientes acciones,
       
- Identificación de datos duplicados: Se buscaron registros duplicados en el conjunto de datos. Esto se puede hacer mediante comparaciones de filas o combinaciones de columnas.

             
**`Datos Atípicos (Outliers)`**.: Los datos atípicos son valores inusuales o extremos en el conjunto de datos que pueden afectar significativamente el análisis. Para tratar los datos atípicos en el análisis exploratorio de datos, se realizaron las siguientes acciones,
         
- Identificación de datos atípicos: Se utilizaron diversas técnicas estadísticas y visuales para identificar datos atípicos en las variables relevantes. Esto podría incluir el uso de gráficos de caja, análisis de dispersión, pruebas estadísticas y más.
-  Tratamiento de datos atípicos: Dependiendo de la naturaleza de los datos atípicos y los objetivos del análisis, se toman decisiones sobre cómo tratarlos. Esto podría incluir la eliminación de valores atípicos, la transformación de variables, o el análisis de los datos con y sin la presencia de valores atípicos para comprender su impacto en los resultados.
             


## **API - DEPLOY**

<p align="center">
<img src="https://www.cloudcenterandalucia.es/wp-content/uploads/2021/05/Servidor-web_Cloud-Center-Andalucia_Cabecera.png"  height=300>
</p>



El término Deploy hace referencia al proceso de implementar o poner en funcionamiento una aplicación, software, sitio web u otro sistema. En este contexto, se aplica a un sitio web que se creó utilizando los servicios de [Render](https://render.com/docs/free#free-web-services)  . Para llevar a cabo el despliegue en Render, es necesario proporcionar un archivo denominado Requirements.txt, el cual contenga las versiones de las bibliotecas que se utilizarán en el desarrollo.

Este proceso de implementación permite que mi **`API`** deje de depender de un servidor local y comience a operar en servidores web, lo que proporciona una mayor disponibilidad y acceso público a la aplicación.

¿ Que es **`API`**? API significa "Interfaz de Programación de Aplicaciones". Es un conjunto de reglas y protocolos que permiten que diferentes componentes de software se comuniquen entre sí. 
    Las API son utilizadas por los desarrolladores para permitir que sus aplicaciones se conecten y utilicen funcionalidades proporcionadas por otros servicios, aplicaciones o plataformas.

Dentro del API vas a encontrar varias funciones: 
 - 1º  :   def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.

- 2º :  def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
 
- 3º:  def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

- 4º: def **UsersWorstDeveloper( *`año` : int* )**:
   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

- 5º: def **sentiment_analysis( *`empresa desarrolladora` : str* )**:
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total 
    de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 




##
**Este link te lleva al Render:** 
https://santiagomoresi-ml-4vt1.onrender.com
