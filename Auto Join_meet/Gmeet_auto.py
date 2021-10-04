import pyautogui
import time
import webbrowser
import  schedule
def join_gmeet():
    webbrowser.open("https://meet.google.com/ucg-dtgh-ngd")
    time.sleep(8)
    pyautogui.hotkey("ctrl", "d")
    pyautogui.hotkey("ctrl", "e")
    time.sleep(1)
    pyautogui.click(1348, 594)
schedule.every().thursday.at("22:00").do(join_gmeet)
while True:
    schedule.run_pending()
    time.sleep(10)
