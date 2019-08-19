"""
This script serves as the API layer between backend WOLFGAME class and the clients, which I assume will be cellphone
"""

from flask import Flask
from flask import render_template, request, session, redirect, jsonify
from flask_cors import CORS
import wolf
import uuid

app = Flask(__name__, template_folder='templates', static_folder='assets/client')
app.secret_key = "REPLACE_ME"

wolfgame = wolf.WolfGame() # Wolf placeholder game
rolemap = {
    "WOLF": "狼人",
    "WITCH": "女巫",
    "PERCEIVAL": "预言家",
    "VILLAGER": "村民",
    "IDIOT": "白痴",
    "HUNT": "猎人",
}

# Create and expose the game instance
def create_game(config_dict):
    global wolfgame
    wolfgame = wolf.WolfGame(**config_dict)

def json_bool_response(b, reason=""):
    return {"status": b, "reason": reason}

# This is a host call
@app.route("/init")
def init():
    initargs = request.form.to_dict()
    create_game(initargs)

# this is a host call
@app.route("/start")
def start():
    if wolfgame.start_game():
        return jsonify(json_bool_response(True))
    return jsonify(json_bool_response(False, "还没全部入座呢"))

# Serve the single page app to client
@app.route("/")
def client():
    if "seat" in session:
        c_uid = wolfgame.who_sits_here(session["seat"])
        if not "uid" in session:
            session.clear()
        if "uid" in session and session["uid"] != c_uid:
            session.clear()
    return render_template("base.html")

# This is a client call
@app.route("/seat")
def seat():
    seat_num = request.args.get("seat");
    try:
        seat_num = int(seat_num)
    except:
        return jsonify(json_bool_response(False, "请输入数字"));
    if "seat" in session:
        return jsonify(json_bool_response(False, "您已经坐在了{}号".format( session["seat"])))
    if "uid" not in session:
        session["uid"] = str(uuid.uuid4())
    status, role = wolfgame.take_seat(session["uid"], seat_num)
    if status:
        session["seat"] = seat_num
        return jsonify({
            "status": True,
            "reason": "您坐在了{}号座".format(seat_num),
            "role": role
        })
    return jsonify(json_bool_response(False, "已经有人坐在这了"))

@app.route("/unseat")
def unseat():
    if "uid" not in session:
        session["uid"] = uuid.uuid4()
    if "seat" in session:
        if wolfgame.unseat(session["seat"]):
            session.pop("seat")
            return jsonify(json_bool_response(True))
        return jsonify(json_bool_response(False, "游戏已经开始"))
    return jsonify(json_bool_response(False, "您还没入坐呢"))

# This is a client call from wolf character
@app.route("/kill")
def wolfkill():
    try:
        index = int(request.args.get("index"))
    except:
        return jsonify(json_bool_response(False, "请输入数字"))
    wolflead = session.get("uid")
    # Give javascript the screening ability, but still check here
    if not wolfgame.game_roles[wolflead] == "WOLF":
        return jsonify(json_bool_response(False, "你不是狼"))
    if not wolfgame.START_FLAG:
        return jsonify(json_bool_response(False, "游戏还没开始"))
    if wolfgame.WOLF_FLAG:
        return jsonify(json_bool_response(False, "已经杀过了"))
    if wolfgame.set_kill(index):
        return jsonify(json_bool_response(True,
        "{}号玩家被杀".format(index)))
    return jsonify(json_bool_response(False, "{}号玩家不存在".format(index)))

# This is a client call from perceival
@app.route("/predict")
def predict():
    perceival = session.get("uid")
    try:
        index = int(request.args.get("index"))
    except:
        return jsonify(json_bool_response(False, "请输入数字"))
    if not wolfgame.game_roles[perceival] == "PERCEIVAL":
        return jsonify(json_bool_response(False, "你不是预言家"))
    if not wolfgame.WOLF_FLAG:
        return jsonify(json_bool_response(False, "等狼杀完"))
    if wolfgame.PREDICT_FLAG:
        return jsonify(json_bool_response(False, "本轮已经预言过了"))
    role = wolfgame.predict(index)
    if not role:
        return jsonify(json_bool_response(False, "{}号玩家不存在".format(index)))
    else: # True if bad
        reason = "坏人" if role == "WOLF" else "好人"
        return jsonify(json_bool_response(True, reason))

# This is a client call from witch
# Will receive information about who got killed
@app.route("/cure_display")
def cure_display():
    witch = session.get("uid")
    if not wolfgame.game_roles[witch] == "WITCH":
        return jsonify(json_bool_response(False, "你不是女巫"))
    if not wolfgame.PREDICT_FLAG:
        return jsonify(json_bool_response(False, "等"))
    if wolfgame.CURE_FLAG:
        return jsonify(json_bool_response(False, "快闭眼"))
    killed_index = wolfgame.get_kill()
    if killed_index < 0:
        return jsonify(json_bool_response(True, "狼人空刀"))
    else:
        return jsonify(json_bool_response(True, "{}号玩家死亡".format(killed_index)))

# This is a client call from witch
@app.route("/cure_action")
def cure_action():
    # Action must be 0 or 1 (BOOLINT)
    action = int(request.args.get("action"))
    witch = session.get("uid")
    if not wolfgame.game_roles[witch] == "WITCH":
        return jsonify(json_bool_response(False, "你不是女巫"))
    if not wolfgame.PREDICT_FLAG:
        return jsonify(json_bool_response(False, "等"))
    if wolfgame.CURE_FLAG:
        return jsonify(json_bool_response(False, "快闭眼"))
    wolfgame.cure(action)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
