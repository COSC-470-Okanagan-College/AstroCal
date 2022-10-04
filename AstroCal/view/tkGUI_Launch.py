from tkinter import *
from datetime import datetime
import control
import pytz
import sys

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


def sunInformation():
    now = datetime.now()
    sun_rise = control.getRiseSet(now.year, now.month, now.day, 'SUN', 'RISE')
    local_rise = utc_hack(sun_rise)
    sun_set = control.getRiseSet(now.year, now.month, now.day, 'SUN', 'SET')
    local_set = utc_hack(sun_set)

    sunInfo = 'Sun will Rise: ' + str(local_rise.hour) + ':' + str(
        local_rise.minute) + '\n Sun will Set : ' + str(local_set.hour) + ':' + str(local_set.minute)
    display.config(text=sunInfo)


def utc_hack(date_tup):
    timezone = pytz.timezone('PST8PDT')
    timeUTC = datetime(date_tup[0], date_tup[1], date_tup[2],
                       date_tup[3], date_tup[4], 0, 0, pytz.UTC)
    timeLocal = timeUTC.astimezone(timezone)
    return timeLocal


# sun menu options
sunFrame = LabelFrame(window, text="Sun Options", padx=40, pady=20)
sunFrame.pack(padx=10, pady=10)
sToday = Button(sunFrame, text="View Today",
                command=sunInformation, padx=5, pady=5)
sToday.grid(row=0, column=0)
sMonth = Button(sunFrame, text="View Month", padx=5, pady=5)
sMonth.grid(row=0, column=2)


def moonInformation():
    now = datetime.now()
    moon_rise = control.getRiseSet(
        now.year, now.month, now.day, 'MOON', 'RISE')
    local_rise = utc_hack(moon_rise)
    moon_set = control.getRiseSet(now.year, now.month, now.day, 'MOON', 'SET')
    local_set = utc_hack(moon_set)

    moonInfo = 'Moon will Rise: ' + str(local_rise.hour) + ':' + str(
        local_rise.minute) + '\n Moon will Set : ' + str(local_set.hour) + ':' + str(local_set.minute),
    display.config(text=moonInfo)


# moon menu options
moonFrame = LabelFrame(window, text="Moon Options", padx=40, pady=20)
moonFrame.pack(padx=10, pady=10)
mToday = Button(moonFrame, text="View Today",
                command=moonInformation, padx=5, pady=5)
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
