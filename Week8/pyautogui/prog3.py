import pyautogui
import time

def automate_keyboard():
    pyautogui.screenshot("pyautogui/butterfly.png")
    img = pyautogui.screenshot(region=(0,0,400,300))
    pyautogui.write("Hello World ! This is Advance python Course", interval=0.2)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("ctrl", "v")

if __name__ == "__main__":
    time.sleep(5)
    automate_keyboard()
    pyautogui.alert(text="Python alert",title="your job done", button="OK")