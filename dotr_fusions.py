import pyautogui
import pyperclip
import time
import subprocess
import keyboard
import os

class DotrFusions:          
  def __init__(self):
    pyautogui.PAUSE = 0.1
    self.__dir_path = os.path.dirname(os.path.realpath(__file__)) 
    self.__exe_path = self.__dir_path + '\DOTR Modding Tool.exe'
    self.__max_fusion = 26540
    self.__fusion_done = 0
    self.__max_alters = int(self.__max_fusion - self.__fusion_done)
    self.__counter = 1
    self.__checkpoint = 100
      
  def CursorPosition(self):
    self.__counter = 1
    main_page = int(self.__fusion_done / 20)
    rest_down = self.__fusion_done % 20
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
    pyautogui.hotkey('win','d')
    subprocess.Popen(f'explorer {self.__exe_path}')
    time.sleep(1)
    pyperclip.copy(self.__dir_path + '\dotr.iso')
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
    self.__fusion_done += 1
    print(f'changes:{self.__counter}, done:{self.__fusion_done}')
    return
  
  def Main(self, fusion):
    self.OpenExe()
    self.__fusion_done = int(fusion)
    self.CursorPosition()
    
    while self.__counter < self.__max_alters:
      while not keyboard.is_pressed('esc'):
        if(self.__counter == self.__checkpoint):
          self.SaveFile()
          self.CursorPosition()
        else:
          time.sleep(1.2)
          self.MakeChanges()
          self.__counter += 1
      break
    self.SaveFile()
    pyautogui.hotkey('alt','f4')  
    msg = 'DONE!'
    return msg

# executes the code
# app = DotrFusions()
# app.Main('3851')