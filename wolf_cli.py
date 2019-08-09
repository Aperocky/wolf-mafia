"""
This script is to handle events from wolf, create audible events with threading so as to be non-blocking. 
"""

import logging
import sys
import time
import threading
import subprocess

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
logger.addHandler(stdout_handler)

SOUND_ASSET_DIR = "assets/sound/"

def play_record(filename):
    import sounddevice as sd
    import numpy as np
    if not filename.endswith("npy"):
        filename+=".npy"
    rec_array = np.load(filename)
    sd.play(rec_array, 5000, blocking=True)

def thread_run(target_func):
    def wrapper(*args):
        logger.info("Starting thread on {}".format(target_func))
        thread = threading.Thread(target=target_func, args=tuple(args))
        thread.start()
    return wrapper
    
@thread_run
def wolf_start():
    time.sleep(5)
    play_record(SOUND_ASSET_DIR + "night_fall_close_eye")
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "wolf_open_eye")
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "wolf_please_kill")

@thread_run
def perceival_start():
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "wolf_already")
    time.sleep(5)
    play_record(SOUND_ASSET_DIR + "perceival_open")
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "perceival_decide")

@thread_run
def witch_start():
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "perceival_close")
    time.sleep(5)
    play_record(SOUND_ASSET_DIR + "witch_open")
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "witch_save_or_not")
    
@thread_run
def end_night():
    time.sleep(2)
    play_record(SOUND_ASSET_DIR + "witch_close")
    time.sleep(3)
    play_record(SOUND_ASSET_DIR + "dawn")

@thread_run
def announce_result(index):
    time.sleep(2)
    if index < 0:
        play_record(SOUND_ASSET_DIR + "end_result_peace")
    else:
        play_record(SOUND_ASSET_DIR + "end_result_mort_first")
        subprocess.call(["say", index])
        time.sleep(0.3)
        play_record(SOUND_ASSET_DIR + "end_result_mort_second")

