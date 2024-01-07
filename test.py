import tkinter as tk
from classes.CategoryManager import CategoryManager
from classes.ConfigManager import ConfigManager
from classes.Card import Card

import numpy as np
import random
import string
import time
from PIL import Image, ImageTk 

class GameWindow:
    def __init__(self, cm):
        self.cm = cm
        self.category_manager = CategoryManager("categories.json")
        self.category_manager.load_categories()

        self.game_window = tk.Tk()
        self.game_window.title("Game - MemoryGame")
        self.game_window.geometry(self.cm.configs["game_window"])
        self.game_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)
        self.buttons = []
        self.first = None
        self.second = None
        self.rows = None
        self.cols = None
        self.letters = []
        self.end_time = None
        self.after_id = None

        self.set_grid_params()
        self.create_list()
        # self.create_button_grid()
        self.create_canvas_grid()

    def set_grid_params(self):
        if self.cm.configs["game_dificulty"] == 1:
            self.cm.configs["rows"] = self.rows = 4
            self.cm.configs["cols"] = self.cols = 6
        elif self.cm.configs["game_dificulty"] == 2:
            self.cm.configs["rows"] = self.rows = 5
            self.cm.configs["cols"] = self.cols = 8
        else:
            self.cm.configs["rows"] = self.rows = 2
            self.cm.configs["cols"] = self.cols = 2
        self.cm.save_configs()

    def create_list(self):
        id = 0
        for category in self.category_manager.category['category']:
            if category['iterate'] == 'single_string':
                for card in category['cards']:
                    self.letters.append((Card(id, 'string', card), Card(id, 'string', card)))
                    id += 1
            elif category['iterate'] == 'double_string':
                for card in category['cards']:
                    self.letters.append((Card(id, 'string', card["value1"]), Card(id, 'string', card["value2"])))
                    id += 1
            elif category['iterate'] == 'name_and_image':
                for card in category['cards']:
                    self.letters.append((Card(id, 'string', card["name"]), Card(id, 'img_path', card["img"])))
                    id += 1

        random.shuffle(self.letters)
        self.letters = self.letters[: self.rows * self.cols //2]
        self.letters = [x for tuple in self.letters for x in tuple]
        random.shuffle(self.letters)


    def create_button_grid(self):
        for i in range(self.rows):
            self.game_window.grid_rowconfigure(i, weight=2)
            row = []
            for j in range(self.cols):
                self.game_window.grid_columnconfigure(j, weight=2)
                button = tk.Button(self.game_window, text='', image='', width=0, borderwidth=1, highlightthickness=0, font=(self.cm.configs["font_name"], self.cm.configs["font_size"]))
                button.grid(row=i, column=j, sticky='nsew')
                button.bind('<Enter>', lambda event, i=i, j=j: self.hover(i, j))
                button.bind('<Leave>', lambda event: self.cancel_hover())
                row.append(button)
            self.buttons.append(row)

    def create_canvas_grid(self):
        self.cell_size = 160 #todo prebaciti u config 
        self.canvases = [[None]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                canvas = tk.Canvas(self.game_window, width=self.cell_size, height=self.cell_size)
                canvas.grid(row=i, column=j)
                cell = canvas.create_rectangle(0, 0, self.cell_size, self.cell_size, fill='white')
                canvas.tag_bind(cell, "<Enter>", lambda event, i=i, j=j: self.hover(i, j))
                canvas.tag_bind(cell, "<Leave>", lambda event: self.cancel_hover())
                self.canvases[i][j] = canvas

    def hover(self, i, j):
        self.hover_id = self.game_window.after(self.cm.configs["on_hover_reveal_card_ms"], self.select_card, i, j)

    def cancel_hover(self):
        self.game_window.after_cancel(self.hover_id)

    def select_card(self, i, j):
        self.game_window.update_idletasks() # chat napisao: Note that you need to call update_idletasks() before getting the dimensions to ensure that any pending resize operations are carried out and you get the correct dimensions.
        if self.first is None:
            self.first = (i, j)
            if self.letters[i * self.cols + j].type == "string":
                self.canvases[i][j].itemconfig(tk.ALL, text=self.letters[i * self.cols + j].data)
            else:
                self.canvases[i][j].itemconfig(tk.ALL, image=self.letters[i * self.cols + j].data)
        elif self.second is None:
            self.second = (i, j)
            if self.letters[i * self.cols + j].type == "string":
                self.canvases[i][j].itemconfig(tk.ALL, text=self.letters[i * self.cols + j].data)
            else:
                self.canvases[i][j].itemconfig(tk.ALL, image=self.letters[i * self.cols + j].data)
            self.game_window.after(self.cm.configs["on_hover_reveal_card_ms"], self.check_match)

    def check_match(self):
        i1, j1 = self.first
        i2, j2 = self.second
        if self.letters[i1 * self.cols + j1].id != self.letters[i2 * self.cols + j2].id:
            self.canvases[i1][j1].itemconfig(tk.ALL, text='')
            self.canvases[i1][j1].itemconfig(tk.ALL, image='')
            self.canvases[i2][j2].itemconfig(tk.ALL, text='')
            self.canvases[i2][j2].itemconfig(tk.ALL, image='')
        else:
            self.canvases[i1][j1].config(state='disabled', bg=self.from_rgb((67, 163, 91)), disabledforeground="white")
            self.canvases[i2][j2].config(state='disabled', bg=self.from_rgb((67, 163, 91)), disabledforeground="white")
        self.first = self.second = None
        if all(canvas['state'] == 'disabled' for row in self.canvases for canvas in row):
            self.end_time = time.time()
            self.after_id = self.game_window.after(1000, self.destroy)  # Store the ID

    def destroy(self):
        self.cm.configs["game_window"] = self.game_window.geometry()
        self.cm.save_configs()
        if self.after_id:  # Check if after_id exists
            self.game_window.after_cancel(self.after_id)  # Cancel the callback
        self.game_window.destroy()

    def save_and_exit(self):
        self.cm.configs["game_window"] = self.game_window.geometry()
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

cm = ConfigManager('config.json')
cm.load_configs()
gw = GameWindow(cm)
gw.run_game()