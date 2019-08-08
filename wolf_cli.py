"""
This script is to handle events from wolf, create audible events with threading so as to be non-blocking. 
"""

import logging
import sys
import time
import threading

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
    sd.play(rec_array, 5000, blocking=False)
    
def threadit(target_func, *args):
    # Open ended thread as it should end anyways.
    logger.info("Starting thread on {}".format(target_func))
    thread = threading.Thread(target_func, args=tuple(args))
    thread.start()
    
