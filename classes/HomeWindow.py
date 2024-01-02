import tkinter as tk
from classes.SettingsWindow import SettingsWindow
from classes.GameWindow import GameWindow
from classes.EndGameWindow import EndGameWindow

class HomeWindow:
    def __init__(self, cm):
        self.home_window = tk.Tk()
        self.cm = cm

        self.home_window.title("Home - MemoryGame")
        self.home_window.geometry(self.cm.configs["home_window"])
        self.home_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        tk.Button(self.home_window, text="Igraj", command=self.play_now).pack()
        tk.Button(self.home_window, text="Postavke", command=self.open_settings).pack()
        tk.Button(self.home_window, text="Izlaz", command=self.save_and_exit).pack()
        self.home_window.mainloop()

    def save_and_exit(self):
        self.cm.configs["home_window"] = self.home_window.geometry()
        self.cm.save_configs()
        self.home_window.quit()

    def play_now(self):
        self.cm.configs["home_window"] = self.home_window.geometry()
        self.cm.save_configs()
        self.home_window.destroy()
        while True:
            gw = GameWindow(self.cm)
            elapsed_time = gw.run_game()
            egw = EndGameWindow(self.cm, elapsed_time)
            if egw.button_pressed != 0:
                break

    def open_settings(self):
        self.cm.configs["home_window"] = self.home_window.geometry()
        self.cm.save_configs()
        SettingsWindow(self.cm)
