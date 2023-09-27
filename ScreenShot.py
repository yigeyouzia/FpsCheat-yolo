import cv2
import numpy as np
from mss import mss

# ScreenX = 2560  # 屏幕宽
# ScreenY = 1600  # 屏幕高
# ScreenX = 1536  # 屏幕宽
# ScreenY = 864  # 屏幕高
ScreenX = 1920  # 屏幕宽
ScreenY = 1080  # 屏幕高
# 定义截图范围 (左上角X，左上角Y，右下角X，右下角Y)
window_size = (
    int(ScreenX / 2 - 320),
    int(ScreenY / 2 - 320),
    int(ScreenX / 2 + 320),
    int(ScreenY / 2 + 320))

# window_size_all = (
#     int(0),
#     int(0),
#     int(ScreenX),
#     int(ScreenY))


# 实例化mss
Screenshot_value = mss()


def screenshot():
    # img = Screenshot_value.grab(window_size_all)  # 调用mss的方法截图
    img = Screenshot_value.grab(window_size)  # 调用mss的方法截图
    img = np.array(img)  # 转换成numpy数组
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 图片4通道转3通道
    return img
