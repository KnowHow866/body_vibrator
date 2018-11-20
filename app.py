import argparse

# local module
from gui import Application
from serial import SerialManager

device_port = '/dev/cu.usbserial-AI0443U0'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
		'''
		Program to run GUI interface to control arduino device body_vibrator
		'''
	)
    parser.add_argument('--device_port', help='path to USB serial port of arduino, usually under /dev of unix like system')
    args = parser.parse_args()

    if args.device_port: device_port = args.device_port

    # set serial manager to manage serial operation 
    serial_manager = SerialManager(device_port=device_port)

    app = Application(serial_manager=serial_manager)
    app.title('Body vibrator')
    app.geometry("300x400")
    app.mainloop()