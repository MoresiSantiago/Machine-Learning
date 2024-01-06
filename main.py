

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

#def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
@app.get('/PlayTimeGenre/{genero: str}') 
def PlayTimeGenre():
             return

#def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas 
#jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
@app.get('/UserForGenre/{genero: str}')
def UserForGenre():
              return 

#def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados 
#por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
@app.get('/UsersRecommend/{genero: str}')
def UserRecommend():
        return

#def UsersWorstDeveloper( año : int ): Devuelve el top 3 de desarrolladoras con juegos MENOS 
#recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
@app.get('/UsersWorstDeveloper/{genero: str}')
def UsersWorstDeveloper():
        return

#def sentiment_analysis( empresa desarrolladora : str ): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la 
#desarrolladora como llave y una lista con 
#la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
@app.get('/sentiment_analysis/{genero: str}')
def sentiment_analysis():
        return