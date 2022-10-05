from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from datetime import datetime

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
class CalGrid(GridLayout):
    pass

class DayMode(FloatLayout):
    pass

class CalendarApp(App):
    def build(self):
        cg = CalGrid()
        cg.ids['month_label'].text = dates.strftime("%B %Y") 
        buttons = list(cg.ids.keys())
        y = startday
        for x in range(1, daysInMonth() + 1):
            cg.ids[buttons[y + 1]].text = str(x)
            y += 1
        return cg
    
    def showDayMode(self):
        dayInfo = DayMode()
        #location
        #dayInfo.ids['l1'].text = 
        # moon and sun info
        #dayInfo.ids['sr1'].text = 
        #dayInfo.ids['ss1'].text = 
        #dayInfo.ids['mr1'].text = 
        #dayInfo.ids['ms1'].text = 
        popupWindow = Popup(title="Popup Window", content=dayInfo, size_hint=(1,1),size=(400,400))
        popupWindow.open()

if __name__ == "__main__":
    CalendarApp().run()