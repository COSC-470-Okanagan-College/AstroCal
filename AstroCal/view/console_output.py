# Astro Calender Console Menu

# Imports
from datetime import datetime
from control import control
import sys


# Main Menu
def main_menu():
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    getCurrentdate()
    print('1. Sun Events')
    print('2. Moon Events')
    print('3. View Month')
    print('4. exit \n')
    option = int(input('Enter selection: '))
    if option == 1:
        sun_menu()
    elif option == 2:
        moon_menu()
    elif option == 3:
        getCurrentMonth()
    elif option == 4:
        print('Bye')
        sys.exit(0)
    else:
        print('error not an option')
        main_menu()


# sun options
def sun_menu():
    print('Sun Events')
    print('1. View Today')
    print('2. View Full Month')
    print('3. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        print(getCurrentdate())  # Displays current date
        # call function name for moon rise
        print('Sun will Rise: ' + control.celestial_rise_or_set('SUN', 'RISE'))
        # call function name for moon set
        print('Sun will Set : ' + control.celestial_rise_or_set('SUN', 'SET'))
    elif option == 2:
        print()  # call month function
    elif option == 3:
        main_menu()
    else:
        print('error not an option')
        sun_menu()
    input('Press enter to continue...')
    main_menu()


# moon options
def moon_menu():
    print('Moon Events')
    print('1. View Today')
    print('2. View Full Month')
    print('3. View Moon Status')
    print('4. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        print(getCurrentdate())  # Displays current date
        # call function name for moon rise
        print('Moon will Rise: ' + control.celestial_rise_or_set('MOON', 'RISE'))
        # call function name for moon set
        print('Moon will Set : ' + control.celestial_rise_or_set('MOON', 'SET'))
    elif option == 2:
        moon_menu()
        # call month function
    elif option == 3:
        moon_status_result = control.getMoonStatus()
        print(moon_status_result[0])
        print(moon_status_result[1])
    elif option == 4:
        main_menu()
    else:
        print('error not an option')
        sun_menu()
    input('Press enter to continue...')
    main_menu()


# get current date
def getCurrentdate():
    currentdate = datetime.now()
    today = currentdate.strftime("%B-%d-%Y  %H:%M \n")
    return today


def getCurrentMonth():
    # Get Current Month & Year
    currentdate = datetime.now()
    month_str = currentdate.strftime("%B")
    month = currentdate.month
    year = currentdate.year

    # Get number of days in the month
    if month > 11:  # If month is December
        daysinmonth = (datetime(year+1, 1, 1) - datetime(year, month, 1)).days
    else:
        daysinmonth = (datetime(year, month + 1, 1) -
                       datetime(year, month, 1)).days

    # Store calculations here || Move into for loop when calculations are put in
    sunrise_start = currentdate.strftime("%I:%M %p")
    sunrise_end = currentdate.strftime("%I:%M %p")
    sunset_start = currentdate.strftime("%I:%M %p")
    sunset_end = currentdate.strftime("%I:%M %p")
    moonrise_start = currentdate.strftime("%I:%M %p")
    moonrise_end = currentdate.strftime("%I:%M %p")
    moonset_start = currentdate.strftime("%I:%M %p")
    moonset_end = currentdate.strftime("%I:%M %p")

    now = datetime.now()
    # Print out info for each day in the month
    for day_wrong in range(daysinmonth):
        day = day_wrong+1
        moon_rise = control.getRiseSet(
            now.year, now.month, day, 'MOON', 'RISE')
        local_moon_rise = utc_hack(moon_rise)
        moon_set = control.getRiseSet(now.year, now.month, day, 'MOON', 'SET')
        local_moon_set = utc_hack(moon_set)
        sun_rise = control.getRiseSet(now.year, now.month, day, 'SUN', 'RISE')
        local_sun_rise = utc_hack(sun_rise)
        sun_set = control.getRiseSet(now.year, now.month, day, 'SUN', 'SET')
        local_sun_set = utc_hack(sun_set)
        print("".ljust(29, '='))
        print("{} {}, {}".format(month_str, day, year))
        print("".ljust(29, '='))
        print("{:<12} | {:<12}".format("Event", "Time"))
        print("".ljust(29, '-'))
        print("{:<12} | {:<12}".format("Sunrise", str(
            local_sun_rise.hour) + ':' + str(local_sun_rise.minute)))
        print("{:<12} | {:<12}".format("Sunset", str(
            local_sun_set.hour) + ':' + str(local_sun_set.minute)))
        print("{:<12} | {:<12}".format("Moonrise", str(
            local_moon_rise.hour) + ':' + str(local_moon_rise.minute)))
        print("{:<12} | {:<12}".format("Moonset", str(
            local_moon_set.hour) + ':' + str(local_moon_set.minute)))
        print()
    main_menu()
