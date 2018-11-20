import tkinter as tk
from tkinter import font  as tkfont

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

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

        button1 = tk.Button(self, text="Direction Mode(方向震動模式)",
                            command=lambda: controller.show_frame('DirectionVibration'))
        button2 = tk.Button(self, text="Undirection Mode(無方向震動模式)",
                            command=lambda: None)
        button1.pack()
        button2.pack()

class DirectionVibration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        var = tk.StringVar()
        vibration_set = []

        vibration_set.append(
            tk.Radiobutton(self, text='由 1~6 來回震動一次',
                    variable=var, value='1',
                    command=None)
        )
        vibration_set.append(
            tk.Radiobutton(self, text='由 6~1 來回震動一次',
                    variable=var, value='2',
                    command=None)
        )

        for radio_button in vibration_set:
            radio_button.pack()


app = Application()
app.title('Body vibrator')
app.geometry("300x400")

if __name__ == '__main__':
    app.mainloop()
