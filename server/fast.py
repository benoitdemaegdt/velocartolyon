from fastapi import FastAPI
from api_trajet import get_traject
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/get_json')
def get_json(
    address_start: str = "39 Cours Emile Zola 69100 Villeurbanne",
    address_end: str = "10 rue de Montbrillant 69003 Lyon"):

    output_json = get_traject(address_start, address_end)

    return output_json

@app.get("/")
def root():
    return dict(greeting="Hello")
