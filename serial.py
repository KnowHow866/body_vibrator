
import serial
import time

class SerialManager():
    '''
    Control communication with arduino
    '''
    def __init__(self, device_port=None, vibrator_number_support=6):
        try:
            self.serial = serial.Serial(device_port, 9600, timeout=1)
        except Exception as e:
            print('Serial is not successfully build, so in test mode', '\n')
            self.serial = None

        self.vibrator_number_support = vibrator_number_support

        self.direction_vibrate_command = []
        self.direction_vibrate_delay_time = 0.5

        self.undirection_vibrate_command = []
        self.undirection_vibrate_delay_time = 0.5
        
    def hand_shake(self, content=None):
        '''
        Tell device what kind of data going to be pass through
        '''

        if content.lower() == 'direction': content = '1'
        if content.lower() == 'undirection': content = '0'

        print('Hnad shaking...')

        if self.serial:
            self.serial.write(str.encode(str(content)))
            read_block = arduino_serial.readline()
        else:
            read_block = 'TestMode'

        if read_block:
            print('Hand shake success, receive: %s' % (read_block), '\n')
            return True
        else:
            print('Hand shake fail, with data: %s' % content, '\n')
            return False
        
    def direction_vibration_command_compile(self, point_str='1:1,2,3,4,5,6'):
        '''
        For direction vibrate
        Convert vibrator point to vibrate string to the array in form of that pass to arduino
        '''
        command_arr = []

        point_arr = point_str.split(',')
        for point_data in point_arr:
            vibrators_status = ['0' for i in range(self.vibrator_number_support)]

            pointed_vibrators = point_data.split(':')
            pointed_vibrators = [data.strip() for data in pointed_vibrators]
            
            for vibrator in pointed_vibrators:
                vibrators_status[int(vibrator)-1] = '1' # set specific vibrator to vibrate

            command_arr.append(''.join(vibrators_status))

        print('Direction vibration command is set')
        print(command_arr, '\n')
        
        self.direction_vibrate_command = command_arr
        return command_arr

    def direction_vibrate(self, command_arr=None):
        ''' Do direction vibrate '''
        if command_arr is None: command_arr = self.direction_vibrate_command

        for command in command_arr:
            if not self.hand_shake(content='direction'): raise Exception('Hand shake error')

            print('Direction commnad: %s' % command, '\n')
            self.hand_shake(content=command)

            time.sleep(self.direction_vibrate_delay_time)

    def undirection_vibration_command_compile(self, amplitude_str='1,2,3,4'):
        return amplitude_str.split(',')

    def undirection_vibrate(self, command_arr=None):
        if command_arr is None: command_arr = self.undirection_vibrate_command

        for command in command_arr:
            if not self.hand_shake(content='undirection'): raise Exception('Hand shake error')

            print('Undirection commnad: %s' % command, '\n')
            self.hand_shake(content=command)

            time.sleep(self.undirection_vibrate_delay_time)
        