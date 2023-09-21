import win32gui
import win32con


if __name__ == '__main__':
    print("1")
    hwnd = win32gui.FindWindow(None, 'window')
    # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
    #                       win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    # 置顶
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 640, 640, win32con.SWP_SHOWWINDOW)