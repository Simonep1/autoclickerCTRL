import time
import threading
from pynput.keyboard import Key, Controller, Listener

delay = 0.001
ctrl_key = Key.ctrl_l
start_stop_key = Key.f1  # F1 key
stop_key = Key.f2  # F2 key

class ClickMouse(threading.Thread):

    def __init__(self, delay, ctrl_key):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.ctrl_key = ctrl_key
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(self.ctrl_key)
                time.sleep(self.delay)
                keyboard.release(self.ctrl_key)
                time.sleep(self.delay)
            time.sleep(0.1)

keyboard = Controller()
click_thread = ClickMouse(delay, ctrl_key)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()
