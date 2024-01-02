import tkinter as tk

class EndGameWindow:
    def __init__(self, cm, elapsed_time):
        self.cm =  cm
        self.end_game = tk.Tk()
        self.elapsed_time = elapsed_time
        self.button_pressed = None
        self.end_game.geometry(self.cm.configs["end_game_window"])
        self.end_game.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        if elapsed_time is None:
            tk.Label(self.end_game, text=f"Igra je prekinuta").pack()
        else:   
            tk.Label(self.end_game, text=f"Rezultat: {self.elapsed_time:.4f} sekunde").pack()

        tk.Button(self.end_game, text="Igraj ponovno", command=self.play_again).pack()
        tk.Button(self.end_game, text="Izlaz", command=self.exit_game).pack()
        
        self.end_game.mainloop()

    def play_again(self):
        self.button_pressed = 0
        self.cm.configs["end_game_window"] = self.end_game.geometry()
        self.cm.save_configs()
        self.end_game.destroy()

    def exit_game(self):
        self.button_pressed = 1
        self.cm.configs["end_game_window"] = self.end_game.geometry()
        self.cm.save_configs()
        self.end_game.destroy()

    def save_and_exit(self):
        self.button_pressed = -1
        self.cm.configs["end_game_window"] = self.end_game.geometry()
        self.cm.save_configs()
        self.end_game.destroy()