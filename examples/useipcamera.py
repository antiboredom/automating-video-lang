import time
import ipcamera
import random

ipcamera.record('coolvid2.mp4', '00:00:30')

starttime = time.time()
currenttime = time.time()

while currenttime - starttime < 30:
    ipcamera.tilt(random.randint(-180, 180))
    time.sleep(.5)
    ipcamera.pan(random.randint(-180, 180))
    time.sleep(.5)
    currenttime = time.time()


