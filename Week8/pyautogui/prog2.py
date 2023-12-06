# Import the necessary modules
import pyautogui
import time

# Define a function to automate GUI actions
def auto_gui_fun():
    # Move the mouse cursor to the coordinates (500, 500) over a duration of 1 second
    pyautogui.moveTo(500, 500, duration=1) 
    # Simulate a mouse click
    pyautogui.click()
    # Type the string "#Hello, World"
    pyautogui.typewrite("#Hello, World")
    # Pause the program for 2 seconds
    time.sleep(2) 
    # Take a screenshot and save it as "pyautogui/screenshot.png"
    pyautogui.screenshot("pyautogui/screenshot.png")
    # Move the mouse cursor to the coordinates (500, 500) over a duration of 1 second
    pyautogui.moveTo(500, 500, duration=1)
    # Scroll the mouse wheel up by 1 step
    pyautogui.scroll(1)
    # Move the mouse cursor to the coordinates (0, 0) over a duration of 1 second
    pyautogui.moveTo(0, 0, duration=1)
    # Simulate a mouse click
    pyautogui.click()

if __name__ == "__main__":
    # Pause the program for 5 seconds
    time.sleep(5)
    # Call the auto_gui_fun function to perform GUI automation
    auto_gui_fun()
    # Display an alert dialog with the given text and title, and an "OK" button
    pyautogui.alert(text="Alert Function Completed", title="ALERT", button="OK")
