

from fastapi import FastAPI
import pandas as pd

from fastapi.responses import RedirectResponse # esta libreria funciona para la url.

app=FastAPI()

# Cargar los datos desde los archivos CSV y Parquet
genre_data = pd.read_csv('genre.csv')
items_data = pd.read_parquet('items1.parquet')
reviews_data = pd.read_csv('reviews.csv') 
steam_data = pd.read_csv('steam.csv')


@app.get("/", include_in_schema=False)  # esta funcion genera que la url ya venga con /doc*/ haciendo que se abra directo el API. 
async def redirect_to_docs():
    return RedirectResponse("/docs")


# Se definen los endpoints de la API:

@app.get("/¡Hola, bienvenido!") # Funcion que saluda a los ingresantes.
def index():
        return {"message": "¡HOLA, Bienvenido!"}

#def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.
@app.get('/developer/{desarrollador: str}') 
def developer():
   return

#def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
@app.get('/userdata/{User:id: str}')
def userdata():
              return 

#def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
@app.get('/UserForGenre/{genero: str}')
def UserForGenre():
        return

#def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)
@app.get('/best_developer_year/{año: int}')
def best_developer_year():
        return

#def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.
@app.get('/developer_reviews_analysis/{desarrolladora: str}')
def developer_reviews_analysis():
        return