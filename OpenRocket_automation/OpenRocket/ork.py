import pyautogui
import time
import tkinter.messagebox as msg
from OpenRocket import parameter

def Timer(start,timeout=5):
    end = time.time()
    if end - start > timeout:
        raise TimeoutError

def tabNca():
    pyautogui.press(['\t','\t'])
    pyautogui.hotkey('ctrl','a')

class OpneRocket_automation:

    def __init__(self,file,nose_png='OpenRocket\\nose.png',body_png='OpenRocket\\body.png',fin_png='OpenRocket\\fin.png'):
        self.file = file
        self.nose_png = nose_png
        self.body_png = body_png
        self.fin_png = fin_png

    def OpenRocket_is_open(self):

        window = pyautogui.getWindowsWithTitle('Rocket')[0]
        if window:
            if window.isActive == False:
                window.activate()
            if window.isMaximized == False:
                window.maximize()
    
    def drawing(self,parts):
        if parts == 'nose':
            parts_img = self.nose_png
        if parts == 'body':
            parts_img = self.body_png
        if parts == 'fin':
            parts_img = self.fin_png
        parts_pos = None
        start = time.time()
        while parts_pos is None:
            parts_pos = pyautogui.locateOnScreen(parts_img,grayscale=True)
            pyautogui.moveTo(10,10)
            Timer(start)
        pyautogui.click(parts_pos)
    
    def design_nose(self):
        draw = OpneRocket_automation(self.file)
        para = parameter.Para(self.file)
        para = para.nose()
        draw.drawing('nose')
        pyautogui.sleep(1)
        for i in range(0,6):
            pyautogui.press('\t')
        for key in para.keys():
            if key == 'shape_nose':
                continue
            if key == 'thickness_nose':
                pyautogui.press('\t')
            tabNca()
            pyautogui.write(str(para[key]))
        pyautogui.press(['\t','\t','\t','enter'])

    def design_body(self):
        draw = OpneRocket_automation(self.file)
        para = parameter.Para(self.file)
        para = para.body()
        for i in range(1,len(para)-1):
            draw.drawing('body')
            pyautogui.sleep(1)
            para_body = para[f'body{i}']
            pyautogui.hotkey('ctrl','a')
            pyautogui.write(f'body{i}')
            pyautogui.press('\t')
            tabNca()
            pyautogui.write(str(para_body['lenght_body']))
            pyautogui.press(['\t','\t','\t'])
            tabNca()
            pyautogui.write(str(para['diameter_body']))
            pyautogui.press('\t')
            tabNca()
            pyautogui.write(str(para_body['inner_diameter']))
            pyautogui.press(['\t','\t','\t','\t','\t','enter'])
        pyautogui.click(1700,750)
    
    def design_fin(self):
        draw = OpneRocket_automation(self.file)
        para = parameter.Para(self.file)
        para = para.fin()
        draw.drawing('fin')
        pyautogui.sleep(1)
        for key in para.keys():
            if key == 'shape_fin':
                continue
            if key == 'inclination' or key == 'thickness_fin':
                pyautogui.press('\t')
            if key == 'offset_fin':
                pyautogui.press(['\t','\t','\t'])
            tabNca()
            pyautogui.write(str(para[key]))
        for i in range(0,10):
            pyautogui.press('\t')
        pyautogui.press('enter')

    def OpenRocket(self):
        try:
            rocket = OpneRocket_automation(self.file)
            rocket.OpenRocket_is_open()
            rocket.design_nose()
            rocket.design_body()
            rocket.design_fin()
            msg.showinfo(title='did it!',message='お待たせしました!')
        except IndexError:
            msg.showerror(title='Found Error',message='OpenRocketを開いてから再起動してください')
        except TimeoutError:
            msg.showerror(title='Timeout Error',message='できませんでした、、')