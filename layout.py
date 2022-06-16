from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox as tkm
from tkinter import font as tkFont
from dotr_fusions import DotrFusions

class app_layout:
    def __init__(self):
        self.__currfusion = 3861
        self.__appname = 'DOTR Fusion Changer'
        self.__bgcolor = '#002343'
        self.__fgcolor = '#FFFFFF'
        self.__btncolor = '#002343'
        self.__pad = 5
        self.__win = Tk()
        self.__font = tkFont.Font(family='Segoe UI', size=12, weight='normal')
        self.__dotr = DotrFusions()

    # app layout structure #
    def __layout_labels(self):
        self.__lb_start_fusion = Label(self.__win)
        self.__lb_info = Label(self.__win)

    def __layout_entries(self):
        self.__tx_fusion_number = Entry(self.__win)

    def __layout_buttons(self):
        self.__bt_start = Button(self.__win)
        self.__bt_about = Button(self.__win)

    def __layout_config(self):
        self.__win.title(self.__appname)
        self.__win.iconbitmap('whiterose.ico')
        self.__win.resizable(False, False)
        self.__win.config(padx=self.__pad, pady=self.__pad, background=self.__bgcolor)
        self.__lb_start_fusion.config(width=14, text='Start Fusion Number', justify='center', font=self.__font, background=self.__bgcolor, foreground=self.__fgcolor)
        self.__lb_info.config(width=14, text='AFTER START keep pressing ESC to exit', justify='center', font=self.__font, background=self.__bgcolor, foreground=self.__fgcolor)
        self.__tx_fusion_number.config(width=14, justify='center', font=self.__font, state='normal')
        self.__bt_start.config(width=14, text='Start', background=self.__btncolor, foreground=self.__fgcolor, font=self.__font)
        self.__bt_about.config(width=14, text='About', background=self.__btncolor, foreground=self.__fgcolor, font=self.__font)
        self.__tx_fusion_number.insert(0,str(self.__currfusion))

    def __layout_grid(self):
        self.__lb_start_fusion.grid(column=0, row=0, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.__tx_fusion_number.grid(column=0, row=1, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.__lb_info.grid(column=0, row=4, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.__bt_about.grid(column=0, row=5, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.__bt_start.grid(column=1, row=5, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')

    # app layout commands and binding #
    def __window_close(self):
        if tkm.askokcancel(self.__appname, 'Do you want to quit?'):
            self.__win.destroy()
    
    def __on_button_about_click(self):
        msg = 'Edgar Santa Rosa (C) 2022\nGitHub: https://github.com/EdgarOSR'
        tkm.showinfo(self.__appname, msg)
    
    def __on_button_start_click(self):
        fusion = self.__tx_fusion_number.get()
        if fusion.isnumeric:
            tkm.showinfo(self.__appname, self.__dotr.Main(fusion))
        else:
            tkm.showerror(self.__appname, 'Enter the fusion position number!')

    # set button commands #
    def __set_button_commands(self):
        self.__bt_about.config(command=self.__on_button_about_click)
        self.__bt_start.config(command=self.__on_button_start_click)

    # app layout initializer #
    def layout_builder(self):
        self.__layout_labels()
        self.__layout_entries()
        self.__layout_buttons()
        self.__layout_config()
        self.__layout_grid()
        self.__set_button_commands()
        self.__win.protocol('WM_DELETE_WINDOW', self.__window_close)
        self.__win.mainloop()
