import tkinter as tk
from classes.CategoryManager import CategoryManager
from classes.Card import Card

import numpy as np
import random
import time

from classes.WindowManager import check_window_position

class GameWindow:
    def __init__(self, cm):
        self.cm = cm
        self.category_manager = CategoryManager("categories.json")
        
        self.category_manager.load_categories()
        self.game_window = tk.Tk()
        # self.game_window.resizable(False, False)
        self.game_window.title("Game - MemoryGame")
        self.game_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)
        
        self.canvases = []
        self.first = None
        self.second = None
        self.rows = None
        self.cols = None
        self.cards = []
        self.end_time = None
        self.after_id = None

        self.image_item1 = None
        self.image_item2 = None
        self.text_item1 = None
        self.text_item2 = None

        self.set_grid_params()
        self.create_letter_list()
        # self.create_button_grid()
        self.create_canvas_grid()

    def set_grid_params(self):
        if self.cm.configs["game_dificulty"] == 1:
            self.cm.configs["rows"] = self.rows = 4
            self.cm.configs["cols"] = self.cols = 6
            self.game_window.geometry(self.cm.configs["game_window_difficulty_1"])
        elif self.cm.configs["game_dificulty"] == 2:
            self.cm.configs["rows"] = self.rows = 5
            self.cm.configs["cols"] = self.cols = 8
            self.game_window.geometry(self.cm.configs["game_window_difficulty_2"])
        else:
            self.cm.configs["rows"] = self.rows = 3
            self.cm.configs["cols"] = self.cols = 4
            self.game_window.geometry(self.cm.configs["game_window_difficulty_0"])
        check_window_position(self.game_window)
        self.cm.save_configs()

    def create_letter_list(self):
        id = 0
        for category in self.category_manager.category['category']:
            if category['iterate'] == 'single_string':
                for card in category['cards']:
                    self.cards.append((Card(id, 'string', card), Card(id, 'string', card)))
                    id += 1
            elif category['iterate'] == 'double_string':
                for card in category['cards']:
                    self.cards.append((Card(id, 'string', card["value1"]), Card(id, 'string', card["value2"])))
                    id += 1
            elif category['iterate'] == 'name_and_image':
                for card in category['cards']:
                    self.cards.append((Card(id, 'string', card["name"].upper()), Card(id, 'img_path', card["img"])))
                    id += 1

        random.shuffle(self.cards)
        self.cards = self.cards[: self.rows * self.cols //2]
        self.cards = [x for tuple in self.cards for x in tuple]
        random.shuffle(self.cards)

    # * vise ne koristimo
    # def create_button_grid(self):
    #     for i in range(self.rows):
    #         self.game_window.grid_rowconfigure(i, weight=2)
    #         row = []
    #         for j in range(self.cols):
    #             self.game_window.grid_columnconfigure(j, weight=2)
    #             button = tk.Button(self.game_window, text='', image='', width=0, borderwidth=1, highlightthickness=0, font=(self.cm.configs["font_name"], self.cm.configs["font_size"]))
    #             button.grid(row=i, column=j, sticky='nsew')
    #             button.bind('<Enter>', lambda event, i=i, j=j: self.hover(i, j))
    #             button.bind('<Leave>', lambda event: self.cancel_hover())
    #             row.append(button)
    #         self.buttons.append(row)

    def create_canvas_grid(self):
        self.cell_size = 160 #todo prebaciti u config 
        self.canvases = [[None]*self.cols for _ in range(self.rows)]
        self.cells = [[None]*self.cols for _ in range(self.rows)]  # Store the IDs of the cells
        for i in range(self.rows):
            for j in range(self.cols):
                canvas = tk.Canvas(self.game_window, width=self.cell_size, height=self.cell_size, highlightbackground="black", highlightthickness=0)
                canvas.grid(row=i, column=j)
                cell = canvas.create_rectangle(0, 0, self.cell_size, self.cell_size, fill='white')
                canvas.bind("<Enter>", lambda event, i=i, j=j: self.hover(i, j))
                canvas.bind("<Leave>", lambda event: self.cancel_hover())
                self.canvases[i][j] = canvas
                self.cells[i][j] = cell  # Store the ID of the cell


    def hover(self, i, j):
        self.hover_id = self.game_window.after(self.cm.configs["on_hover_reveal_card_ms"], self.select_card, i, j)

    def cancel_hover(self):
        self.game_window.after_cancel(self.hover_id)

    def select_card(self, i, j):
        # self.game_window.update_idletasks()
        if self.first is None:
            self.first = (i, j)
            if self.cards[i * self.cols + j].type == "string":
                self.text_item1 = self.canvases[i][j].create_text(80, 80, text=self.cards[i * self.cols + j].data, anchor='center', font=("Arial", 20))
            else:
                self.image_item1 = self.canvases[i][j].create_image(80, 80, image=self.cards[i * self.cols + j].data, anchor='center')
        elif self.second is None:
            self.second = (i, j)
            if self.cards[i * self.cols + j].type == "string":
                self.text_item2 = self.canvases[i][j].create_text(80, 80, text=self.cards[i * self.cols + j].data, anchor='center', font=("Arial", 20))
            else:
                self.image_item2 = self.canvases[i][j].create_image(80, 80, image=self.cards[i * self.cols + j].data, anchor='center')
            self.game_window.after(self.cm.configs["on_hover_reveal_card_ms"], self.check_match)

    def check_match(self):
        i1, j1 = self.first
        i2, j2 = self.second
        if self.cards[i1 * self.cols + j1].id == self.cards[i2 * self.cols + j2].id:
            self.canvases[i1][j1].itemconfig(self.cells[i1][j1], fill=self.from_rgb((67, 163, 91)))  # Change the color of the cell
            self.canvases[i2][j2].itemconfig(self.cells[i2][j2], fill=self.from_rgb((67, 163, 91)))  # Change the color of the cell
            self.canvases[i1][j1].unbind("<Enter>")
            self.canvases[i1][j1].unbind("<Leave>")
            self.canvases[i2][j2].unbind("<Enter>")
            self.canvases[i2][j2].unbind("<Leave>")
            for item in self.canvases[i1][j1].find_all():
                if self.canvases[i1][j1].type(item) == 'image':
                    self.cards[i1 * self.cols + j1].tint_picture()
                    self.canvases[i1][j1].create_image(80, 80, image=self.cards[i1 * self.cols + j1].data, anchor='center')
            for item in self.canvases[i2][j2].find_all():
                if self.canvases[i2][j2].type(item) == 'image':
                    self.cards[i2 * self.cols + j2].tint_picture()
                    self.canvases[i2][j2].create_image(80, 80, image=self.cards[i2 * self.cols + j2].data, anchor='center')
            if all(self.canvases[i][j].itemcget(self.cells[i][j], 'fill') == self.from_rgb((67, 163, 91)) for i in range(self.rows) for j in range(self.cols)):
                self.end_time = time.time()
                self.after_id = self.game_window.after(1000, self.destroy)  # Store the ID
        else:
            if self.text_item1 is not None:
                self.canvases[i1][j1].delete(self.text_item1)
            if self.text_item2 is not None:
                self.canvases[i2][j2].delete(self.text_item2)
            if self.image_item1 is not None:
                self.canvases[i1][j1].delete(self.image_item1)
            if self.image_item2 is not None:
                self.canvases[i2][j2].delete(self.image_item2)
        self.first = self.second = self.text_item1 = self.text_item2 = self.image_item1 = self.image_item2 = None

    def destroy(self):
        if self.cm.configs["game_dificulty"] == 1:
            self.cm.configs["game_window_difficulty_1"] = self.game_window.geometry()
        elif self.cm.configs["game_dificulty"] == 2:
            self.cm.configs["game_window_difficulty_2"] = self.game_window.geometry()
        else:
            self.cm.configs["game_window_difficulty_0"] = self.game_window.geometry()
        self.cm.save_configs()
        if self.after_id:  # Check if after_id exists
            self.game_window.after_cancel(self.after_id)  # Cancel the callback
        self.game_window.destroy()

    def save_and_exit(self):
        if self.cm.configs["game_dificulty"] == 1:
            self.cm.configs["game_window_difficulty_1"] = self.game_window.geometry()
        elif self.cm.configs["game_dificulty"] == 2:
            self.cm.configs["game_window_difficulty_2"] = self.game_window.geometry()
        else:
            self.cm.configs["game_window_difficulty_0"] = self.game_window.geometry()
        self.cm.save_configs()
        if self.after_id:  # Check if after_id exists
            self.game_window.after_cancel(self.after_id)  # Cancel the callback
        self.destroy()

    def run_game(self):
        self.start_time = time.time()
        self.game_window.mainloop()
        if self.end_time is not None:
            return self.end_time - self.start_time

    def from_rgb(self, rgb):
        return '#%02x%02x%02x' % rgb
