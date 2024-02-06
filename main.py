

from fastapi import FastAPI, Path
import pandas as pd
import numpy as np
import math
import json
from typing import Dict, Any
from typing import List, Optional


from fastapi.responses import RedirectResponse # esta libreria funciona para la url.

app=FastAPI()

# Cargar los datos desde los archivos CSV y Parquet
df1 = pd.read_csv('genre.csv')
df2 = pd.read_parquet('items1.parquet')
df3 = pd.read_csv('reviews.csv') 
df4 = pd.read_csv('steam.csv')
df_5 = pd.concat([df1, df2, df3, df4])

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
@app.get('/UserForGenre/{Genero: str}')
def UserForGenre(genero: str) -> dict:
    df_genres = df_5[df_5['Genero'] == genero]
    
    # Eliminar filas donde 'playtime_forever' es 0
    df_genres = df2[df2['playtime_forever'] != 0]

    if df_genres.empty:
        # Si no hay datos después de aplicar los filtros, retornar un mensaje
        return {"message": f"No hay datos para el género {genero}"}

    # Manejar el caso de valores no numéricos en 'user_id'
    try:
        user_id_max_playtime = int(df_genres.loc[df_genres['playtime_forever'].idxmax(), 'user_id_code'])

    except (ValueError, TypeError):
        return {"message": f"Error al obtener el usuario con más horas jugadas para el género {genero}. Asegúrate de que 'user_id' sea un valor numérico."}

    agg_df = df_5.groupby('release_year').agg({'user_id_code': max, 'playtime_forever': sum}).reset_index()
    
    playtime_list = agg_df.to_dict(orient='records')

    result = {
        "Usuario con más horas jugadas para Género " + genero: user_id_max_playtime,
        "Horas jugadas": [{
            
            "release_year": int(item["release_year"]),
            #"user_id_code": int(item["user_id_code"]) if not math.isnan(item["user_id_code"]) else None,
            "playtime_forever": int(item["playtime_forever"]) } #if not math.isnan(item["playtime_forever"]) else None }
            for item in playtime_list]
        
    }

    return result 

#def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)
@app.get('/best_developer_year/{año: int}')
def best_developer_year():        
        return

#def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.
@app.get('/developer_reviews_analysis/{desarrolladora: str}')
def developer_reviews_analysis():
        return