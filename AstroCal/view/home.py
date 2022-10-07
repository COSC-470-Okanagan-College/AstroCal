from turtle import color
import kivy
import random

from kivy import *
from kivy.app import *
from kivy.uix.label import *
from kivy.core.window import *
from kivy.uix.anchorlayout import *
from kivy.uix.boxlayout import *
from kivy.uix.button import *
from kivy.uix.gridlayout import *
from kivy.uix.widget import *
from kivy.uix.textinput import *
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
import kivy.utils as utils
from datetime import datetime
from control import control
import pytz

blue =  [0,0,1,1]
pageBackground=utils.get_color_from_hex("#102646")
navColor=utils.get_color_from_hex('#4575B1')

class HBoxLayoutExample(App):
    mainlayout = BoxLayout(orientation='vertical', height=800, width=800)
    toplayout = BoxLayout(size_hint=(1, None))
    middlelayout = BoxLayout(size_hint=(1,None),height=400,center_x=True)
    bottomlayout = BoxLayout(size_hint=(1,None),height=75)
    def build(self):
    #Defines the 3 buttons for the bottom of the screen: day, month, event.
        day = ToggleButton(text="DAY",
                    state='down',
                    size = (20,20),
                    font_size=20, 
                    background_color=blue,
                    bold=True,
                    group="bottomButtons")
        day.bind(on_press=self.dayView)
        month = ToggleButton(text="MONTH" ,
                    size = (20,20), 
                    background_color=blue,
                    bold=True,
                    font_size=20,
                    group="bottomButtons")
        month.bind(on_press=self.monthView)
        event = ToggleButton(text="EVENTS" ,
                    size = (20,20), 
                    background_color=blue,
                    bold=True,
                    font_size=20,
                    group="bottomButtons")
        event.bind(on_press=self.eventView)
        self.bottomlayout.add_widget(day)
        self.bottomlayout.add_widget(month)
        self.bottomlayout.add_widget(event)
    #Add display features to middle primary display window (defaults to day view)
        dayInfo = AnchorLayout(size_hint=(1,None),height=300,anchor_x='right',anchor_y='center')
        dayImage = BoxLayout(orientation='vertical',size_hint=(1,None),height=300)
        wimg = Image(source="view/assets/moon_phases/full_moon.png",allow_stretch=True)
        dayImage.add_widget(wimg)
        info = Label(text="SUNRISE          0:00 AM\nSUNSET           0:00 AM\nMOONRISE     0:00 AM\nMOONSET       0:00 AM".format(),#str(self.getSunRise().time()), 
                        bold=True,
                        underline=True,
                        font_size=20,
                        line_height=2)
        moonphase = Label(text="FULL MOON",
                        bold=True,
                        underline=True,
                        halign='left',
                        font_size=20,
                        line_height=2,
                        center_y=True)
        dayImage.add_widget(moonphase)
        dayInfo.add_widget(info)
        self.middlelayout.add_widget(dayImage)
        self.middlelayout.add_widget(dayInfo)
    #Add to top boxlayout
        topbtn = Button(text="Button" ,
                     size = (10,10), 
                     background_color=blue)
        self.toplayout.add_widget(topbtn)
    #Add top,middle,bottom boxlayouts to mainlayout
        self.mainlayout.add_widget(self.toplayout)
        self.mainlayout.add_widget(self.middlelayout)
        self.mainlayout.add_widget(self.bottomlayout)
        return self.mainlayout
    ##Displays day view
    def dayView(self,thing):
        self.middlelayout.clear_widgets()
        dayInfo = AnchorLayout(size_hint=(1,None),height=300,anchor_x='right',anchor_y='center')
        dayImage = BoxLayout(orientation='vertical',size_hint=(1,None),height=300)
        wimg = Image(source="view/assets/moon_phases/full_moon.png",allow_stretch=True)
        dayImage.add_widget(wimg)
        info = Label(text="SUNRISE          0:00 AM\nSUNSET           0:00 AM\nMOONRISE     0:00 AM\nMOONSET       0:00 AM".format(),#str(self.getSunRise().time()),
                        bold=True,
                        underline=True,
                        font_size=20,
                        line_height=2)
        moonphase = Label(text="FULL MOON",
                        bold=True,
                        underline=True,
                        halign='left',
                        font_size=20,
                        line_height=2,
                        center_y=True)
        dayImage.add_widget(moonphase)
        dayInfo.add_widget(info)
        self.middlelayout.add_widget(dayImage)
        self.middlelayout.add_widget(dayInfo)
    ## Display month view
    def monthView(self,thing):
        field = Label(text='What a month')
        self.middlelayout.clear_widgets()
        self.middlelayout.add_widget(field)
    ## Display event view (placeholder)
    def eventView(self,thing):
        field = Label(text='Whats the event')
        self.middlelayout.clear_widgets()
        self.middlelayout.add_widget(field)
    ## Functions to call specific fields (will need ot be removed or edited to new control)
    def getSunRise(self):
        now = datetime.now()
        sun_rise = control.getRiseSet(now.year, now.month, now.day, 'SUN', 'RISE')
        local_rise = self.utc_hack(sun_rise)
        return local_rise
    def getSunSet(self):
        now = datetime.now()
        sun_rise = control.getRiseSet(now.year, now.month, now.day, 'SUN', 'SET')
        local_set = self.utc_hack(sun_rise)
        return local_set
    def getMoonRise(self):
        #App.getCurrentdate()
        now = datetime.now()
        sun_rise = control.getRiseSet(now.year, now.month, now.day, 'MOON', 'RISE')
        local_rise = self.utc_hack(sun_rise)
        return local_rise
    def getMoonSet(self):
        now = datetime.now()
        moon_set = control.getRiseSet(now.year, now.month, now.day, 'MOON', 'SET')
        local_set = self.utc_hack(moon_set)
        return local_set
    def getCurrentdate():
        currentdate = datetime.now()
        today = currentdate.strftime("%B-%d-%Y  %H:%M \n")
        print(today)
    def utc_hack(self,date_tup):
        timezone = pytz.timezone('PST8PDT')
        timeUTC = datetime(date_tup[0], date_tup[1], date_tup[2], date_tup[3], date_tup[4], 0, 0, pytz.UTC)
        timeLocal = timeUTC.astimezone(timezone)
        return timeLocal
   
def run():
    #if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()