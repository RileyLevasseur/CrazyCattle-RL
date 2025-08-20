# This file will capture and perform actions in the game - essentially a gym environment.

# From what I was able to find, pywin32 is the best library for sending actions to the .exe file.
# Rather than simulating key presses, it sends actions directly to the window.

import subprocess
import pygetwindow as gw
import time
import pydirectinput

def step(forward_or_back, left_or_right, duration = 0.05):
    # The executable uses a framework that is incompatible with Win32 controls, so pyautogui it is
    # Update: pyautogui doesn't work either, but pydirectinput does

    forward_or_back_key = ''
    left_or_right_key = ''

    match forward_or_back:
        case "forward":
            forward_or_back_key = 'w'
        case "back":
            forward_or_back_key = 's'

    match left_or_right:
        case "left":
            left_or_right_key = 'a'
        case "right":
            left_or_right_key = 'd'

    # Ensure that the correct window is in focus
    window = gw.getWindowsWithTitle("CrazyCattle3D (DEBUG)")[0]
    if not window.isActive:
        window.activate()
    time.sleep(0.5)

    if len(forward_or_back_key) > 0:
        print(f"Pressing {forward_or_back_key} for {duration} seconds")
        pydirectinput.keyDown(forward_or_back_key)
    if len(left_or_right_key) > 0:
        print(f"Pressing {left_or_right_key} for {duration} seconds")
    
    time.sleep(duration)
    pydirectinput.keyUp(forward_or_back_key)
    pydirectinput.keyUp(left_or_right_key)

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

    # Select "New Game"
    print('Clicking "New Game"')
    pydirectinput.click(x = 335, y = 395)
    time.sleep(1)

    # Select "Ireland"
    print('Clicking "Ireland"')
    pydirectinput.click(x= 75, y = 285)
    time.sleep(5) # May take longer to load on certain devices

if __name__ == "__main__":
    reset()
    step("forward", 3)
    step("back", 3)
    step("right", 3)
    step("left", 3)