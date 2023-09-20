import win32gui
import win32con

hwnd = win32gui.FindWindow(None, 'window')
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
