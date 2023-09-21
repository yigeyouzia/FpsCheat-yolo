import ctypes

user32 = ctypes.windll.user32

#单显示器屏幕宽度和高度:
screen_size0 = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#对于多显示器设置,您可以检索虚拟显示器的组合宽度和高度:
screen_size1 = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

print(screen_size0," ", screen_size1) # (1536, 864)   (1536, 864)

# import tkinter as tk
# root = tk.Tk()
# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())
# root.destroy()