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
            "game_window_difficulty_2": "1313x820+2039+248",
            "game_window_difficulty_1": "985x656+2039+248",
            "game_window_difficulty_0": "656x493+2039+248",
            "settings_window": "1277x618+114+82",
            "end_game_window": "499x334+2647+468",
            "rows": 5,
            "cols": 8,
            "font_name": "Helvetica",
            "font_size": 25,
            "game_dificulty": 2,
            "on_hover_reveal_card_ms": 800,
            "difficulty_0": [
            ],
            "difficulty_1": [
            ],
            "difficulty_2": [
            ]
        }
        self.save_configs()