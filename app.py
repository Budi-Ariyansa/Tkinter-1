from distutils import command
from tkinter import *
from tkinter.filedialog import FileDialog, askopenfile

from matplotlib.pyplot import text

root = Tk()
root.geometry("400x400")
root.title("OImage")

photo = PhotoImage(file="C:\\Users\\ASUS\\Pictures\\LogoFTI.png")

frame = LabelFrame(root, text="Image View")
frame.grid(row=0, column=0, padx=20, pady=20)

image = Label(frame, text="No Image", image=photo)
image.pack()

open_dialog = Button(frame, text="Open Image", command=lambda:askopenfile())
open_dialog.pack(padx=20, pady=20)

root.mainloop()