import tkinter as tk
from classes.WindowManager import check_window_position

class SettingsWindow:
    def __init__(self, cm):
        self.cm = cm
        self.setting_window = tk.Toplevel()
        self.setting_window.title("Settings - MemoryGame")
        self.setting_window.resizable(False, False)
        self.setting_window.geometry(self.cm.configs["settings_window"])
        check_window_position(self.setting_window)
        self.setting_window.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        # Create a label to display the value
        self.label = tk.Label(self.setting_window, text="Brzina označavanja kartice", font=("Arial", 20))
        self.label.pack()

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.setting_window)
        button_frame.pack()

        # Create a button to decrement the value
        self.decrement_button = tk.Button(button_frame, text="-", font=("Arial", 20), width=3, height=1, command=self.decrement)
        self.decrement_button.pack(side="left", padx=10)

        # Create a label to display the value
        self.value_reveal_ms = self.cm.configs["on_hover_reveal_card_ms"]
        if self.value_reveal_ms > 1500:
            self.value_reveal_ms = 1500
        elif self.value_reveal_ms < 300:
            self.value_reveal_ms = 300
        self.value_label = tk.Label(button_frame, text=f"{self.value_reveal_ms} ms", font=("Arial", 20))
        self.value_label.pack(side="left")

        # Create a button to increment the value
        self.increment_button = tk.Button(button_frame, text="+", font=("Arial", 20), width=3, height=1, command=self.increment)
        self.increment_button.pack(side="left", padx=10)

        # Move all components away from the edge of the window
        self.label.pack(pady=10)
        button_frame.pack(pady=10)

        # Spremi i izađi button
        self.save_button = tk.Button(self.setting_window, text="Spremi i Izađi", font=("Arial", 14), width=15, height=2, command=self.save_and_exit)
        self.save_button.pack(side="bottom", padx=10, pady=10, anchor="e")

        self.cell_size_label = tk.Label(self.setting_window, text="Veličina kartice", font=("Arial", 20))
        self.cell_size_label.pack()
        self.cell_size_button_frame = tk.Frame(self.setting_window)
        self.cell_size_button_frame.pack()
        self.decrement_cell_size_button = tk.Button(self.cell_size_button_frame, text="-", font=("Arial", 20), width=3, height=1, command=self.decrement_cell_size)
        self.decrement_cell_size_button.pack(side="left", padx=10)
        self.cell_size_value = self.cm.configs["cell_size"]
        self.cell_size_value_label = tk.Label(self.cell_size_button_frame, text=f"{self.cell_size_value}", font=("Arial", 20))
        self.cell_size_value_label.pack(side="left")
        self.increment_cell_size_button = tk.Button(self.cell_size_button_frame, text="+", font=("Arial", 20), width=3, height=1, command=self.increment_cell_size)
        self.increment_cell_size_button.pack(side="left", padx=10)

        # Additional code for img_size
        self.img_size_label = tk.Label(self.setting_window, text="Veličina slike", font=("Arial", 20))
        self.img_size_label.pack()
        self.img_size_button_frame = tk.Frame(self.setting_window)
        self.img_size_button_frame.pack()
        self.decrement_img_size_button = tk.Button(self.img_size_button_frame, text="-", font=("Arial", 20), width=3, height=1, command=self.decrement_img_size)
        self.decrement_img_size_button.pack(side="left", padx=10)
        self.img_size_value = self.cm.configs["img_size"]
        self.img_size_value_label = tk.Label(self.img_size_button_frame, text=f"{self.img_size_value}", font=("Arial", 20))
        self.img_size_value_label.pack(side="left")
        self.increment_img_size_button = tk.Button(self.img_size_button_frame, text="+", font=("Arial", 20), width=3, height=1, command=self.increment_img_size)
        self.increment_img_size_button.pack(side="left", padx=10)

    def increment(self):
        if self.value_reveal_ms < 1500:
            self.value_reveal_ms += 50
        self.value_label.config(text=f"{self.value_reveal_ms} ms")

    def decrement(self):
        if self.value_reveal_ms > 300:
            self.value_reveal_ms -= 50
        self.value_label.config(text=f"{self.value_reveal_ms} ms")
    
    def increment_cell_size(self):
        if self.cell_size_value < 180:
            self.cell_size_value += 1
        self.cell_size_value_label.config(text=f"{self.cell_size_value}")

    def decrement_cell_size(self):
        if self.cell_size_value > 140:
            self.cell_size_value -= 1
        self.cell_size_value_label.config(text=f"{self.cell_size_value}")

    # Additional methods for img_size
    def increment_img_size(self):
        if self.img_size_value < 180:
            self.img_size_value += 1
        self.img_size_value_label.config(text=f"{self.img_size_value}")

    def decrement_img_size(self):
        if self.img_size_value > 140:
            self.img_size_value -= 1
        self.img_size_value_label.config(text=f"{self.img_size_value}")

    def save_and_exit(self):
        self.cm.configs["settings_window"] = self.setting_window.geometry()
        self.cm.configs["on_hover_reveal_card_ms"] = self.value_reveal_ms
        self.cm.configs["cell_size"] = self.cell_size_value
        self.cm.configs["img_size"] = self.img_size_value
        self.cm.save_configs()
        self.setting_window.destroy()
