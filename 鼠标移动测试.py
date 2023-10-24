from time import sleep

import win32api

from SendInput import *
# CDLL("lib/ghub_mouse.dll", winmode=0)
# WinDLL("lib/ghub_mouse.dll", winmode=0)
# mouse_xy(1000, 1000)

import pydirectinput

while True:
    pydirectinput.click() # 移动鼠标至坐标100，150
    sleep(5)
# while True:
#     pydirectinput.moveTo(300, 300) # 移动鼠标至坐标100，150
# pydirectinput.click() # 点击鼠标左键
# pydirectinput.click(200, 220) # 移动鼠标至坐标200，220，并点击左键
# pydirectinput.move(None, 10)  # 鼠标移动相对y位置
# pydirectinput.doubleClick() # 双击鼠标左键
# pydirectinput.press('esc') # 按一下esc
# pydirectinput.keyDown('shift')#按下shift
# pydirectinput.keyUp('shift')#弹起shift

# import pydirectinput
# pydirectinput.moveTo(100, 150) # 移动鼠标至坐标100，150

# point = (0, 0)
# win32api.SetCursorPos(point)