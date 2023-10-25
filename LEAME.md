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
 
 En esta parte consta de realizar una **`Extraccion, Transformacion y Carga (ETL)`**.  
 De los archivos:   *`Reviews`*  - *`Items`* - *`Steam`*  -  *`Genre`*  

 Se hizo una  Carga de los archivos, originalmente eran archivos '.json', se tuvo que hacer una transofrmacion ya que este tipo de achivos son muy dificiles de trabajar y se tranformaron en arhcivos '.csv' ya que asi son mas ligeros y mas facil manejarlos. Y particularmente se uso archivo parquet porque era demasiado pesado y contenia demsaidos datos se tomo la desicion de usar '.parquet' porque tiene la caracteristica de tener un diseño teniendo en cuenta estructuras complejas. 

Hubieron que Transformar datos como las fechas que se encontraban los años - meses - dias en columnas separadas y se agruparon para asi poder llevar un registro mas adecuado. 

Y por ulitmo, se Extrajeron datos de los cuales no eran utiles y para hacer el archivo mas ligero se eliminaron. 

En cada archivo de 'ETL - ... ' esta mas detallado paso por paso lo que se realizo. 

Se realizo *`Anlisis de sentimento (PNL)`*, que se puede encontrar en el archivo 'ETL-reviews', esta columna tiene la particularidad de contener los numeros '0' `MALO` - 1' `NEUTRO` - '2' `POSITIVO`. Vienen a remplazar a las palabras de las reseñas dejando asi una froma binaria para luego poder trabajar mejor con el modelo de aprendizaje automatico. 



## **MACHINE LEARNING**

En esta segunda parte se realizo un **`Analisis exploratorio de los datos (EDA)`**.

Se buscaron: 
             
             * Datos faltantes

             
             * Datos duplicados

             
             * Datos atipicos
             


## **API - DEPLOY**

<p align="center">
<img src="https://www.cloudcenterandalucia.es/wp-content/uploads/2021/05/Servidor-web_Cloud-Center-Andalucia_Cabecera.png"  height=300>
</p>


El termino **`Deploy`** se refiere al rpoceso de implementar o lanzar una aplicacion, software, sitio web o cualuiqer otro sistema. En este caso es para un sitio we, que se relaizo gracias a los sistemas de [Render](https://render.com/docs/free#free-web-services) para lanzar el render se necesita un archivo **`Requirements.txt`** que dentro contiene las versiones de las librerias que use. 

Con esto mi **`API`** pasa de usar mi servidor local a servidores web. 
