import os
import json

class ConfigManager:
    def __init__(self, url):
        self.url = url
        self.configs = None

    def load_configs(self):
        if os.path.exists(self.url):
            with open(self.url, 'r') as f:
                self.configs = json.load(f)
        else:
            self.new_config_file()

    def save_configs(self):
        with open(self.url, 'w') as f:
            json.dump(self.configs, f)
            

    def new_config_file(self):
        self.configs = {
            "home_window": "600x300",
            "game_window": "939x511",
            "settings_window": "1277x618",
            "end_game_window": "489x384",
            "rows": 4,
            "cols": 3,
            "font_name": "Helvetica",
            "font_size": 25,
            "game_dificulty": 1,
            "category": 1,
            "cell_size": 160,
            "img_size": 160,
            "on_hover_reveal_card_ms": 500,
            "difficulty_0": [],
            "difficulty_1": [],
            "difficulty_2": []
        }
        self.save_configs()