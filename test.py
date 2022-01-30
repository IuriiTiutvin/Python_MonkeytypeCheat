import threading
import keyboard as k
def restart():
    while True:
        if k.is_pressed(['shift', 'tab']):
            print("u gau")
            main()

thread = threading.Thread(target = restart)
thread.start()
thread.join()
