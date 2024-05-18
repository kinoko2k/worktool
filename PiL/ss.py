import tkinter as tk
from PIL import Image, ImageTk
import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

root = tk.Tk()
root.title("スクリーンショット表示")

screenshot = Image.open("screenshot.png")
screenshot_tk = ImageTk.PhotoImage(screenshot)

canvas = tk.Canvas(root, width=screenshot.width, height=screenshot.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=screenshot_tk)

root.mainloop()
