import pyautogui
import time
import win32gui

def find_window(title):
    def callback(hwnd, extra):
        if title in win32gui.GetWindowText(hwnd):
            extra.append(hwnd)
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows[0] if windows else None

def hold_key_in_window(window_title, key, duration):
    hwnd = find_window(window_title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.keyDown(key)
        time.sleep(duration)
        pyautogui.keyUp(key)
    else:
        print(f"Window with title '{window_title}' not found.")

if __name__ == "__main__":
    window_title = "Untitled - Notepad"  # Change this to the title of the window you want to target
    key = 'a'  # Change this to the key you want to hold down
    duration = 5  # Duration in seconds

    hold_key_in_window(window_title, key, duration)
