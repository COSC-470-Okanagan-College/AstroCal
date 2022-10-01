from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from datetime import datetime

dm = datetime.now().month
#startday = dm.isoweekday()
#if startday == 7:
#    startday = 0
#else:
#    startday += 1
def daysInMonth():
    if dm in [1,3,5,7,8,10,12]:
        return 31
    elif dm in [4,6,9,11]:
        return 30
    elif dm == 2:
        yr = datetime.now().year
        if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
            return 29
        else:
            return 28
class CalGrid(GridLayout):
    pass

class CalendarApp(App):
    def build(self):
        for x in range(1,daysInMonth()):
            btn = self.root.ids[x]
            btn.text = str(x)
        return CalGrid()
        
    
if __name__ == "__main__":
    CalendarApp().run()