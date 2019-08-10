# Run some test.
import uuid
import wolf
import time

# Create non-default wolf game
wolfgame_config = [3,3,1,1,0]
wolfgame = wolf.WolfGame(*wolfgame_config)
assert(wolfgame.total_player == 9)

# Create default wolf game
wolfgame = wolf.WolfGame()
assert(wolfgame.total_player == 12)

# Create 12 Users and seat them
users_uuid = [str(uuid.uuid4()) for i in range(12)]
roles = [wolfgame.take_seat(uid, i) for i, uid in enumerate(users_uuid)]
print(roles)
wolfgame.start_game()
time.sleep(20)

# Get a wolf to kill a random person:
wolves = [(i, e[0]) for i, e in enumerate(roles) if e[1] == "WOLF"]
print(wolves)

status = wolfgame.set_kill(0)
assert(status)
time.sleep(30)

role = wolfgame.predict(wolves[1][0])
assert(role == "WOLF")
time.sleep(30)

killed = wolfgame.get_kill()
assert(killed == 0)
time.sleep(5)
wolfgame.cure(False)

time.sleep(10)
wolfgame.result()

