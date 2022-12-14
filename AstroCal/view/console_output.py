# Astro Calender Console Menu

# Imports
from datetime import datetime, timedelta
import calendar
from gettext import find
from pickle import TRUE
from xmlrpc.client import DateTime
from AstroCal.control import control
import sys
from AstroCal.constants.globals import DATE, LAST_MENU_OPTION
import os
import pytz


# Main Menu
def main_menu(option=None):
    global DATE, LAST_MENU_OPTION
    clear()
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    print("Date Selected: " + get_date_formatted(DATE))
    print('Main Menu')
    print('1. Sun Events')
    print('2. Moon Events')
    print('3. View Solar Month')
    print('4. View Lunar Month')
    print('5. Change Date\n')
    print('6. Exit \n')
    if option == None:
        option = getInputSanitized('Enter selection: ', None, int)
        LAST_MENU_OPTION = option
    else:
        print('Enter selection: ' + str(option))
    if option == 1:
        LAST_MENU_OPTION = None
        sun_menu()
    elif option == 2:
        LAST_MENU_OPTION = None
        moon_menu()
    elif option == 3:
        getMonth()
        input('Press enter to continue...')
        main_menu()
    elif option == 4:
        getLunarMonth()
        input('Press enter to continue...')
        main_menu()
    elif option == 5:
        DATE = getDateFromUser()
        print("\nNew Date: " + get_date_formatted(DATE))
        input('Press enter to continue...')
        main_menu()
    elif option == 6:
        print('Bye')
        sys.exit(0)
    else:
        print('ERROR: not an option')
        LAST_MENU_OPTION = None
        main_menu()
    LAST_MENU_OPTION = None


# sun options
def sun_menu(option=None):
    global LAST_MENU_OPTION
    clear()
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    print('Sun Events')

    print("Date Selected: " + get_date_formatted(DATE))
    #print('1. View Today')
    print('1. Solar Eclipse')
    print('2. Day Lengths\n')
    print('3. Back \n')
    if option == None:
        option = getInputSanitized('Enter selection: ', sun_menu, int)
        LAST_MENU_OPTION = option
    else:
        print('Enter selection: ' + str(option))
    """if option == 1:
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
              " Days: " + str(sun_set_day))"""
    if option == 1:
        sol_eclipse_start, sol_eclipse_max, sol_eclipse_end, sol_eclipse_duration = control.getWhenSolEclipse(
            DATE.year, DATE.month, DATE.day)
        print("Solar Eclipse:")
        print("\tStart:\t\t" + str(sol_eclipse_start))
        print("\tTotality:\t" + str(sol_eclipse_max))
        print("\tEnd:\t\t" + str(sol_eclipse_end))
        print("\tDuration:\t" + str(sol_eclipse_duration))
    elif option == 2:
        amountOfDays = getInputSanitized(
            'Enter amount of days (up to 500). Default is 30 days (enter): ', sun_menu, int, 0, 500, 30)
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
    elif option == 3:
        LAST_MENU_OPTION = None
        main_menu()
    else:
        print('ERROR: not an option')
        input('Press enter to continue...')
        LAST_MENU_OPTION = None
        sun_menu()
    input('Press enter to continue...')
    LAST_MENU_OPTION = None
    main_menu()


# moon options
def moon_menu(option=None):
    global LAST_MENU_OPTION
    clear()
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    print('Moon Events')
    print("Date Selected: " + get_date_formatted(DATE))
    #print('1. View Today')
    print('1. Lunar Eclipse')
    print('2. View Moon Status')
    print('3. Date of Next New Moon')
    print('4. Date of Next Full Moon \n')
    print('5. Back \n')
    if option == None:
        option = getInputSanitized('Enter selection: ', moon_menu, int)
        LAST_MENU_OPTION = option
    else:
        print('Enter selection: ' + str(option))
    """if option == 1:
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
              " Days: " + str(moon_set_day))"""
    if option == 1:
        lun_eclipse_start, lun_eclipse_max, lun_eclipse_end, lun_eclipse_duration = control.getWhenLunEclipse(
            DATE.year, DATE.month, DATE.day)
        print("Lunar Eclipse:")
        print("\tStart:\t\t" + str(lun_eclipse_start))
        print("\tTotality:\t" + str(lun_eclipse_max))
        print("\tEnd:\t\t" + str(lun_eclipse_end))
        print("\tDuration:\t" + str(lun_eclipse_duration))
    elif option == 2:
        moon_status_result = control.getMoonStatus(
            DATE.year, DATE.month, DATE.day)
        print(moon_status_result[0])
        print("Illumination " + str(moon_status_result[1]) + "%")
    elif option == 3:
        dateNewMoon = control.getDateOfNextNewMoon(
            DATE.year, DATE.month, DATE.day)
        print("Next New Moon On: " +
              str(dateNewMoon[0]) + "-" + str(dateNewMoon[1]) + "-" + str(dateNewMoon[2]))
    elif option == 4:
        dateFullMoon = control.getDateOfNextFullMoon_UTC(
            DATE.year, DATE.month, DATE.day)
        print("Next Full Moon On: " +
              str(dateFullMoon[0]) + "-" + str(dateFullMoon[1]) + "-" + str(dateFullMoon[2]))
    elif option == 5:
        LAST_MENU_OPTION = None
        main_menu()
    else:
        print('ERROR: not an option')
        input('Press enter to continue...')
        LAST_MENU_OPTION = None
        moon_menu()
    input('Press enter to continue...')
    LAST_MENU_OPTION = None
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

    # Print Out headers
    print("{:<20} | {:<8} | {:<8} | {:<8} | {:<8} | {:<20} | {:<8}".format(
        "Date", "Sunrise", "Sunset", "Moonrise", "Moonset", "Moon Phase", "Day"))
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
        moon_status, moon_illumin = control.getMoonStatus(year, month, day)
        day_name = datetime(year, month, day).strftime("%a")
        date = "{} {} {}, {}".format(day_name, month_str, day, year)

        print("{:<20} | {:<8} | {:<8} | {:<8} | {:<8} | {:<20} | {:<8}".format(
            date,
            format_24hour_time_output(sun_rise_time),
            format_24hour_time_output(sun_set_time),
            format_24hour_time_output(moon_rise_time),
            format_24hour_time_output(moon_set_time),
            str(moon_illumin) + "%, " + moon_status,
            (same_day if day == sun_rise_day else "Sunrise " + next_day + " ") + (same_day if day == sun_set_day else "Sunset " + next_day + " ") +
            (same_day if day == moon_rise_day else "Moonrise " + next_day +
             " ") + (same_day if day == moon_set_day else "Moonset " + next_day),
        ))

# Get Lunar Month
def getLunarMonth():
    """
        Print out the lunar month.
        Starts at the previous new moon and goes to the end of the current gregorian calendar month.
    """
    month = DATE.month
    year = DATE.year
    same_day = ""
    next_day = "Next Day"

    # Get previous new moon
    curr_time = datetime(DATE.year, DATE.month, DATE.day)
    # curr_time = datetime(2004, 11, 8)
    start_month = curr_time.month

    # Find the previous new moon. We'll start from the first of the lunar month.
    buffer_days = timedelta(days=32)
    while (curr_time.month == start_month):
        earlier_fortnight = curr_time - buffer_days
        previous_new_moon = control.getDateOfNextNewMoon(earlier_fortnight.year, earlier_fortnight.month, earlier_fortnight.day)
        prev_new_date = datetime(previous_new_moon[0], previous_new_moon[1], previous_new_moon[2], previous_new_moon[3], previous_new_moon[4], int(previous_new_moon[5]), 0, pytz.utc)
        curr_time = prev_new_date # - timedelta(hours=5)

    # distance_to_current = curr_time - prev_new_date

    # Get next new moon
    next_new_moon = control.getDateOfNextNewMoon(curr_time.year, curr_time.month, curr_time.day+1)
    next_new_moon_utc = datetime(next_new_moon[0], next_new_moon[1], next_new_moon[2], next_new_moon[3], next_new_moon[4], int(next_new_moon[5]), 0, pytz.utc)

    # Get next full moon
    next_full_moon = control.getDateOfNextFullMoon_UTC(curr_time.year, curr_time.month, curr_time.day+1)
    next_full_moon_utc = datetime(next_full_moon[0], next_full_moon[1], next_full_moon[2], next_full_moon[3], next_full_moon[4], int(next_full_moon[5]), 0, pytz.utc)

    curr_time = curr_time.astimezone(pytz.timezone('PST8PDT'))
    lunar_day = 0;
    fortnight_str = "Shukla paksha"

    # Print Out headers
    print("{:<20} | {:>9} | {:<14} | {:<8} | {:<8} | {:<20} | {:<8}".format(
        "Date", "Lunar Day", "Fortnight", "Moonrise", "Moonset", "Moon Phase", "Day"))
    # Print out info for each day in the month
    delta = timedelta(hours=16)
    while curr_time.month <= start_month:

        # Fast forward to next moon set. This places us after any lunar event
        hour_fraction = 0 if curr_time.minute == 0 else (60 / curr_time.minute)
        result = control.getRiseSet(curr_time.year, curr_time.month, curr_time.day, 'MOON', 'SET', curr_time.hour + hour_fraction)
        curr_time = datetime(result[0], result[1], result[2], result[3], result[4], 0, 0, pytz.utc)
        lunar_day += 1

        # Check if we've hit a full moon
        if curr_time > next_full_moon_utc:
            lunar_day = 1
            next_full_moon = control.getDateOfNextFullMoon_UTC(curr_time.year, curr_time.month, curr_time.day+4)
            next_full_moon_utc = datetime(next_full_moon[0], next_full_moon[1], next_full_moon[2], next_full_moon[3], next_full_moon[4], int(next_full_moon[5]), 0, pytz.utc)
            fortnight_str = "Krishna paksha"
        
        ## Check if we've hit a new moon
        elif curr_time > next_new_moon_utc:
            lunar_day = 1
            next_new_moon = control.getDateOfNextNewMoon(curr_time.year, curr_time.month, curr_time.day+4)
            next_new_moon_utc = datetime(next_new_moon[0], next_new_moon[1], next_new_moon[2], next_new_moon[3], next_new_moon[4], int(next_new_moon[5]), 0, pytz.utc)
            fortnight_str = "Shukla paksha"

        
        # Get regular moon events for the day
        curr_time = curr_time.astimezone(pytz.timezone('PST8PDT'))
        moon_rise_time, moon_rise_day = control.celestial_rise_or_set(
            'MOON', 'RISE', curr_time.year, curr_time.month, curr_time.day)
        moon_set_time, moon_set_day = control.celestial_rise_or_set(
            'MOON', 'SET', curr_time.year, curr_time.month, curr_time.day)
        moon_status, moon_illumin = control.getMoonStatus(curr_time.year, curr_time.month, curr_time.day)

        # Since we start at the start of the lunar month, we need to check if we're in the current gregorian month
        if curr_time.month == start_month:
            print("{:<20} | {:>9} | {:<14} | {:<8} | {:<8} | {:<20} | {:<8}".format(
                "{} {}, {}".format(curr_time.strftime("%B"), curr_time.day, curr_time.year),
                str(lunar_day),
                fortnight_str,
                format_24hour_time_output(moon_rise_time),
                format_24hour_time_output(moon_set_time),
                str(moon_illumin) + "%, " + moon_status,
                (same_day if curr_time.day == moon_rise_day else "Moonrise " + next_day +
                " ") + (same_day if curr_time.day == moon_set_day else "Moonset " + next_day)
            ))
             
        # Move to next lunar day
        curr_time = curr_time + delta

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
    now = datetime.now()
    year = getInputSanitized(
        'Enter a year between 1000 and 3000. Default is current year (enter): ', None, int, 1000, 3000, now.year)
    month = getInputSanitized(
        'Enter a month between 1 and 12. Default is current month (enter): ', None, int, 1, 12, now.month)
    days_in_month = calendar.monthrange(year, month)[1]
    day = getInputSanitized('Enter a day between 1 and ' + str(days_in_month) +
                            '. Default is current day (enter): ', None, int, 1, days_in_month, now.day)
    # Needs sanitizing for 31 days or 30 days
    # Needs sanitizing for input types
    # Year needs to be within a range
    return datetime(year, month, day)


# Sanitizes input by requesting fpr inputType
# message = message to display to user when asking for input
# menu = menu that will show up after input fails. main_menu by default
# inputType = declared by developer: (int, float, str). str by default
# min = minimum value expected by the users input
# max = maximum value expected by the users input
def getInputSanitized(message=None, menu=None, input_type=None, min=None, max=None, default_user_input=None):
    global LAST_MENU_OPTION
    get_input_success = True
    if message == None:  # Default message to user'
        message = "Please enter input: "
    if menu == None:  # Default menu to re-display
        menu = main_menu
    # Get Input
    user_input = getInput(message)
    # Input is empty
    if user_input == '' and default_user_input != None:
        user_input = default_user_input
    elif user_input == '':
        print("You entered nothing.")
        get_input_success = False
    # Input is wrong type
    if input_type != None and get_input_success != False:
        get_input_success = checkInputType(user_input, input_type)
        if get_input_success == True:
            # converts input from str to input_type
            user_input = input_type(user_input)
    # Input is in range
    if min != None and max != None and get_input_success != False and input_type != None:
        get_input_success = restrictInputToRangeInclusive(
            user_input, min, max)
    # All tests pass
    if get_input_success == True:
        return user_input
    else:
        input('Press enter to continue...')
        menu(LAST_MENU_OPTION)


# Raw input from user
def getInput(message):
    return input(message)


# raises exception if input type is wrong
def checkInputType(user_input, input_type):
    try:
        input_type(user_input)
        return True
    except:
        print("ERROR: Incorrect input type. Please try again.")
        return False


# raises exception if input is not within range
def restrictInputToRangeInclusive(user_input, min, max):
    if user_input < min or user_input > max:
        print("ERROR: Please type a number between (" +
              str(min) + "-" + str(max) + ").")
        return False
    return True


# Clears console when called
def clear(): return os.system('cls')
