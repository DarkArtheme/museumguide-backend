import pymongo
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from schemas import *

with open(".env", "r") as f:
    mongo_link = f.read()

client = pymongo.MongoClient(mongo_link)


database = client.museums_db
museums_collection = database.museums
users_coll = database.users_and_fav

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def start_page():
    return """ This is start page """


@app.post("/get_favorites")
async def get_favorites_by_id(data: UserId):
    result = users_coll.find_one({"UserId": data.user_id})
    favorites = []
    if result is None:
        users_coll.insert_one({"UserId": data.user_id, "Favorites": []})
        return []
    else:
        for fav in result["Favorites"]:
            favorites.append(fav)
        return favorites


@app.post("/add_to_favorites")
async def add_to_favorites(data: FavMuseum):
    result = users_coll.find_one({"UserId": data.user_id})
    if result is None:
        users_coll.insert_one({"UserId": data.user_id, "Favorites": []})
    users_coll.update({"UserId": data.user_id}, {"$addToSet": {"Favorites": data.fav_id}})


@app.post("/delete_from_favorites")
async def delete_from_favorites(data: FavMuseum):
    result = users_coll.find_one({"UserId": data.user_id})
    if result is None:
        return []
    users_coll.update({"UserId": data.user_id}, {"$pull": {"Favorites": data.user_id}})


# Retrieve all museums present in the database
@app.get("/museums")
async def get_all_museums():
    museums = []
    for museum in museums_collection.find().sort("_id", 1):
        museums.append(museum_short(museum))
    return museums


@app.post("/museums/by_id")
async def get_museum(data: MuseumId):
    museum = museums_collection.find_one({"_id": data.museum_id})
    if museum:
        return museum_helper(museum)


@app.post("/favorites")
async def get_favorites_list(data: UserId):
    fav_list = []
    fav = await get_favorites_by_id(data)
    for museum in museums_collection.find().sort("_id", 1):
        for i in fav:
            if museum["_id"] == i:
                fav_list.append(museum_helper(museum))
    return fav_list


def museum_helper(museum) -> dict:
    return {
        "id": museum["_id"],
        "name": museum["name"],
        "description": museum["description"],
        "pictures": museum["pictures"],
        "address": museum["address"],
        "phone": museum["phone"],
        "website": museum["website"],
        "worktime": museum["worktime"],
        "vk": museum["vk"],
        "inst": museum["inst"],
        "twitter": museum["twitter"],
        "facebook": museum["facebook"],
        "odnokl": museum["odnokl"],
        "eng_name": museum["eng"],
        "distance": museum["distance"],
        "station": museum["station"],
        "payment": museum["payment"],
    }


def museum_short(museum) -> dict:
    return {
        "id": museum["_id"],
        "name": museum["name"],
        "pictures": museum["pictures"][0],
        "address": museum["address"],
        "phone": museum["phone"],
        "worktime": museum["worktime"],
        "distance": museum["distance"],
        "station": museum["station"],
        "payment": museum["payment"],
    }


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8001)