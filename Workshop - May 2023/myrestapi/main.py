from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


class Show(BaseModel):
    name: str
    producer: str
    description: str
    show_id: str


app = FastAPI()


shows_db = [
    { 'name': 'The Wire',
      'producer': 'HBO',
      'description': 'This is the tv show description',
      'show_id': '1'},

    { 'name': 'Breaking Bad',
      'producer': 'HBO',
      'description': 'This is the tv show description',
      'show_id': '2'},

    { 'name': 'Mindhunter',
      'producer': 'Netflix',
      'description': 'This is the tv show description',
      'show_id': '3'},

    { 'name': 'Vikings',
      'producer': 'History',
      'description': 'This is the tv show description',
      'show_id': '4'},
]


@app.get("/")
async def home():
    #return {"message": "Hello World"}
    return {"all_shows": shows_db}


@app.get("/shows/{show_id}")
async def get_show(show_id: str):
    for show in shows_db:
        if show['show_id'] == show_id:
            return show
    return {"Error": "No show in DB with such id"}


@app.post("/create")
async def create_show(show: Show):
    shows_db.append(show)
    return show


@app.put("/update/{show_id}", response_model=Show)
async def update_show(show_id: str, show: Show):
    update_show_encoded = jsonable_encoder(show)
    for i in range(len(shows_db)):
        if shows_db[i]['show_id'] == show_id:
            shows_db[i] = update_show_encoded
            
    return update_show_encoded