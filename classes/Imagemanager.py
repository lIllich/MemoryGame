from PIL import Image, ImageTk

def right_format_and_size(path):
    # Open an image file
    with Image.open(path) as img:
        # Get the aspect ratio of the image
        aspect_ratio = img.width / img.height

        # Calculate new dimensions
        if aspect_ratio > 1:
            # Image is wider than it is tall
            new_width = 160
            new_height = round(new_width / aspect_ratio)
        else:
            # Image is taller than it is wide, or is a square
            new_height = 160
            new_width = round(new_height * aspect_ratio)

        # # Save the resized image
        # img.save('resized_image.png')
        return ImageTk.PhotoImage(Image.open(path).resize((new_width, new_height), Image.LANCZOS))