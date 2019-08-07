The requirement for the 'First Night' Web Application for a modified version of Mafia.

## Server side

### WOLF.PY

The class that stores the actual logic and are called by the server.

### SERVER.PY

Act as an API layer between the frontend and the actual class.

### API LIST

1. INIT

    This calls the init to get a WOLF instance. Player type & count is passed in.

    WOLF shall process init as such that it will predetermined.

2. DISPLAY

    This will display the seating area for all calls.

3. TAKE\_SEAT

    This call allow the person to assume a specific seat in the game.

    The client will register a cookie with calltype and use that for all of subsequent calls.

    The client will have to use repeat ajax request to verify that the game has not actually started. BECAUSE SOCKET IO WON'T WORK DUE TO APPLE SHIT.
    actually on second thought they don't need this

    The call will also return all the data pertinent to the character of that seat.

4. START

    This start the game after all seat has been occupied.

    This will play music from a specific computer (master), START_FLAG will be set, allowing further API

5. WOLF\_KILL

    This API is only available to WOLF. This will designate a specific person to be killed.

    Will set KILL_FLAG in WOLF class to TRUE, enable further API from other character.

    Disable all future WOLF_KILL API calls

6. PREDICT

    Perceival will predict a Player, return True or False.

    Will set PREDICT_FLAG to TRUE. Only possible if KILL_FLAG has been set.

7. CURE\_VISIBLE && CURE\_ACTION

    VISIBLE will return killed person

    ACTION will allow cure/not

    set CURE_FLAG to true

8. DECLARE

    This will be called when all finishes, the host computer then announce last night's results.

