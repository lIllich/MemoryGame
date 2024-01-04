from PIL import Image, ImageTk

def right_format_and_size(path, width, height):
    return ImageTk.PhotoImage(Image.open(path).resize((width, height), Image.LANCZOS))