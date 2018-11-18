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
value = arduino_serial.readline()

arduino_serial.write(b'1')
read_block = arduino_serial.readline()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
		'''
		Program to run GUI interface to control arduino device body_vibrator
		'''
	)
    parser.add_argument('--device_port', help='path to USB serial port of arduino, usually under /dev of unix like system')
    args = parser.parse_args()
    
    if args.device_port: device_port = args.device_port

    while True:
        for i in range(4):
            tmp = ['0', '0', '0', '0']
            tmp[i] = '1';
            str_to_send = "".join(tmp)
            print(str_to_send)
            arduino_serial.write(str.encode(str_to_send))
            if read_block:
                print(read_block)
            time.sleep(0.5)
