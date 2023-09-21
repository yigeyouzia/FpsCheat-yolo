import win32api

from SendInput import *
# CDLL("lib/ghub_mouse.dll", winmode=0)
# WinDLL("lib/ghub_mouse.dll", winmode=0)
mouse_xy(1000, 1000)

# import pydirectinput
# pydirectinput.moveTo(100, 150) # 移动鼠标至坐标100，150

# point = (0, 0)
# win32api.SetCursorPos(point)