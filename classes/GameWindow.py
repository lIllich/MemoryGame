import tkinter as tk
import random
import string
import time

class GameWindow:
    def __init__(self, cm):
        self.cm = cm
        self.game_window = tk.Tk()
        self.game_window.title("Game - MemoryGame")
        self.game_window.geometry(self.cm.configs["game_window"])
        self.game_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)
        self.buttons = []
        self.first = None
        self.second = None
        self.rows = None
        self.cols = None
        self.letters = None
        self.end_time = None
        self.after_id = None        
        self.create_buttons()

    def create_buttons(self):
        if self.cm.configs["game_dificulty"] == 1:
            self.cm.configs["rows"] = self.rows = 4
            self.cm.configs["cols"] = self.cols = 6
        elif self.cm.configs["game_dificulty"] == 2:
            self.cm.configs["rows"] = self.rows = 5
            self.cm.configs["cols"] = self.cols = 8
        else:
            self.cm.configs["rows"] = self.rows = 3
            self.cm.configs["cols"] = self.cols = 4
        
        self.cm.save_configs()
        self.letters = list(string.ascii_uppercase[:self.rows * self.cols // 2]) * 2
        random.shuffle(self.letters)

        for i in range(self.rows):
            self.game_window.grid_rowconfigure(i, weight=2)
            row = []
            for j in range(self.cols):
                self.game_window.grid_columnconfigure(j, weight=2)
                button = tk.Button(self.game_window, text='', width=2, font=(self.cm.configs["font_name"], self.cm.configs["font_size"]))
                button.grid(row=i, column=j, sticky='nsew')
                button.bind('<Enter>', lambda event, i=i, j=j: self.hover(i, j))
                button.bind('<Leave>', lambda event: self.cancel_hover())
                row.append(button)
            self.buttons.append(row)

    def hover(self, i, j):
        self.hover_id = self.game_window.after(self.cm.configs["on_hover_reveal_card_ms"], self.select_card, i, j)

    def cancel_hover(self):
        self.game_window.after_cancel(self.hover_id)

    def select_card(self, i, j):
        if self.first is None:
            self.first = (i, j)
            self.buttons[i][j].config(text=self.letters[i * self.cols + j])
        elif self.second is None:
            self.second = (i, j)
            self.buttons[i][j].config(text=self.letters[i * self.cols + j])
            self.game_window.after(self.cm.configs["on_hover_reveal_card_ms"], self.check_match)

    def check_match(self):
        i1, j1 = self.first
        i2, j2 = self.second
        if self.letters[i1 * self.cols + j1] != self.letters[i2 * self.cols + j2]:
            self.buttons[i1][j1].config(text='')
            self.buttons[i2][j2].config(text='')
        else:
            self.buttons[i1][j1].config(state='disabled', bg=self.from_rgb((67, 163, 91)), disabledforeground="white")
            self.buttons[i2][j2].config(state='disabled', bg=self.from_rgb((67, 163, 91)), disabledforeground="white")
        self.first = self.second = None
        if all(button['state'] == 'disabled' for row in self.buttons for button in row):
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