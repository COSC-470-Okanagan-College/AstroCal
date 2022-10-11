# Astro Calender Console Menu

# Imports
from datetime import datetime, timedelta
from gettext import find
from control import control
import sys
from constants.globals import DATE


# Main Menu
def main_menu():
    global DATE
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    print("Date Selected: " + get_date_formatted(DATE))
    print('1. Sun Events')
    print('2. Moon Events')
    print('3. View Month')
    print('4. Change Date')
    print('5. exit \n')
    option = int(input('Enter selection: '))
    if option == 1:
        sun_menu()
    elif option == 2:
        moon_menu()
    elif option == 3:
        getMonth()
    elif option == 4:
        DATE = getDateFromUser()
        print("New Date: " + get_date_formatted(DATE))
        input('Press enter to continue...')
        main_menu()
    elif option == 5:
        print('Bye')
        sys.exit(0)
    else:
        print('error not an option')
        main_menu()


# sun options
def sun_menu():
    print('Sun Events')
    print("Date Selected: " + get_date_formatted(DATE))
    print('1. View Today')
    print('2. Solar Eclipse')
    print('3. Day Lengths')
    print('4. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        # Displays current date
        print(get_date_formatted(DATE))
        # call function name for moon rise
        sun_rise_time, sun_rise_day = control.celestial_rise_or_set(
            'SUN', 'RISE', DATE.year, DATE.month, DATE.day)
        print('Sun will Rise: ' + format_24hour_time_output(sun_rise_time) +
              " Days: " + str(sun_rise_day))
        # call function name for moon set
        sun_set_time, sun_set_day = control.celestial_rise_or_set(
            'SUN', 'SET', DATE.year, DATE.month, DATE.day)
        print('Sun will Set : ' + format_24hour_time_output(sun_set_time) +
              " Days: " + str(sun_set_day))
    elif option == 2:
        sol_eclipse_start, sol_eclipse_max, sol_eclipse_end, sol_eclipse_duration = control.getWhenSolEclipseLoc(
            DATE.year, DATE.month, DATE.day)
        print("Solar Eclipse:")
        print("\tStart:\t\t" + str(sol_eclipse_start))
        print("\tTotality:\t" + str(sol_eclipse_max))
        print("\tEnd:\t\t" + str(sol_eclipse_end))
        print("\tDuration:\t" + str(sol_eclipse_duration))
    elif option == 3:
        amountOfDays = int(input('Enter amount of days: '))
        currentDay = DATE
        dayLengths = control.getVariableDayLength(
            amountOfDays, DATE.year, DATE.month, DATE.day)
        for i in range(0, amountOfDays):
            currentDay = DATE
            currentDay += timedelta(days=i)

            sun_rise_time = control.celestial_rise_or_set(
                'SUN', 'RISE', currentDay.year, currentDay.month, currentDay.day)[0]
            sun_set_time = control.celestial_rise_or_set(
                'SUN', 'SET', currentDay.year, currentDay.month, currentDay.day)[0]

            print("".ljust(40, '='))
            print("{}, {}, {}".format(currentDay.strftime("%B"),
                  currentDay.day, currentDay.year))
            print("".ljust(40, '='))
            print("{:<10} | {:<10} | {:<12}".format(
                'Day Begin', 'Day End', 'Length of Day'))
            print("".ljust(40, '-'))
            print("{:<10} | {:<10} | {:<12}".format(
                format_24hour_time_output(sun_rise_time),
                format_24hour_time_output(sun_set_time),
                str(dayLengths[i][0]) + ":" + str(dayLengths[i][1]) + "hrs" + "\n"))

    elif option == 4:
        main_menu()
    else:
        print('error not an option')
        sun_menu()
    input('Press enter to continue...')
    main_menu()


# moon options
def moon_menu():
    print('Moon Events')
    print("Date Selected: " + get_date_formatted(DATE))
    print('1. View Today')
    print('2. Lunar Eclipse')
    print('3. View Moon Status')
    print('4. Date of Next New Moon')
    print('5. Date of Next Full Moon \n')
    print('6. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        # Displays current date
        print(get_date_formatted(DATE))
        # call function name for moon rise
        moon_rise_time, moon_rise_day = control.celestial_rise_or_set(
            'MOON', 'RISE', DATE.year, DATE.month, DATE.day)
        print('Moon will Rise: ' + format_24hour_time_output(moon_rise_time) +
              " Days: " + str(moon_rise_day))
        # call function name for moon set
        moon_set_time, moon_set_day = control.celestial_rise_or_set(
            'MOON', 'SET', DATE.year, DATE.month, DATE.day)
        print('Moon will Set : ' + format_24hour_time_output(moon_set_time) +
              " Days: " + str(moon_set_day))
    elif option == 2:
        lun_eclipse_start, lun_eclipse_max, lun_eclipse_end, lun_eclipse_duration = control.getWhenLunEclipseLoc(
            DATE.year, DATE.month, DATE.day)
        print("Lunar Eclipse:")
        print("\tStart:\t\t" + str(lun_eclipse_start))
        print("\tTotality:\t" + str(lun_eclipse_max))
        print("\tEnd:\t\t" + str(lun_eclipse_end))
        print("\tDuration:\t" + str(lun_eclipse_duration))
    elif option == 3:
        moon_status_result = control.getMoonStatus(
            DATE.year, DATE.month, DATE.day)
        print(moon_status_result[0])
        print(moon_status_result[1])
    elif option == 4:
        dateNewMoon = control.getDateOfNextNewMoon(
            DATE.year, DATE.month, DATE.day)
        print("Next New Moon On: " +
              str(dateNewMoon[0]) + "-" + str(dateNewMoon[1]) + "-" + str(dateNewMoon[2]))
    elif option == 5:
        dateFullMoon = control.getDateOfNextFullMoon_UTC(
            DATE.year, DATE.month, DATE.day)
        print("Next Full Moon On: " +
              str(dateFullMoon[0]) + "-" + str(dateFullMoon[1]) + "-" + str(dateFullMoon[2]))
    elif option == 6:
        main_menu()
    else:
        print('error not an option')
        sun_menu()
    input('Press enter to continue...')
    main_menu()


# Displays the overall output for each day of the current month
def getMonth():
    # Get Current Month & Year
    month_str = DATE.strftime("%B")
    month = DATE.month
    year = DATE.year
    same_day = ""
    next_day = "Next Day"

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
        sun_rise_time, sun_rise_day = control.celestial_rise_or_set(
            'SUN', 'RISE', year, month, day)
        sun_set_time, sun_set_day = control.celestial_rise_or_set(
            'SUN', 'SET', year, month, day)
        moon_rise_time, moon_rise_day = control.celestial_rise_or_set(
            'MOON', 'RISE', year, month, day)
        moon_set_time, moon_set_day = control.celestial_rise_or_set(
            'MOON', 'SET', year, month, day)

        print("".ljust(36, '='))
        print("{} {}, {}".format(month_str, day, year))
        print("".ljust(36, '='))
        print("{:<12} | {:<12} | {:<12}".format("Event", "Time", "Day"))
        print("".ljust(36, '-'))
        print("{:<12} | {:<12} | {:<12}".format(
            "Sunrise", format_24hour_time_output(sun_rise_time),  same_day if day == sun_rise_day else next_day))
        print("{:<12} | {:<12} | {:<12}".format(
            "Sunset", format_24hour_time_output(sun_set_time), same_day if day == sun_set_day else next_day))
        print("{:<12} | {:<12} | {:<12}".format("Moonrise",
              format_24hour_time_output(moon_rise_time), same_day if day == moon_rise_day else next_day))
        print("{:<12} | {:<12} | {:<12}".format(
            "Moonset", format_24hour_time_output(moon_set_time), same_day if day == moon_set_day else next_day))
        print()
    main_menu()


# Get current year, month, day
def get_current_year_month_day():
    now = datetime.now()
    return now.year, now.month, now.day


# get current date
def get_date_formatted(date=0):
    if date == 0:
        date = datetime.now()
    today = date.strftime("%B-%d-%Y  %H:%M \n")
    return today


# Formats any datetime object into 24 hour string
def format_24hour_time_output(time):
    if time.hour < 10:
        hour_str = "0" + str(time.hour)
    else:
        hour_str = str(time.hour)
    if time.minute < 10:
        minute_str = "0" + str(time.minute)
    else:
        minute_str = str(time.minute)
    return hour_str + ':' + minute_str


# Gets date from the user
def getDateFromUser():
    year = int(input('Enter year: '))
    month = int(input('Enter month (1-12): '))
    day = int(input('Enter day (1-31): '))
    # Needs sanitizing for 31 days or 30 days
    # Needs sanitizing for input types
    # Year needs to be within a range
    return datetime(year, month, day)
