from classes.ImageManager import right_format_and_size

class Card:
    def __init__(self, id, type, data):
        self.id = id
        self.type = type
        self.data = data
        
        self.load_picture(100, 100)

    def load_picture(self, width, height):
        if self.type == 'img_path':
            self.data = right_format_and_size(self.data, width, height)