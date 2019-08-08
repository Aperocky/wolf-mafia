from flask import Flask
from flask import render_template, request, session, redirect, jsonify
from flask_cors import CORS
import wolf
import uuid

app = Flask(__name__, template_folder='templates', static_folder='assets')

GAME_START_FLAG = False
wolfgame = wolf.WolfGame() # Wolf placeholder game

# Create and expose the game instance
def create_game(config_dict):
    global wolfgame
    wolfgame = wolf.WolfGame(**config_dict)

# This is a host call
@app.route("/init")
def init():
    initargs = request.form.to_dict()
    create_game(initargs)

# this is a host call
@app.route("/start")
def start():
    if wolfgame.startable:
        return True
    return False

# This is a client call
@app.route("/seat")
def seat():
    seat_num = request.args.get("SEAT")
    
    pass

# This is a client call from wolf character
@app.route("/kill")
def wolfkill():
    pass

# This is a client call from perceival
@app.route("/predict")
def predict():
    pass

# This is a client call from witch
@app.route("/cure_display")
def cure_display():
    pass

# This is a client call from witch
@app.route("/cure_action")
def cure_action():
    pass


if __name__ == "__main__":
    app.run(debug=True)
