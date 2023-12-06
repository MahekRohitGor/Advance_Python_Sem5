import pyautogui
import time

def automating_editor():
    pyautogui.press("win")
    pyautogui.write("Notepad")
    pyautogui.press("enter")

    time.sleep(2)

    text_to_type = "Hello World ! I am Mahek"
    pyautogui.write(text_to_type, interval=0.1)

    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    pyautogui.write("pyautogui.txt")
    pyautogui.press("enter")

if __name__ == "__main__":
    time.sleep(5)
    automating_editor()
    pyautogui.alert(text="Python alert", title="Your job is done", button="OK")
