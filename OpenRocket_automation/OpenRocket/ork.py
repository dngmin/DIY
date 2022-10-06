import pyautogui
import time
import tkinter.messagebox as msg
import cv2
import os
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
        for key in para.keys():
            pyautogui.sleep(0.1)
            if key == 'shape_nose':
                for i in range(0,5):
                    pyautogui.press('\t')
            elif key == 'material':
                pyautogui.sleep(0.2)
                draw.material_selection(para[key])
                pyautogui.sleep(0.2)
            elif key =='thickness_nose' or key == 'shape_coef':
                pyautogui.press('\t')
                tabNca()
                pyautogui.write(str(para[key]))
            else:
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
            pyautogui.press(['\t','\t'])
            pyautogui.sleep(0.2)
            draw.material_selection(para_body['material'])
            pyautogui.sleep(0.2)
            pyautogui.press('\t')
            tabNca()
            pyautogui.write(str(para['diameter_body']))
            pyautogui.press('\t')
            tabNca()
            pyautogui.write(str(para_body['inner_diameter']))
            for i in range(0,5):
                pyautogui.press('\t')
            pyautogui.press('enter')
        pyautogui.click(draw.find_body(),750)
    
    def design_fin(self):
        draw = OpneRocket_automation(self.file)
        para = parameter.Para(self.file)
        para = para.fin()
        draw.drawing('fin')
        pyautogui.sleep(1)
        for key in para.keys():
            pyautogui.sleep(0.1)
            if key == 'shape_fin':
                continue
            elif key == 'inclination' or key == 'thickness_fin':
                pyautogui.press('\t')
            elif key == 'offset_fin':
                for i in range(0,3):
                    pyautogui.press('\t')
            elif key == 'material':
                pyautogui.press(['\t','\t'],interval=0.25)
                pyautogui.sleep(0.2)
                draw.material_selection(para[key])
                pyautogui.sleep(0.2)
                continue
            tabNca()
            pyautogui.write(str(para[key]))
        for i in range(0,8):
            pyautogui.press('\t')
        pyautogui.press('enter')

    def material_selection(self,meterial):
        try:
            if meterial == 'ボール紙':
                pass
            elif meterial == 'Basswood':
                for i in range(1,16):
                    pyautogui.press('up')
            elif meterial =='Blue tube':
                for i in range(0,15):
                    pyautogui.press('up')
            elif meterial =='Depron(XPS)':
                for i in range(0,14):
                    pyautogui.press('up')
            elif meterial =='Quantum tubing':
                for i in range(0,13):
                    pyautogui.press('up')
            elif meterial =='アクリル':
                for i in range(0,12):
                    pyautogui.press('up')
            elif meterial =='アルミ':
                for i in range(0,11):
                    pyautogui.press('up')
            elif meterial =='カエデ材':
                for i in range(0,10):
                    pyautogui.press('up')
            elif meterial =='カバ材':
                for i in range(0,9):
                    pyautogui.press('up')
            elif meterial =='カーボンファイバー':
                for i in range(0,8):
                    pyautogui.press('up')
            elif meterial =='ガラスファイバー':
                for i in range(0,7):
                    pyautogui.press('up')
            elif meterial =='コルク材':
                for i in range(0,6):
                    pyautogui.press('up')
            elif meterial =='スタイロフォーム(EPS)':
                for i in range(0,5):
                    pyautogui.press('up')
            elif meterial =='スタイロフォーム青(XPS)':
                for i in range(0,4):
                    pyautogui.press('up')
            elif meterial =='スプルース材':
                for i in range(0,3):
                    pyautogui.press('up')
            elif meterial =='チタン':
                for i in range(0,2):
                    pyautogui.press('up')
            elif meterial =='バルサ材':
                pyautogui.press('up')
            elif meterial =='ポリカーボネート(Lecan)':
                pyautogui.press('down')
            elif meterial =='ポリスチレン':
                for i in range(0,2):
                    pyautogui.press('down')
            elif meterial =='ポリ塩化ビニル':
                for i in range(0,3):
                    pyautogui.press('down')
            elif meterial =='マツ材':
                for i in range(0,4):
                    pyautogui.press('down')
            elif meterial =='合板(カバ材)':
                for i in range(0,5):
                    pyautogui.press('down')
            elif meterial =='真鍮':
                for i in range(0,6):
                    pyautogui.press('down')
            elif meterial =='紙フェノール':
                for i in range(0,7):
                    pyautogui.press('down')
            elif meterial =='紙(オフィス用)':
                for i in range(0,8):
                    pyautogui.press('down')
            elif meterial =='鉄':
                for i in range(0,9):
                    pyautogui.press('down')
            else:
                pass
        except:
            pass
    
    def find_body(self):
        scr = pyautogui.screenshot(region=(70,525,1830,475))
        scr.save('OpenRocket\\find_body.png')
        body = cv2.imread('OpenRocket\\find_body.png')
        gray = cv2.cvtColor(body,cv2.COLOR_BGR2GRAY)
        ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

        x_list = []

        for cnt in contours:
            if 800000 > cv2.contourArea(cnt) > 500:
                x, y, width, height = cv2.boundingRect(cnt)
                x_list.append(x)
        print(x_list)
        x_list.sort()
        print(x_list)
        os.remove('OpenRocket\\find_body.png')

        return int(x_list[-1] + 100) 
        
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