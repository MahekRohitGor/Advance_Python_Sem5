# Import pyautogui and time
import pyautogui
import time

# Function to automate mouse movement
def automate_mouse():
    # Move the mouse cursor to the coordinates (500, 500) over a duration of 1 second
    pyautogui.moveTo(500,500,duration=1)
    # Simulate a mouse click at the current mouse cursor position
    pyautogui.click()
    # Move the mouse cursor to the coordinates (800, 300) over a duration of 1 second
    pyautogui.moveTo(800,300,duration=1)

if __name__ == "__main__":
    # Pause the program for 5 seconds
    time.sleep(5)
    # Call the automate_mouse() function
    automate_mouse()
    # Get the screen width and height using pyautogui
    screenWidth, screenHeight = pyautogui.size()

    # Print the screen width and height
    print("Screen Width: ", screenWidth)
    print("Screen Height: ", screenHeight)

    #Display an alert dialog with the given text and title, and an "OK" button
    pyautogui.alert(text="Python alert",title="Python alert", button="OK")