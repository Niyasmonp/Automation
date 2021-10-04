import pyautogui
import time
import webbrowser
import  schedule
obs= "start /d \"C:\Program Files\obs-studio\\bin\\64bit\" obs64.exe --startrecording"
mon_2016="https://iitmadras.webex.com/webappng/sites/iitmadras/meeting/download/db8eb849eb04464690de791b3f63c81a?siteurl=iitmadras&MTID=m1a992df7d279a05a84f8df586ac29c39"
tue_2016="https://iitmadras.webex.com/webappng/sites/iitmadras/meeting/download/def853f9105b4a02bfaff8308bbe9410?siteurl=iitmadras&MTID=m3ffc93ea342be1d701764b403d72a818"
EE2025="https://meet.google.com/ukj-tnov-zdc?pli=1&authuser=1"
EE2015="https://meet.google.com/abv-wxup-qst?authuser=1&hl=en"
EE3110="https://iitmadras.webex.com/webappng/sites/iitmadras/meeting/download/d00a63a3e8144e3391b1734727211d13?siteurl=iitmadras&MTID=m5a8494adfd0e1a54ba6e33934515a60d"
def join_gmeet(url):
    webbrowser.open(url)
    time.sleep(30)
    pyautogui.hotkey("ctrl", "d")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "e")
    time.sleep(1)
    pyautogui.click(1348, 594)

def join_webex(url):
    webbrowser.open(url)
    time.sleep(20)
    pyautogui.typewrite("EE20B094 Niyas Mon P")
    pyautogui.typewrite(["tab"])
    pyautogui.typewrite(["tab"])
    time.sleep(0.2)
    pyautogui.typewrite("ee20b094@smail.iitm.ac.in")
    time.sleep(0.3)
    pyautogui.typewrite(["enter"])
    time.sleep(5)
    pyautogui.typewrite(["enter"])
    time.sleep(7)
    pyautogui.click(1695,82)

def open_obs(path):
    pyautogui.click(184,1058)
    time.sleep(2)
    pyautogui.typewrite("cmd")
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])
    time.sleep(2)
    pyautogui.typewrite(path)
    time.sleep(0.1)
    pyautogui.typewrite(["enter"])
    time.sleep(10)



def monday():
    schedule.every().monday.at("07:58").do(open_obs,obs)
    schedule.every().monday.at("07:59").do(join_gmeet,EE3110)
    schedule.every().monday.at("08:59").do(join_webex,mon_2016)
    schedule.every().monday.at("10:58").do(open_obs, obs)
    schedule.every().monday.at("10:59").do(join_gmeet,EE2025)

def tuesday():
    schedule.every().tuesday.at("07:58").do(open_obs, obs)
    schedule.every().tuesday.at("07:59").do(join_webex,tue_2016)
    schedule.every().tuesday.at("09:59").do(join_gmeet, EE2025)
    schedule.every().tuesday.at("12:58").do(open_obs, obs)
    schedule.every().tuesday.at("12:59").do(join_webex, EE3110)

def wednesday():
    schedule.every().wednesday.at("08:58").do(open_obs, obs)
    schedule.every().wednesday.at("08:59").do(join_gmeet, EE2025)

def thursday():
    schedule.every().thursday.at("10:58").do(open_obs, obs)
    schedule.every().thursday.at("10:59").do(join_webex, EE3110)
    schedule.every().thursday.at("13:58").do(open_obs, obs)
    schedule.every().thursday.at("13:59").do(join_gmeet, EE2015)

def friday():
    schedule.every().friday.at("09:58").do(open_obs, obs)
    schedule.every().friday.at("09:59").do(join_webex, EE3110)
    schedule.every().friday.at("12:58").do(open_obs, obs)
    schedule.every().friday.at("12:59").do(join_gmeet, EE2015)

monday()
tuesday()
wednesday()
thursday()
friday()
while True:
    schedule.run_pending()
    time.sleep(10)
