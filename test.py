import threading
import keyboard as k
def restart():
    while True:
            if k.is_pressed(['p', 'o']):
                print("u gau")

thread = threading.Thread(target = restart)
thread.start()
thread.join()
