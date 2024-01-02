import tkinter as tk

class SettingsWindow:
    def __init__(self, cm):
        self.cm = cm
        self.setting_window = tk.Toplevel()
        self.setting_window.title("Settings - MemoryGame")
        self.setting_window.geometry(self.cm.configs["settings_window"])
        self.setting_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)
        tk.Label(self.setting_window, text="Settings will be implemented later").pack()

    def save_and_exit(self):
        self.cm.configs["settings_window"] = self.setting_window.geometry()
        self.cm.save_configs()
        self.setting_window.destroy()