from tkinter import*
import simplekml
import pandas as pd
from tkinter import filedialog
import tkinter.messagebox as msgbox
import webbrowser
import time

"""
GPS tracker !


Longitude(経度) range
0 ~ 180 : 本初子午線より東
-180 ~ 0 : 本初子午線より西

Latitude(緯度) range : -180 ~ 180
0 ~ 180 : 北半球
-180 ~ 0 : 南半球


csvファイルを読み込む時には中身を

lan lot alt
x1  y1  z1
x2  y2  z2
..  ..  ..

のようにしてくださーい
( altはなかったら省略可)

"""

class GUI:
    def __init__(self):
        pass

    def main_GUI_open():
        gps_GUI = Tk()
        gps_GUI.title('GPS tracker')
        gps_GUI.geometry("400x300+300+300")
        gps_GUI.resizable(False,False)
        frame_main = Frame(gps_GUI)
        main_label = Label(frame_main,text="GPS tracker",font=('MSゴシック','20','bold'))
        main_point_btn = Button(frame_main,padx=20,pady=10,text='位置表示',command=GUI.point_GUI_open)
        main_route_btn = Button(frame_main,padx=20,pady=10,text='経路表示',command=GUI.route_GUI_open)

        frame_main.pack()
        main_label.pack(pady=30)
        main_point_btn.pack(pady=10)
        main_route_btn.pack(pady=10)

        gps_GUI.mainloop()

    def point_GUI_open():
        point_GUI = Tk()
        point_GUI.title('point')
        point_GUI.geometry("250x150+600+300")
        point_GUI.resizable(False,False)

        point_label_frame = Frame(point_GUI)
        Lat_label = Label(point_label_frame,text='緯度 (Latitude)',font=('MSゴシック','10','bold'))
        Lon_label = Label(point_label_frame,text='経度 (Longitude)',font=('MSゴシック','10','bold'))
        point_text_frame = Frame(point_GUI)
        Lat_Text = Entry(point_text_frame,width=15)
        Lon_Text = Entry(point_text_frame,width=15)
        point_btn_frame = Frame(point_GUI)
        run_btn = Button(point_btn_frame,padx=20,pady=5,text='Run',command=lambda:to_kml.point(Lon_Text.get(),Lat_Text.get()))

        point_label_frame.pack(side='left')
        Lat_label.pack(padx=4)
        Lon_label.pack(padx=4,pady=3)
        point_text_frame.pack(side='right')
        Lat_Text.pack(padx=4)
        Lon_Text.pack(padx=4,pady=3)
        point_btn_frame.pack(side='bottom')
        run_btn.pack(pady=5)

        point_GUI.mainloop()

    def route_GUI_open():

        def find_csv():
            file_selected = filedialog.askopenfilename(filetypes=(("csvファイル","*.csv"),("すべて","*.*")))
            file_path_text.delete(0,END)
            file_path_text.insert(0,file_selected)

        route_GUI = Tk()
        route_GUI.title('route')
        route_GUI.geometry("400x110+600+300")
        route_GUI.resizable(False,False)

        route_frame = LabelFrame(route_GUI,text='GPSファイル',font=('MSゴシック','10','bold'))
        route_frame.pack(fill='x',padx=5,pady=10)
        open_btn = Button(route_frame,text='open',width=10,command=lambda:find_csv())

        file_path_text = Entry(route_frame)        
        file_path_text.pack(side='left',fill='x',expand=True,padx=3,pady=5,ipady=4)        
        open_btn.pack(side='right')

        run_btn = Button(route_GUI,padx=20,pady=3,text='Run',command=lambda:to_kml.route(file_path_text.get()))
        run_btn.pack()

        route_GUI.mainloop()

class to_kml:
    def point(Longitude,Latitude): #  経度 , 緯度
        try:
            if (-180<=float(Latitude)<=180) and (-180<=float(Longitude)<=180):
                    point = simplekml.Kml()
                    point.newpoint(name='GPS POINT',description='POINT from GPS tracker',coords=[(Longitude,Latitude)])
                    point.save('GPS tracker point.kml')
                    func.ask_open_map()
            else:
                msgbox.showerror(title='value error!',message='-180から 180の間の値を入力してください')
        except ValueError:
            msgbox.showerror(title='value error!',message='正しい値を入力してください')

    def route(gps_file): # ファイル位置
        try:
            df = pd.read_csv(gps_file)
            try:
                coord = list(zip(df['lon'],df['lat'],df['alt']))
            except KeyError:
                coord = list(zip(df['lon'],df['lat']))

            route = simplekml.Kml()
            lin = route.newlinestring(name='GPS ROUTE',description='ROUTE from GPS tracker',coords=coord)
            lin.extrude = 1
            lin.altitudemode = simplekml.AltitudeMode.relativetoground
            lin.style.linestyle.color = simplekml.Color.greenyellow
            lin.style.linestyle.width = 8
            route.save('GPS tracker route.kml')
            func.ask_open_map()
        except FileNotFoundError:
            msgbox.showerror(title='FileNotFoundError!',message='ファイルが見つかりません')

class func:
    def ask_open_map():
        url = 'https://www.google.co.jp/maps/'
        
        res = msgbox.askyesno(title='open google map?',message='Googleマップを開きますか？')
        if res == True:
            webbrowser.open(url)
        else:
            pass

GUI.main_GUI_open()