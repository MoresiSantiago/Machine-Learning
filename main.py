

from fastapi import FastAPI
import pandas as pd


app=FastAPI()


# Cargar los datos desde los archivos CSV y Parquet
genre_data = pd.read_csv('genre.csv')
items_data = pd.read_parquet('items1.parquet')
reviews_data = pd.read_csv('reviews.csv')
steam_data = pd.read_csv('steam.csv')

# Se definen los endpoints de la API
@app.get("/INICIO")
def index():
        return {"message": "¡HOLA, Bienvenido!"}

@app.get('/desarrollador/ {item_id: str}')  # Cantidad de items y porcentajede contenido Free por año según empresa desarrolladora
def desarrollador (item_id: str):
    if item_id in items_data:
        return items_data[item_id]
    
    else:
        return "desarrollador NO encontrado", 404
    

@app.get('/userdata/ {user_id: str}') # Debe devolver cantidadde dinero gastado por el usuario, el porcentajede recomendación en base a reviews.recommend y cantidad de items
def userdata (user_id :str):
    if user_id in reviews_data:
        return reviews_data[user_id]
    else: 
        return 'user NO encontrado', 404




