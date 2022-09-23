#Astro Calender Console Menu

#Imports
from datetime import datetime
import control
import pytz
import sys


#sun options
def sun():
    print('Sun Events')
    print('1. View Today')
    print('2. View Full Month')
    print('3. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        getCurrentdate()
        now = datetime.now()
        sun_rise = control.getRiseSet(now.year, now.month, now.day, 'SUN', 'RISE')
        local_rise = utc_hack(sun_rise)

        sun_set = control.getRiseSet(now.year, now.month, now.day, 'SUN', 'SET')
        local_set = utc_hack(sun_set)
        print('Sun will Rise: ' + str(local_rise.hour) + ':' + str(local_rise.minute)) #call function name for moon rise
        print('Sun will Set : ' + str(local_set.hour) + ':' + str(local_set.minute)) #call function name for moon set
    elif option == 2:
        print() #call month function
    elif option == 3:
        createMenu()
    else:
        print('error not an option')
        sun()
    input('Press enter to continue...')
    createMenu()

def utc_hack(date_tup):
    timezone = pytz.timezone('PST8PDT')
    timeUTC = datetime(date_tup[0], date_tup[1], date_tup[2], date_tup[3], date_tup[4], 0, 0, pytz.UTC)
    timeLocal = timeUTC.astimezone(timezone)
    return timeLocal
        

#moon options
def moon():
    print('Moon Events')
    print('1. View Today')
    print('2. View Full Month')
    print('3. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        getCurrentdate()
        now = datetime.now()
        moon_rise = control.getRiseSet(now.year, now.month, now.day, 'MOON', 'RISE')
        local_rise = utc_hack(moon_rise)

        moon_set = control.getRiseSet(now.year, now.month, now.day, 'MOON', 'SET')
        local_set = utc_hack(moon_set)
        print('Moon will Rise: ' + str(local_rise.hour) + ':' + str(local_rise.minute)) #call function name for moon rise
        print('Moon will Set : ' + str(local_set.hour) + ':' + str(local_set.minute)) #call function name for moon set
    elif option == 2:
        moon() 
        #call month function
    elif option == 3:
        createMenu()
    else:
        print('error not an option')
        sun()
    input('Press enter to continue...')
    createMenu()

#get current date
def getCurrentdate():
    currentdate = datetime.now()
    today = currentdate.strftime("%B-%d-%Y  %H:%M \n")
    print(today)


#create menu
def createMenu():
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    getCurrentdate()
    print('1. Sun Events')
    print('2. Moon Events')
    print('3. exit \n')
    option = int(input('Enter selection: '))
    if option == 1:
        sun()
    elif option == 2:
        moon()
    elif option == 3:
        print('Bye')
        sys.exit(0)
    else:
        print('error not an option')
        createMenu()
