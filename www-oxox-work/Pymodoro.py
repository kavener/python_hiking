import tkinter
from tkinter import messagebox
DEFAULT_GAP = 25


class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        # tkinter 类型的字符串
        self.timer_text = tkinter.StringVar()
        self.timer_text.trace('w', self.build_time)
        self.time_left = tkinter.IntVar()
        self.time_left.set(DEFAULT_GAP)
        self.time_left.trace('w', self.alert())
        self.runing = False

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_time()
        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            bg='red',
            text='番茄钟',
            fg='white',
            font=('微软雅黑', 24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

    def build_buttons(self):
        build_frame = tkinter.Frame(self.mainframe)
        build_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        build_frame.columnconfigure(0, weight=1)
        build_frame.columnconfigure(1, weight=1)

        self.start_button = tkinter.Button(
            build_frame,
            text='start',
            command=self.start_timer
        )
        self.stop_button = tkinter.Button(
            build_frame,
            text='stop',
            command=self.stop_timer
        )
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        self.stop_button.config(state=tkinter.DISABLED)
    def build_time(self, *args):
        timer = tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=('微软雅黑', 36)
        )
        timer.grid(row=1, column=0, sticky='nsew')

    def start_timer(self):
        self.time_left.set(DEFAULT_GAP)
        self.runing = True
        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)
    def stop_timer(self):
        self.runing = False
        self.start_button.config(state=tkinter.NORMAL)
        self.stop_button.config(state=tkinter.DISABLED)

    def alert(self,*args):
        if not self.time_left.get():
            messagebox.shwinfo('时间到','小番茄')


    def minutes_seconds(self, seconds):
        return int(seconds / 60), int(seconds % 60)

    def update(self):
        time_left = self.time_left.get()
        if self.runing and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes,seconds)
            )
            self.time_left.set(time_left-1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes,seconds)
            )
            self.stop_timer()
        self.master.after(1000, self.update)

if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
