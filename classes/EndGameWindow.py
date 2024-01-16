# import tkinter as tk

# class EndGameWindow:
#     def __init__(self, cm, elapsed_time):
#         self.cm =  cm
#         self.end_game = tk.Tk()
#         self.end_game.resizable(False, False)
#         self.elapsed_time = elapsed_time
#         self.difficulty_level = self.cm.configs["game_dificulty"]
#         self.button_pressed = None
#         self.end_game.geometry(self.cm.configs["end_game_window"])
#         self.end_game.protocol("WM_DELETE_WINDOW", self.save_and_exit)

#         if self.elapsed_time is None:
#             tk.Label(self.end_game, text=f"Igra je prekinuta").pack()
#         else:   
#             tk.Label(self.end_game, text=f"Tvoj rezultat: {self.elapsed_time:.4f} sekunde").pack()
#             self.update_score_table()

#         self.show_score_table()

#         # Create a frame for the buttons
#         button_frame = tk.Frame(self.end_game)
#         button_frame.pack(pady=10)  # Add some padding to move the buttons away from the score table

#         # Create the buttons with the same width
#         tk.Button(button_frame, text="Igraj ponovno", command=self.play_again, width=20).pack(side=tk.LEFT, padx=5)
#         tk.Button(button_frame, text="Izlaz", command=self.exit_game, width=20).pack(side=tk.LEFT, padx=5)
        
#         self.end_game.mainloop()

#     def play_again(self):
#         self.button_pressed = 0
#         self.cm.configs["end_game_window"] = self.end_game.geometry()
#         self.cm.save_configs()
#         self.end_game.destroy()

#     def exit_game(self):
#         self.button_pressed = 1
#         self.cm.configs["end_game_window"] = self.end_game.geometry()
#         self.cm.save_configs()
#         self.end_game.destroy()

#     def save_and_exit(self):
#         self.button_pressed = -1
#         self.cm.configs["end_game_window"] = self.end_game.geometry()
#         self.cm.save_configs()
#         self.end_game.destroy()

#     def show_score_table(self):
#         scores = self.cm.configs[f"difficulty_{self.difficulty_level}"]
#         scores.sort()

#         tk.Label(self.end_game, text=f"Top 10 najboljih rezultata za razinu '{self.razina_num_to_word(self.difficulty_level)}':").pack()
#         for i, score in enumerate(scores[:10]):
#             if score == self.elapsed_time:
#                 label = tk.Label(self.end_game, text=f"{i+1}. {score:.4f} sekunde (tvoj rezultat)", fg="red")
#                 label.pack()
#             else:
#                 tk.Label(self.end_game, text=f"{i+1}. {score:.4f} sekunde").pack()

#     def update_score_table(self):
#         scores = self.cm.configs[f"difficulty_{self.difficulty_level}"]

#         # Check if the elapsed time is better than the worst score in the top 10
#         if len(scores) < 10 or self.elapsed_time < max(scores):
#             # If it is, add the elapsed time to the score table and sort it
#             scores.append(self.elapsed_time)
#             scores.sort()

#             # Keep only the top 10 scores
#             self.cm.configs[f"difficulty_{self.difficulty_level}"] = scores[:10]

#             # Save the updated scores to the config file
#             self.cm.save_configs()

#     def razina_num_to_word(self, num):
#         if num == 0:
#             return 'Jednostavno'
#         elif num == 1:
#             return 'Normalno'
#         elif num == 2:
#             return 'Teško'
#         else:
#             return 'ERR'

# gore prijasnji kod, dole kod od domagoja, kopirano iz njegove grane da ne moramo mergat

import tkinter as tk
from classes.FontManager import FontManager as font
class EndGameWindow:
    def __init__(self, cm, elapsed_time):
        self.cm = cm
        self.end_game = tk.Tk()
        self.end_game.resizable(False, False)
        self.elapsed_time = elapsed_time
        self.difficulty_level = self.cm.configs["game_dificulty"]
        self.button_pressed = None
        self.end_game.geometry(self.cm.configs["end_game_window"])
        self.end_game.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        if self.elapsed_time is None:
            tk.Label(self.end_game, text=f"Igra je prekinuta").pack()
        else:
            tk.Label(self.end_game, text=f"Tvoj rezultat: {self.elapsed_time:.4f} sekunde", font=font.title_text).pack()
            self.update_score_table()

        self.show_score_table()

        # Create a frame for the buttons
        button_frame = tk.Frame(self.end_game)
        button_frame.pack(pady=10)

        # Create the buttons with the same width
        tk.Button(button_frame, text="Igraj ponovno", command=self.play_again, width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Povratak na početnu", command=self.exit_game, width=20).pack(side=tk.LEFT, padx=5)

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
        self.create_home_window()

    def create_home_window(self):
        # Create a new instance of HomeWindow
        from classes.HomeWindow import HomeWindow  # Import HomeWindow here
        home_window = HomeWindow(self.cm)
        home_window.home_window.mainloop()

    def save_and_exit(self):
        self.button_pressed = -1
        self.cm.configs["end_game_window"] = self.end_game.geometry()
        self.cm.save_configs()
        self.end_game.destroy()

    def show_score_table(self):
        scores = self.cm.configs[f"difficulty_{self.difficulty_level}"]
        scores.sort()

        tk.Label(self.end_game, text=f"Top 10 najboljih rezultata za razinu '{self.razina_num_to_word(self.difficulty_level)}':").pack()
        for i, score in enumerate(scores[:10]):
            if score == self.elapsed_time:
                label = tk.Label(self.end_game, text=f"{i+1}. {score:.4f} sekunde (tvoj rezultat)", fg="red", font=font.title_text)
                label.pack()
            else:
                tk.Label(self.end_game, text=f"{i+1}. {score:.4f} sekunde").pack()

    def update_score_table(self):
        scores = self.cm.configs[f"difficulty_{self.difficulty_level}"]

        # Check if the elapsed time is better than the worst score in the top 10
        if len(scores) < 10 or self.elapsed_time < max(scores):
            # If it is, add the elapsed time to the score table and sort it
            scores.append(self.elapsed_time)
            scores.sort()

            # Keep only the top 10 scores
            self.cm.configs[f"difficulty_{self.difficulty_level}"] = scores[:10]

            # Save the updated scores to the config file
            self.cm.save_configs()

    def razina_num_to_word(self, num):
        if num == 0:
            return 'Jednostavno'
        elif num == 1:
            return 'Normalno'
        elif num == 2:
            return 'Teško'
        else:
            return 'ERR'