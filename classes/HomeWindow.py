import tkinter as tk
from classes.SettingsWindow import SettingsWindow
from classes.GameWindow import GameWindow
from classes.EndGameWindow import EndGameWindow

class HomeWindow:
    def __init__(self, cm):
        self.home_window = tk.Tk()
        self.cm = cm

        self.home_window.title("Home - MemoryGame")
        self.home_window.resizable(False, False)
        self.home_window.geometry(self.cm.configs["home_window"])
        self.home_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        l_title = tk.Label(self.home_window, text="MemoryGame", font=("", 20, 'bold'))
        b_play = tk.Button(self.home_window, text="Igraj", font=("", 14), command=self.play_now)
        b_settings = tk.Button(self.home_window, text="Postavke", font=("", 14), command=self.open_settings)
        b_exit = tk.Button(self.home_window, text="Izlaz", font=("", 14), command=self.save_and_exit)

        l_title.place(x=200, y=35)
        b_play.place(x=30, y=100, width=200, height=50)
        b_settings.place(x=30, y=155, width=200, height=50)
        b_exit.place(x=30, y=210, width=200, height=50)

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
