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
from datetime import datetime
from control import control
import pytz
import sys
import logging

blue =  [0,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        mainlayout = BoxLayout(orientation='vertical', height=800, width=800)
        toplayout = BoxLayout(size_hint=(1, None))
        middlelayout = BoxLayout(size_hint=(1,None),height=400,orientation='vertical')
        bottomlayout = BoxLayout(size_hint=(1,None),height=75)
    #Defines the 3 buttons for the bottom of the screen: day, month, event.
        day = ToggleButton(text="DAY" ,
                     size = (20,20), 
                     background_color=blue,
                     bold=True,
                     group="bottomButtons")
        day.bind(on_press=self.dayView)
        month = ToggleButton(text="MONTH" ,
                    size = (20,20), 
                    background_color=blue,
                    bold=True,
                    group="bottomButtons")
        month.bind(on_press=self.monthView)
        event = ToggleButton(text="EVENTS" ,
                    size = (20,20), 
                    background_color=blue,
                    bold=True,
                    group="bottomButtons")
        event.bind(on_press=self.eventView)
        
        bottomlayout.add_widget(day)
        bottomlayout.add_widget(month)
        bottomlayout.add_widget(event)
    #Add display features to middle primary display window
        dayInfo = BoxLayout(orientation="vertical",size_hint=(1,None),height=150)
        dayImage = BoxLayout(size_hint=(1,None),height=250)
        wimg = Image(source="view/assets/moon_phases/full_moon.png",allow_stretch=True)
        dayImage.add_widget(wimg)

        sunrise = Label(text="SUNRISE "+str(self.getSunRise().time()), 
                        bold=True,
                        underline=True,
                        halign='left',
                        outline_color=blue)
        sunset = Label(text="SUNSET "+str(self.getSunSet().time()),bold=True,underline=True)
        moonrise = Label(text="MOONRISE "+str(self.getMoonRise().time()),bold=True,underline=True)
        moonset = Label(text="MOONSET "+str(self.getMoonSet().time()),bold=True,underline=True)
        
        dayInfo.add_widget(sunrise)
        dayInfo.add_widget(sunset)
        dayInfo.add_widget(moonrise)
        dayInfo.add_widget(moonset)
        middlelayout.add_widget(dayImage)
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
    def dayView(self,middlelayout):
        field = Label(text='Good Day')
        middlelayout.add_widget(field)
        
    def monthView(self,middlelayout):
        field = Label(text='What a month')
        middlelayout.add_widget(field)
        
    def eventView(self,middlelayout):
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