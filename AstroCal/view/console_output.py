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


# Displays the overall output for each day of the current month
def getCurrentMonth():
    # Get Current Month & Year
    now = datetime.now()
    month_str = now.strftime("%B")
    month = now.month
    year = now.year

    # Get number of days in the month
    if month > 11:  # If month is December
        days_in_month = (datetime(year+1, 1, 1) -
                         datetime(year, month, 1)).days
    else:
        days_in_month = (datetime(year, month + 1, 1) -
                         datetime(year, month, 1)).days

    # Print out info for each day in the month
    for day in range(days_in_month):
        day += 1

        print("".ljust(29, '='))
        print("{} {}, {}".format(month_str, day, year))
        print("".ljust(29, '='))
        print("{:<12} | {:<12}".format("Event", "Time"))
        print("".ljust(29, '-'))
        print("{:<12} | {:<12}".format(
            "Sunrise", control.celestial_rise_or_set('SUN', 'RISE', year, month, day)))
        print("{:<12} | {:<12}".format(
            "Sunset", control.celestial_rise_or_set('SUN', 'SET', year, month, day)))
        print("{:<12} | {:<12}".format("Moonrise",
              control.celestial_rise_or_set('MOON', 'RISE', year, month, day)))
        print("{:<12} | {:<12}".format(
            "Moonset", control.celestial_rise_or_set('MOON', 'SET', year, month, day)))
        print()
    main_menu()
