from tkinter import *
from datetime import datetime
import control


# creating tkinter window
window = Tk()
window.title = ("Astro Calendar")
window.geometry("400x400")

# app label
header = Label(
    text="✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ",
    font=10,
)
header.pack()

today = datetime.now().strftime("%B-%d-%Y  %H:%M \n")
todayLabel = Label(
    text=today,
    font=5,
)
todayLabel.pack()


def sun_information():
    sunInfo = 'Sun will Rise: ' + control.celestial_rise_or_set(
        'SUN', 'RISE') + '\n Sun will Set : ' + control.celestial_rise_or_set('SUN', 'SET')
    display.config(text=sunInfo)


def moon_information():
    moonInfo = 'Moon will Rise: ' + control.celestial_rise_or_set(
        'MOON', 'RISE') + '\n Moon will Set : ' + control.celestial_rise_or_set('MOON', 'SET')
    display.config(text=moonInfo)


# sun menu options
sunFrame = LabelFrame(window, text="Sun Options", padx=40, pady=20)
sunFrame.pack(padx=10, pady=10)
sToday = Button(sunFrame, text="View Today",
                command=sun_information, padx=5, pady=5)
sToday.grid(row=0, column=0)
sMonth = Button(sunFrame, text="View Month", padx=5, pady=5)
sMonth.grid(row=0, column=2)


# moon menu options
moonFrame = LabelFrame(window, text="Moon Options", padx=40, pady=20)
moonFrame.pack(padx=10, pady=10)
mToday = Button(moonFrame, text="View Today",
                command=moon_information, padx=5, pady=5)
mToday.grid(row=0, column=0)
mMonth = Button(moonFrame, text="View Month", padx=5, pady=5)
mMonth.grid(row=0, column=2)

# output
outputFrame = LabelFrame(window, text="Output", padx=40, pady=20)
outputFrame.pack()
display = Label(
    outputFrame,
    text=" ",
)
display.pack()
