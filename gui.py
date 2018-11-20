import tkinter as tk
from tkinter import font  as tkfont

from serial import SerialManager

class Application(tk.Tk):
    '''
    Controller of tkinter Frame
    '''
    def __init__(self, serial_manager=None, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # serial port to communicate ith arduino
        self.serial_manager = serial_manager

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = dict()
        for F in (StartPage, DirectionVibration,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Body vibrator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Direction Mode(方向震動模式)", pady=10,
                            command=lambda: controller.show_frame('DirectionVibration'))
        button2 = tk.Button(self, text="Undirection Mode(無方向震動模式)",  pady=10,
                            command=lambda: None)

        button1.pack(pady=10)
        button2.pack(pady=10)

class DirectionVibration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        var = tk.StringVar()
        vibration_set = []

        vibration_set.append(
            tk.Radiobutton(self, 
                    text='由 1~6 來回震動一次', 
                    variable=var, value='1,2,3,4,5,6,5,4,3,2,1',
                    command=None)
        )
        vibration_set.append(
            tk.Radiobutton(self, 
                    text='由 6~1 來回震動一次',
                    variable=var, value='6,5,4,3,2,1,2,3,4,5,6',
                    command=None)
        )

        for radio_button in vibration_set:
            radio_button.pack(pady=7)

        def direction_vibrate_handler():
            controller.serial_manager.direction_vibration_command_compile(point_str=var.get())
            controller.serial_manager.direction_vibrate()

        commit_button = tk.Button(
            self, text="執行", 
            command=direction_vibrate_handler)
        commit_button.pack(pady=10)

        back_button = tk.Button(
            self, text="回上一頁", 
            command=lambda: controller.show_frame('StartPage'))
        back_button.pack(pady=10)

if __name__ == '__main__':
    print('Run test mode GUI, no device_serial_port is connected', '\n')

    # set serial manager to manage serial operation 
    serial_manager = SerialManager(device_port=None)

    app = Application(serial_manager=serial_manager)
    app.title('Body vibrator')
    app.geometry("300x400")
    app.mainloop()
