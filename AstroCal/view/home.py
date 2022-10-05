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
from datetime import datetime
from control import control
import pytz
import sys
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


blue =  [0,0,1,1]


class HBoxLayoutExample(App):
    def build(self):
        mainlayout = BoxLayout(orientation='vertical', height=800, width=800)
        toplayout = BoxLayout(size_hint=(1, None))
        middlelayout = BoxLayout(size_hint=(1,None),height=400)
        bottomlayout = BoxLayout(size_hint=(1,None),height=75)
    #Defines the 3 buttons for the bottom of the screen: day, month, event.
        day = ToggleButton(text="Day" ,
                     size = (10,10), 
                     background_color=blue,
                     bold=True,
                     group="bottomButtons")
        #day.bind(on_press=self.dayView)
        month = ToggleButton(text="Month" ,
                    size = (10,10), 
                    background_color=blue,
                    bold=True,
                    group="bottomButtons")
        #month.bind(on_press=self.monthView)
        event = ToggleButton(text="Events" ,
                    size = (10,10), 
                    background_color=blue,
                    bold=True,
                    group="bottomButtons")
        #event.bind(on_press=self.eventView)
        
        bottomlayout.add_widget(day)
        bottomlayout.add_widget(month)
        bottomlayout.add_widget(event)
    #Add display features to middle primary display window
        
        sunrise = Label(text="SUNRISE "+str(self.getSunRise()).center(10), bold=True)
        sunset = Label(text="SUNSET "+str(self.getSunSet()),bold=True)
        moonrise = Label(text="MOONRISE "+str(self.getMoonRise()),bold=True)
        moonset = Label(text="MOONSET "+str(self.getMoonSet()),bold=True)
        dayInfo = GridLayout()
        dayInfo.cols = 1
        dayInfo.add_widget(moonset)
        dayInfo.add_widget(moonrise)
        dayInfo.add_widget(sunset)
        dayInfo.add_widget(sunrise)
        middlelayout.add_widget(dayInfo)
       
    #Add to top boxlayout
        topbtn = Button(text="Button" ,
                     size = (10,10), 
                     background_color=blue)
        toplayout.add_widget(topbtn)
    #Add top,middle,bottom boxlayouts to mainlayout
        mainlayout.add_widget(toplayout)
        mainlayout.add_widget(middlelayout)
        mainlayout.add_widget(bottomlayout)
        return mainlayout

    ## Functions to call specific fields
    def dayView(middlelayout):
        field = Label(text='Good Day')
        middlelayout.add_widget(field)
        
    def monthView(middlelayout):
        field = Label(text='What a month')
        middlelayout.add_widget(field)
        
    def eventView(middlelayout):
        field = Label(text='Whats the event')
        middlelayout.add_widget(field)
        
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