# Run some test.
import uuid
import wolf
import time
from collections import Counter

def wolftest(test_string):
    def test_wrapper(test_func):
        def func_wrapper(*args, **kwargs):
            print(test_string)
            global wolfgame
            try:
                test_func(*args, **kwargs)
            except AssertionError as e:
                print("Test failed with assertion error: {}".format(e))
            except Exception as e:
                print("Test failed with other error: {}".format(e))
        func_wrapper()
    return test_wrapper

# Create non-default wolf game
@wolftest("Testing custom/default parameter and total players")
def test_parameter():
    global wolfgame
    wolfgame_config = [3,3,1,1,0]
    wolfgame = wolf.WolfGame(*wolfgame_config)
    assert(wolfgame.total_player == 9)
    # Create default wolf game
    wolfgame = wolf.WolfGame()
    assert(wolfgame.total_player == 12)

# Create 12 Users and seat them
@wolftest("Testing taking seat function with custom uuid")
def test_take_seat():
    global wolfgame, test_users
    users_uuid = [str(uuid.uuid4()) for i in range(12)]
    test_users = [{
        "index": i,
        "uid": u
        } for i, u in enumerate(users_uuid)]
    for user in test_users:
        status = wolfgame.take_seat(user["uid"], user["index"])
        if status[0]:
            user["role"] = status[1]
        else:
            raise AssertionError("Taking seat failed")
    assert(Counter(wolfgame.roles) == Counter([user["role"] for user in test_users]))

@wolftest("Testing the startgame logic, you should hear commands")
def test_start_game():
    if wolfgame.start_game():
        assert(wolfgame.START_FLAG)
        assert(wolfgame.game_roles)
        # more assertions
        time.sleep(20) # Time for audio to play
    else:
        raise AssertionError("Game did not start")

# # Get a wolf to kill a random person:
# wolves = [(i, e[0]) for i, e in enumerate(roles) if e[1] == "WOLF"]
# print(wolves)
# 
# status = wolfgame.set_kill(0)
# assert(status)
# time.sleep(30)
# 
# role = wolfgame.predict(wolves[1][0])
# assert(role == "WOLF")
# time.sleep(30)
# 
# killed = wolfgame.get_kill()
# assert(killed == 0)
# time.sleep(5)
# wolfgame.cure(False)
# 
# time.sleep(10)
# wolfgame.result()
# 
