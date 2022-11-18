from tkinter import *
from PIL import Image, ImageTk

ws = Tk()
ws.title("Image Viewer")
ws.geometry("1366x768")

canvas = Canvas(
	ws,
	width = 1366,
	height = 768,
)

canvas.pack()

# Avril Lavigne10_566
label = Label(ws)

img = Image.open(r"../dataset/Avril Lavigne/Avril Lavigne10_566.jpg")
img = ImageTk.PhotoImage(img)

canvas.create_image(
	200,
	200,
	anchor=NW,
	image=img,
)

# Label(
# 	ws,
# 	image = label.img,
# ).pack()

ws.mainloop()