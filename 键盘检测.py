from pynput import keyboard  # 首先导入模块


def key_press(key):  # 定义按键按下时触发的函数
    print("按键被按下了")


def key_release(key):
    print("按键被松开了")


with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()