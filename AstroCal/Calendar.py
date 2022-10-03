from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from datetime import datetime

date = datetime.now()
dm = date.month
firstday = date.replace(day=1)
startday = firstday.isoweekday()
if startday == 7:
    startday = 0
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
        cg = CalGrid()
        cg.ids['month_label'].text = date.strftime("%B %Y")
        buttons = list(cg.ids.keys())
        y = startday
        for x in range(1, daysInMonth() + 1):
            cg.ids[buttons[y + 1]].text = str(x)
            y += 1
        return cg

if __name__ == "__main__":
    CalendarApp().run()