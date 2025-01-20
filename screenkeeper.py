import ctypes
import time

mouse_event = ctypes.windll.user32.mouse_event
MOUSE_EVENT_MODE = 0x0001
timer = 10
movement = 2
print("press ctrl + c to exit")
try:
    while True:
        mouse_event(MOUSE_EVENT_MODE, movement, 0, 0, 0, 0)  # right
        time.sleep(timer)
        mouse_event(MOUSE_EVENT_MODE, -movement, 0, 0, 0, 0)  # left
        time.sleep(timer)
except KeyboardInterrupt:
    pass
