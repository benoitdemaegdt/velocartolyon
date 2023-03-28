from fastapi import FastAPI
from api_trajet import get_traject

app = FastAPI()

@app.get('/get_json')
def get_geojson(adress_start: str,
                adress_end: str):

    get_traject(adress_start, adress_end)


    return f

@app.get("/")
def root():
    return dict(greeting="Hello")
