from classes.ImageManager import right_format_and_size, tint_card_image
from PIL import Image, ImageTk
from classes.ConfigManager import ConfigManager

class Card:
    def __init__(self, id, type, data):
        self.id = id
        self.type = type
        self.data = data
        self.pil_image = None  # Add this line
        
        self.load_picture()

    def load_picture(self):
        if self.type == 'img_path':
            self.data, self.pil_image = right_format_and_size(self.data, self.img_size())  # Modify this line

    def tint_picture(self):
        if self.type == 'img_path' and self.pil_image is not None:  # Modify this line
            self.data = tint_card_image(self.pil_image)  # Modify this line

    def img_size(self):
        config_file = "config.json"
        cm = ConfigManager(config_file)
        cm.load_configs()

        return cm.configs["img_size"]