from PIL import Image, ImageTk
import tkinter as tk

# Create the root window
root = tk.Tk()

# Replace with the actual path to your image
image_path = "test.png"  

# Open the image file
img = Image.open(image_path)

# Define your desired button size
button_width = 100
button_height = 100

# Resize the image using PIL
img = img.resize((button_width, button_height), Image.LANCZOS)

# Convert the image to a PhotoImage
photoImg = ImageTk.PhotoImage(img)

# Create a button with the image
button1 = tk.Button(root, image=photoImg)
button1.pack()

root.mainloop()
