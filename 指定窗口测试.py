from time import sleep

import cv2

from ScreenShot import screenshot
import win32gui
import win32con

# im0 = screenshot()
# cv2.imshow('test', im0)
hwnd = win32gui.FindWindow(None, 'window')
# 置顶
# win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 640, 640, win32con.SWP_SHOWWINDOW)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)