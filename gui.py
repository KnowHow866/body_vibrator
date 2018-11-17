
# test communicate with arduino by serial bus
# reference doc: https://playground.arduino.cc/interfacing/python

import argparse
import serial
import tkinter as tk

device_port = '/dev/cu.usbserial-AI0443U0' # default to holis macBook, please set as your own port

arduino_serial = serial.Serial(device_port, 9600, timeout=.1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
		'''
		Program to run GUI interface to control arduino device body_vibrator
		'''
	)
    parser.add_argument('--device_port', help='path to USB serial port of arduino, usually under /dev of unix like system')
    args = parser.parse_args()

    if args.device_port: arduino_serial = args.device_port

    print('Serial read test'.ljust(100, '.'))
    while True:
        read_block = arduino_serial.readline()
        if read_block:
            print(read_block)
