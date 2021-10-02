import serial
import pyautogui
import time
ser=serial.Serial('COM6',9600)
dist=100
def ss():
    pyautogui.hotkey("win","prtsc")
    time.sleep(0.2)
while True:
    distance=ser.readline().strip()
    dist=int(float(distance.decode()))
    print(dist)
    if dist < 10 :
        ss()

