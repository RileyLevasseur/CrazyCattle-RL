# This file will capture and perform actions in the game - essentially a gym environment.

import subprocess
import pygetwindow as gw
import time

def step(action):
    pass

def reset():
    exe_path = "bin\\CrazyCattle3D.exe"
    window_title = "CrazyCattle3D (DEBUG)"

    window_width = 800
    window_height = 600

    # Close the window if open
    open_window = gw.getWindowsWithTitle(window_title)
    if open_window:
        print(f"Closing {open_window[0].title}")
        open_window[0].close()
        time.sleep(0.5)

    # Open the application using subprocess
    print(f"Launching {exe_path}")
    process = subprocess.Popen([exe_path])
    time.sleep(0.5)

    # Find the application
    open_window = gw.getWindowsWithTitle(window_title)
    while(len(open_window) == 0):
        time.sleep(0.5) # Account for slow launch if necessary
        open_window = gw.getWindowsWithTitle(window_title)
    window = open_window[0]
    print(f"Found Application: {window.title}")

    # Move the application to the front if minimized
    if window.isMinimized:
        window.restore()
    window.activate()
    
    # Move the application to the top left
    print("Moving window to the top left of the screen.")
    window.moveTo(0,0)

    # Resize the window
    print(f"Resizing window to {window_width}x{window_height}")
    window.resizeTo(window_width, window_height)

    while True:
        time.sleep(10)
