import tkinter as tk
from PIL import Image, ImageTk
import pyautogui

# スクリーンショットを撮る
screenshot = pyautogui.screenshot()

# スクリーンショットを保存する（必要に応じて）
screenshot.save("screenshot.png")

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("スクリーンショット表示")

# スクリーンショットをPillowで開く
screenshot = Image.open("screenshot.png")

# スクリーンショットをTkinterで表示できる形式に変換
screenshot_tk = ImageTk.PhotoImage(screenshot)

# キャンバスを作成して画像を表示
canvas = tk.Canvas(root, width=screenshot.width, height=screenshot.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=screenshot_tk)

# ウィンドウのメインループを開始
root.mainloop()
