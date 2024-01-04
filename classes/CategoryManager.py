import os
import json

class CategoryManager:
    def __init__(self, url):
        self.url = url
        self.category = None

    def load_categories(self):
        if os.path.exists(self.url):
            with open(self.url, 'r', encoding='utf-8') as f:
                self.category = json.load(f)
        # else:
        #     self.new_config_file()

    def save_configs(self):
        with open(self.url, 'w') as f:
            json.dump(self.category, f)
            

    # def _new_config_file(self):
    #     self.configs = {
    #         "home_window": "600x300+2789+414",
    #         "game_window": "939x511+296+145",
    #         "settings_window": "1277x618+131+70",
    #         "end_game_window": "489x384+52+52",
    #         "rows": 4,
    #         "cols": 3,
    #         "font_name": "Helvetica",
    #         "font_size": 25,
    #         "game_dificulty": 1,
    #         "on_hover_reveal_card_ms": 500,
    #         "difficulty_0": [],
    #         "difficulty_1": [],
    #         "difficulty_2": []
    #     }
    #     self.save_configs()