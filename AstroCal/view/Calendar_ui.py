from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from datetime import datetime
from datetime import time

def calendarStartDay(date=0):
    if date == 0 :
        date = datetime.now()
    firstday = date.replace(day=1)
    startday = firstday.isoweekday()
    if startday == 7:
        startday = 0
    return startday


def setUpDaysInMonth():
    dates = datetime.now()
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

class CalGrid(GridLayout):
    pass


class CalendarApp(App):
    def build(self):
        cg = CalGrid()
        dates = datetime.now()
        startday = calendarStartDay()

        cg.ids['month_label'].text = dates.strftime("%B %Y") 

        buttons = list(cg.ids.keys())
        
        y = startday
        for x in range(1, setUpDaysInMonth() + 1):
            cg.ids[buttons[y + 1]].text = str(x) #populate buttons and show day numbers
            y += 1
        return cg
    def printToConsole(self):
        print("Clicked a Calendar day")
    
