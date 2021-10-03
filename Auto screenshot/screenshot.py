import serial    #library for serail communication
import pyautogui #library to automate user interface
import time
ser=serial.Serial('COM6',9600)
dist=100
def ss():  #function to take screenshot
    pyautogui.hotkey("win","prtsc") 
    time.sleep(0.2)
while True:
    distance=ser.readline().strip() #Reading the input from serial port
    dist=int(float(distance.decode())) #.decode() to conver 'byte' into 'str'
    print(dist)
    if dist < 10 :
        ss()
