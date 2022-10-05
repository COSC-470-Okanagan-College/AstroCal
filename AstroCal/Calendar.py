from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from datetime import datetime
from datetime import time
from functools import partial
import swisseph as swe

dates = datetime.now()
firstday = dates.replace(day=1)
startday = firstday.isoweekday()
if startday == 7:
    startday = 0
def daysInMonth():
    if dates.month in [1,3,5,7,8,10,12]:
        return 31
    elif dates.month in [4,6,9,11]:
        return 30
    elif dates.month == 2:
        yr = dates.year
        if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
            return 29
        else:
            return 28
def getRiseSet(year, month, day, celestial, status):
    constCel = swe.SUN
    if(celestial == 'MOON'):
        constCel = swe.MOON
    constStatus = swe.CALC_RISE
    if(status == 'SET'):
        constStatus = swe.CALC_SET
    tjd = swe.julday(year, month, day, 7, swe.GREG_CAL)  # julian day
    res, tret = swe.rise_trans(tjd, constCel, constStatus,
                               (-119.4960, 49.8880, 342.0), 0, 0, swe.FLG_SWIEPH)  # Coordiantes are hardcoded for now
    if (res != 0):
        return None
    utcTime = swe.jdut1_to_utc(tret[0], swe.GREG_CAL)
    return utcTime

class CalGrid(GridLayout):
    pass

class DayMode(BoxLayout):
    pass

class CalendarApp(App):
    def build(self):
        cg = CalGrid()
        cg.ids['month_label'].text = dates.strftime("%B %Y") #Show month name and year
        buttons = list(cg.ids.keys())
        y = startday
        for x in range(1, daysInMonth() + 1):
            cg.ids[buttons[y + 1]].text = str(x) #populate buttons and show day numbers
            cg.ids[buttons[y + 1]].bind(on_press=partial(self.showDayMode, x))
            y += 1
        return cg
    
    def showDayMode(self, instance, dayX):
        dayInfo = DayMode()
        #location
        #dayInfo.ids['l1'].text = 
        # moon and sun info
        sunrise = getRiseSet(dates.year, dates.month, dayX, 'SUN', 'RISE')
        sunset = getRiseSet(dates.year, dates.month, dayX, 'SUN', 'SET')
        moonrise = getRiseSet(dates.year, dates.month, dayX, 'MOON', 'RISE')
        moonset = getRiseSet(dates.year, dates.month, dayX, 'MOON', 'SET')
        # jdut1_to_utc returns a list - convert the time to a time() object
        sunriseT = time(sunrise[3], sunrise[4], int(sunrise[5]))
        sunsetT = time(sunset[3], sunset[4], int(sunset[5]))
        moonriseT = time(moonrise[3], moonrise[4], int(moonrise[5]))
        moonsetT = time(moonset[3], moonset[4], int(moonset[5]))
        dayInfo.ids['sr1'].text = "Sunrise: " + sunriseT.strftime("%H:%M:%S")
        dayInfo.ids['ss1'].text = "Sunset: " + sunsetT.strftime("%H:%M:%S")
        dayInfo.ids['mr1'].text = "Moonrise: " + moonriseT.strftime("%H:%M:%S")
        dayInfo.ids['ms1'].text = "Moonset: " + moonsetT.strftime("%H:%M:%S")
        popupWindow = Popup(title="Popup Window", content=dayInfo)
        popupWindow.open()

if __name__ == "__main__":
    CalendarApp().run()