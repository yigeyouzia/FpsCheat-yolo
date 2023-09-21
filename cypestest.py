from time import sleep

from SendInput import *
import pydirectinput
import win32api
import win32con
import win32gui
import win32com.client

while True:
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 100)
    sleep(5)