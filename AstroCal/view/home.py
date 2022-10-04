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
from kivy.uix.behaviors import *
from kivy.uix.togglebutton import *

blue =  [0,0,1,1]


class HBoxLayoutExample(App):
    def build(self):
        textinput = Label(text='Hello world')
        textinput1 = Label(text='Hello world')

        dayInfo = GridLayout()
        dayInfo.cols = 1

        layout = BoxLayout(orientation='vertical', height=800, width=800)
        toplayout = BoxLayout(size_hint=(1, None), height=100)
        middle = BoxLayout(size_hint=(1,None),height=400)
        bottomlayout = BoxLayout(size_hint=(1,None),height=75)
        btn2 = Button(text="Button 2" ,
                     background_color=blue)
        colors = [blue]

        btn1 = Button(text="Day" ,
                     size = (10,10), 
                     background_color=blue)
        btn1.bind(on_press=self.day)
        btn2 = Button(text="Month" ,
                    size = (10,10), 
                    background_color=blue)
       # btn2.bind(on_press=self.month)
        btn3 = Button(text="Events" ,
                    size = (10,10), 
                    background_color=blue)
        #btn3.bind(on_press=self.events)
                     
        bottomlayout.add_widget(btn1)
        bottomlayout.add_widget(btn2)
        bottomlayout.add_widget(btn3)

        dayInfo.add_widget(textinput)
        dayInfo.add_widget(textinput1)
        middle.add_widget(dayInfo)

        tbtn = Button(text="Button" ,
                     size = (10,10), 
                     background_color=blue)
        toplayout.add_widget(tbtn)
        layout.add_widget(toplayout)
        layout.add_widget(middle)
        layout.add_widget(bottomlayout)
        return layout
    
    def day(self, instance):
        dayLabel = Label(text='This is the day page')


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()