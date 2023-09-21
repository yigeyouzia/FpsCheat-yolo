import threading

import pynput.mouse
from pynput.mouse import Listener

from SendInput import mouse_xy


def mouse_click(x, y, button, pressed):
    # print("debug")
    # print(x, y, button, pressed)
    print("检测到了")
    if pressed and button == pynput.keyboard.KeyCode:
        print("1")
        mouse_xy(x + 100, y + 100);
    elif not pressed and button == pynput.mouse.Button.left:
        print("2")
        mouse_xy(x, y);



def mouse_listener():
    with Listener(on_click=mouse_click) as listener:
        listener.join()

if __name__ == '__main__':
    threading.Thread(target=mouse_listener).start()