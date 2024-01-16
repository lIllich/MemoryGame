import tkinter as tk
from classes.SettingsWindow import SettingsWindow
from classes.GameWindow import GameWindow
from classes.EndGameWindow import EndGameWindow
from classes.FontManager import FontManager as font
from classes.WindowManager import check_window_position

class HomeWindow:
    def __init__(self, cm):
        self.home_window = tk.Tk()
        self.cm = cm

        self.home_window.title("Home - MemoryGame")
        self.home_window.resizable(False, False)
        self.home_window.geometry(self.cm.configs["home_window"])
        check_window_position(self.home_window)
        self.home_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)
        check_window_position(self.home_window)
        self.hw_ret_value = 0

        l_title = tk.Label(self.home_window, text="MemoryGame", font=font.title_text)
        b_play = tk.Button(self.home_window, text="Igraj", font=font.normal_text, command=self.play_now)
        b_settings = tk.Button(self.home_window, text="Postavke", font=font.normal_text, command=self.open_settings)
        b_exit = tk.Button(self.home_window, text="Izlaz", font=font.normal_text, command=self.save_and_exit)

        l_title.place(x=200, y=35)
        b_play.place(x=80, y=100, width=200, height=50)
        b_settings.place(x=80, y=155, width=200, height=50)
        b_exit.place(x=80, y=210, width=200, height=50)

        l_razina = tk.Label(self.home_window, text="Razina:", font=font.subtitle_text)
        l_razina.place(x=350, y=115)
        # Create a StringVar to hold the value of the radio buttons
        self.game_difficulty = tk.IntVar(value=1)

        # Create the radio buttons
        radio1 = tk.Radiobutton(self.home_window, text='Jednostavno', font=font.normal_text, value=0, variable=self.game_difficulty)
        radio2 = tk.Radiobutton(self.home_window, text='Normalno', font=font.normal_text, value=1, variable=self.game_difficulty)
        radio3 = tk.Radiobutton(self.home_window, text='Teško', font=font.normal_text, value=2, variable=self.game_difficulty)

        radio1.place(x=370, y=150)
        radio2.place(x=370, y=185)
        radio3.place(x=370, y=220)
    
    def show(self):
        self.home_window.mainloop()
        return self.hw_ret_value

    def save_and_exit(self):
        self.cm.configs["home_window"] = self.home_window.geometry()
        self.cm.configs["game_dificulty"] = self.game_difficulty.get()
        self.cm.save_configs()
        self.home_window.quit()

    def play_now(self):
        self.cm.configs["home_window"] = self.home_window.geometry()
        self.cm.configs["game_dificulty"] = self.game_difficulty.get()
        self.cm.save_configs()
        self.home_window.destroy()
        while True:
            gw = GameWindow(self.cm)
            elapsed_time = gw.run_game()
            egw = EndGameWindow(self.cm, elapsed_time)
            if egw.button_pressed == 1:
                self.hw_ret_value = 1
                break
            elif egw.button_pressed == -1:
                break

    def open_settings(self):
        self.cm.configs["home_window"] = self.home_window.geometry()
        self.cm.configs["game_dificulty"] = self.game_difficulty.get()
        self.cm.save_configs()
        SettingsWindow(self.cm)
