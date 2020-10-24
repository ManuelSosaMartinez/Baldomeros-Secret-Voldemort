from fastapi import FastAPI
from .crud import *

app = FastAPI()


@app.get("/")
async def root():
  return {"secret voldemort": "initial page"}

# USER

@app.post("/account")
async def register_user():
  return {"secret voldemort": "user registration"}

@app.post("/session")
async def autenticate_user():
  return {"secret voldemort": "user autentication"}

@app.put("/session")
async def update_session():
  return {"secret voldemort": "update session status"}

@app.delete("/session")
async def close_session():
  return {"secret voldemort": "close session"}

@app.get("/user/{uid}")
async def get_user_profile():
  return {"user": "profile"}

@app.patch("/user/{uid}")
async def load_user_data():
  return {"user": "new data"}

@app.put("/user/{uid}/password")
async def change_user_password():
  return {"user": "password changed"}

# USER

# OPEN GAMES

@app.get("/games")
async def list_games():
  return {"games": "list of games"}

@app.post("/game/new")
async def create_game():
  return {"game": "created game"}

@app.get("/game/{gid}")
async def join_game():
  return {"game": "your game"}

@app.patch("/game/{gid}")
async def start_game():
  return {"game": "started game"}

@app.get("/game/{gid}/players")
async def get_game_players():
  return {"game": "list of players"}

# OPEN GAMES

# RUNNING GAMES

@app.get("/game/{gid}/player/{pid}")
async def get_player_info():
  return {"game": "player info"}

@app.put("/game/{gid}/player/{pid}/vote")
async def vote_candidate():
  return {"game": "vote"}

@app.get("/game/{gid}/election")
async def get_election_info():
  return {"game": "election info"}

@app.get("/game/{gid}/deck")
async def get_proclamations():
  return {"game": "proclamations"}

@app.put("/game/{gid}/proclamation")
async def discard_proclamations():
  return {"game": "proclamations discarded"}

@app.get("/game/{gid}/board")
async def get_phoenix_proclamations():
  return {"game": "board infor"}

# RUNNING GAMES