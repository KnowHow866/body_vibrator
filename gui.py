import serial
from tkinter import *
import time

# global variable to sent and set
amplitude = 0

# tkinter setting
tkBoard = Tk()
tkBoard.minsize(width=320, height=170)
tkBoard.config(bg='yellow')
tkBoard.title("GUI for Arduino")

# arduino serial setting
device_port = '/dev/cu.usbserial-AI0443U0'
arduino_serial = serial.Serial(device_port, 9600, timeout=1)
#value = arduino_serial.readline()

mode_is_set = 0
mode = 0


while True:
    if not mode_is_set:
        arduino_serial.write(str.encode(str(mode)))
        read_block = arduino_serial.readline()
        if read_block:
            print(read_block)
            mode_is_set = 1

    else:
        if mode:
            for i in range(4):
                tmp = ['0', '0', '0', '0']
                tmp[i] = '1'
                str_to_send = "".join(tmp)
                #print(str_to_send)
                arduino_serial.write(str.encode(str_to_send))
                read_block = arduino_serial.readline()
                if read_block:
                    print(read_block)
                time.sleep(0.5)
                

        else:
            for i in range(4): # for the 1st 2 seconds
                arduino_serial.write( str.encode( str(i + 1) ) )
                # print(str(i) + "-th loop")
                read_block = arduino_serial.readline()
                if read_block:
                    print(read_block)
                time.sleep(0.5)

