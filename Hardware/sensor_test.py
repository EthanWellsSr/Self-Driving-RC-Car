import serial #loads PySerial library to communicate w/ Arduino
import time #loads time library for delays

arduino = serial.Serial("COM4", 9600) #connects to board in COM4 at 9600 baud rate (coms speed)

time.sleep(2) #waits 2sec

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip() #ReciveData/Conv2Txt/removes "newline"

        print(data)