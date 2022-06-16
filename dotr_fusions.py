import pyautogui
import pyperclip
import time
import subprocess

class DotrFusions:          
    def __init__(self):
        pyautogui.PAUSE = 0.1        
        self.exe_path = r'DOTR Modding Tool.exe'
        self.max_fusion = 26540
        self.fusion_done = 3821
        self.max_alters = int(self.max_fusion - self.fusion_done)
        self.counter = 1
        self.checkpoint = 100
        
    def CursorPosition(self):
        self.counter = 1
        main_page = int(self.fusion_done / 20)
        rest_down = self.fusion_done % 20
        print(f'page:{main_page}')
        pyautogui.press('pgdn', main_page)
        pyautogui.press('down',rest_down)
        time.sleep(2)
        return

    def SaveFile(self):
        pyautogui.hotkey('ctrl','home')
        with pyautogui.hold('shift'):
            pyautogui.press(keys='tab', presses=2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press(keys='tab', presses=2)
        return

    def OpenExe(self):
        pyautogui.hotkey('ctrl', 'end')
        # pyautogui.hotkey('win','d')
        subprocess.Popen(f'explorer {self.exe_path}')
        time.sleep(1)
        pyperclip.copy('E:\CURSOS PROGRAMACAO\PYTHON\yugioh_dotr\dotr.iso')
        pyautogui.hotkey('ctrl','v')
        time.sleep(5)
        pyautogui.hotkey('enter')
        with pyautogui.hold('ctrl'):
            pyautogui.press(keys='pgdn', presses=4)
        time.sleep(1)
        pyautogui.press(keys='tab', presses=3)
        time.sleep(2)
        return

    def MakeChanges(self):
        pyperclip.copy('Blue-Eyes White Dragon')
        while self.counter < self.max_alters:
            if(self.counter == self.checkpoint):
                self.SaveFile()
                self.CursorPosition()
            col = 2
            while col < 8:
                pyautogui.press('tab', col)
                pyautogui.hotkey('f2')
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('down')
                pyautogui.hotkey('ctrl','left')
                col +=2
                time.sleep(0.4)
            pyautogui.press('down')
            self.fusion_done += 1
            print(f'changes:{self.counter}, done:{self.fusion_done}')
            self.counter += 1
            time.sleep(1.2)
    
    def Main(self):
        self.OpenExe()
        self.CursorPosition()
        self.MakeChanges()
        self.SaveFile()
        
# executes the code
app = DotrFusions()
app.Main()
