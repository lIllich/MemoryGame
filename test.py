import tkinter as tk
from tkinter import PhotoImage

def button_click():
    print("Button clicked!")

root = tk.Tk()

# Create a PhotoImage object from an image file
image_path = "test.png"  # Replace with the actual path to your image
img = PhotoImage(file=image_path)

# Create a button with the image
button1 = tk.Button(root, image=img, command=button_click)
button2 = tk.Button(root, text="1234", command=button_click)
button1.pack()
button2.pack()

root.mainloop()


# import tkinter as tk

# # Define a class for the home screen
# class HomeScreen:
#     def __init__(self, master):
#         # Initialize the home screen with the specified master (root) window
#         self.master = master
#         master.title("Home Screen")

#         # You would typically add widgets (buttons, labels, etc.) and configure the layout here.

# # Define the main function
# def main():
#     # Create the main (root) window
#     root = tk.Tk()

#     # Create an instance of the HomeScreen class, passing the root window as the master
#     home_screen = HomeScreen(root)

#     # Start the Tkinter event loop
#     root.mainloop()

# # Check if the script is being run directly (not imported as a module)
# if __name__ == "__main__":
#     # If so, call the main function
#     main()

# import tkinter as tk

# my_font = ('Helvetica', 16)
# root = tk.Tk()
# button = tk.Button(root, text="Play Now").pack()
# button = tk.Button(root, text="Play Now", font=my_font).pack()
# root.mainloop()
