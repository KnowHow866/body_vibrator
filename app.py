import tkinter as tk

# reference
# 1. multiple frame: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# 2. how to locate element:     pack, grid, place

root = tk.Tk()
root.title('Body vibrator')
root.geometry("300x200")
root.resizable(0, 0)
# root.pack_propagate(0)
# root.pack(fill=tk.BOTH, expand=1)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack_propagate(0)
        self.pack(fill=tk.BOTH, expand=1)

        self.entry_point()

    def entry_point(self):
        '''
        Start interface of program, let user choose basic mode
        basic mode like: direction, undirection
        '''
        self.direction_mode = tk.Button(
            self, text='Direction Mode(方向震動模式)',
            command=None
            )
        self.undirection_mode = tk.Button(
            self, text='Undirection Mode(無方向震動模式)',
            command=None
            )

        self.direction_mode.grid(row=0, sticky=tk.E+tk.W)
        self.undirection_mode.grid(row=1, sticky=tk.E+tk.W)

        # self.direction_mode.pack(side="top")
        # self.undirection_mode.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

app = Application(master=root)

if __name__ == '__main__':
    app.mainloop()
