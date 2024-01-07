import tkinter as tk
from PIL import Image, ImageTk

class CanvasApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.image_on_canvas = None
        self.text_on_canvas = None
        self.canvas.bind("<Enter>", self.on_enter)

    def add_image(self, image_path):
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)
        self.image_on_canvas = self.canvas.create_image(250, 250, image=self.image)

    def add_text(self, text):
        self.text_on_canvas = self.canvas.create_text(250, 250, text=text)

    def clear_canvas(self):
        if self.image_on_canvas:
            self.canvas.delete(self.image_on_canvas)
            self.image_on_canvas = None
        if self.text_on_canvas:
            self.canvas.delete(self.text_on_canvas)
            self.text_on_canvas = None

    def on_enter(self, event):
        self.master.after(500, self.add_image, 'a_test.png')
        self.master.after(2500, self.clear_canvas)

root = tk.Tk()
app = CanvasApp(root)
root.mainloop()
