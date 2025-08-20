# This file will capture and perform actions in the game - essentially a gym environment.

# From what I was able to find, pywin32 is the best library for sending actions to the .exe file.
# Rather than simulating key presses, it sends actions directly to the window.

import subprocess
import pygetwindow as gw
import time
import win32gui
import win32api
import win32con

def step(action, duration = 0.05):
    # Find the correct window
    hwnd = win32gui.FindWindow(None, "CrazyCattle3D (DEBUG)")
    win32gui.SetForegroundWindow(hwnd)
    key_code = 0x57

    # Send an event to the window corresponding to the given action
    # Virtual key codes found here: https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

    match action:
        case "back":
            key_code = 0x53
        case "right":
            key_code = 0x44
        case "left":
            key_code = 0x41

    # To simulate a key press, it's required to send a "KEYDOWN" and "KEYUP" function
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key_code, 0)
    time.sleep(duration)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, key_code, 0)

    print(f"Action: {action}\nKey Code: {key_code}\nDuration: {duration} seconds")

def click(x, y, duration = 0.05):
    hwnd = win32gui.FindWindow(None, "CrazyCattle3D (DEBUG)")
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.1)

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0)
    time.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0)

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
    click(335,395)
    time.sleep(1)

    # Select "Ireland"
    print('Clicking "Ireland"')
    click(75,285)
    time.sleep(7) # May take longer to load on certain devices

if __name__ == "__main__":
    reset()
    step("forward", 4)
    step("back", 3)
    step("left", 3)
    step("right", 3)
    