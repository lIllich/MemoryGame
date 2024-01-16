def check_window_position(root):
    # Update window and wait for all tasks to complete
    root.update_idletasks()

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Get window width, height, and position
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    window_x = root.winfo_x()
    window_y = root.winfo_y()

    # DEBUG
    # print(screen_height, screen_width)
    # print(window_x, window_y)
    # print(window_height, window_width)

    # Check if window is off screen
    if window_x + window_width > screen_width or window_y + window_height > screen_height:
        # Reset window position
        root.geometry("+10+10")