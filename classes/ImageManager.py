from PIL import Image, ImageTk

def right_format_and_size(path):
    with Image.open(path) as img:
        aspect_ratio = img.width / img.height
        if aspect_ratio > 1:
            new_width = 160
            new_height = round(new_width / aspect_ratio)
        else:
            new_height = 160
            new_width = round(new_height * aspect_ratio)
        pil_image = img.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(pil_image), pil_image  # Modify this line

def tint_card_image(pil_image):
    # print('debug', pil_image.size)
    tint = Image.new('RGBA', pil_image.size, (67, 163, 91, 128))
    return ImageTk.PhotoImage(Image.alpha_composite(pil_image, tint))
