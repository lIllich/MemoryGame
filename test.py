# from PIL import Image, ImageTk
# import tkinter as tk

# # Create the root window
# root = tk.Tk()

# # Replace with the actual path to your image
# image_path = "slike/zivotinje/leptir.png"  

# # Open the image file
# img = Image.open(image_path)

# # Define your desired button size
# button_width = 100
# button_height = 100

# # Resize the image using PIL
# img = img.resize((button_width, button_height), Image.LANCZOS)

# # Convert the image to a PhotoImage
# photoImg = ImageTk.PhotoImage(img)

# # Create a button with the image
# button1 = tk.Button(root, text="1234", image=photoImg)
# button1.pack()

# root.mainloop()


from classes.CategoryManager import CategoryManager
import random

c = CategoryManager("categories.json")
c.load_categories()
letters = []
rows = 2
cols = 2



for category in c.category['category']:
            if category['iterate'] == 'single_string':
                for card in category['cards']:
                    letters.append(card)
            elif category['iterate'] == 'double_string':
                for card in category['cards']:
                    letters.append(card['value2'])
            elif category['iterate'] == 'name_and_image':
                for card in category['cards']:
                    letters.append(card['name'])
        

random.shuffle(letters)
letters = letters[: rows * cols // 2] * 2
print(letters)
