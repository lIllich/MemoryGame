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
            "home_window": "600x300+2789+414",
            "game_window": "1536x793+-71+-13",
            "settings_window": "300x200",
            "end_game_window": "300x200+52+52",
            "rows": 4,
            "cols": 3,
            "font_name": "Helvetica",
            "font_size": 25,
            "game_dificulty": 1,
        }
        self.save_configs()