from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from datetime import datetime
from datetime import time
from AstroCal.constants.globals import DATE
from AstroCal.constants.globals import LOCATION
from dateutil.relativedelta import relativedelta

def calendarStartDay(date=0):
    if date == 0 :
        date = datetime.now()
    firstday = date.replace(day=1)
    startday = firstday.isoweekday()
    if startday == 7:
        startday = 0
    return startday


def setUpDaysInMonth():
    if DATE.month in [1,3,5,7,8,10,12]:
        return 31
    elif DATE.month in [4,6,9,11]:
        return 30
    elif DATE.month == 2:
        yr = DATE.year
        if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
            return 29
        else:
            return 28

class CalGrid(GridLayout):
    pass

sm = ScreenManager()

class CalendarApp(App):
    def build(self):
        return CalGrid()

    def loadDays(self):
        startday = calendarStartDay()
        buttons = list(self.ids.keys())
        
        y = startday
        for x in range(1, setUpDaysInMonth() + 1):
            self.ids[buttons[y + 1]].text = str(x) #populate buttons and show day numbers
            y += 1

    def getCurLocation(self):
        return "Kelowna, Canada"
        #return LOCATION

    def getMonthName(self):
        return DATE.strftime("%B %Y")

    def openDayView(self):
        print("A day button was clicked.")

    def moveMonthBack(self):
        global DATE
        DATE = DATE + relativedelta(months=-1)
        print(DATE.strftime("%B %Y"))
        self.month_label = DATE.strftime("%B %Y")

    def moveMonthForward(self):
        global DATE
        DATE = DATE + relativedelta(months=+1)
        print(DATE.strftime("%B %Y"))
        self.month_label = DATE.strftime("%B %Y")