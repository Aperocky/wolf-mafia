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
[wolfgame.take_seat(uid, i) for i, uid in enumerate(users_uuid)]
wolfgame.start_game()

time.sleep(20)

