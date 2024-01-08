from classes.ImageManager import right_format_and_size, tint_card_image

class Card:
    def __init__(self, id, type, data):
        self.id = id
        self.type = type
        self.data = data
        
        self.load_picture()

    def load_picture(self):
        if self.type == 'img_path':
            self.data = right_format_and_size(self.data)

    def tint_picture(self):
        if self.type == 'img_path':
            self.data = tint_card_image(self.data)