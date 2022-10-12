from time import time
import swisseph as swe
import pytz
import sqlite3
from sqlite3 import Error
from datetime import datetime
from array import *

# Global tuple to save the currently called location. Interacts with getLocation and getLocationTest
# Uncomment the function call at the bottom to use the getLocation tests
LOCATION = ()

# returns either rise or set of a specific celestial object in a formatted 24 hour string
# celestial: SUN, MOON
# event: RISE, SET
# year, month, day of when the event will happen, can be left out of parameters to get current day
# Returns time_unformatted and the day the event happens on


def celestial_rise_or_set(celestial, event, year=None, month=None, day=None):
    if ((year == None)) & ((month == None)) & ((day == None)):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    event_result = getRiseSet(year, month, day, celestial, event)
    time_unformatted = utc_hack(event_result)
    return time_unformatted, time_unformatted.day


# Turns tuplet into usable DateTime object
def utc_hack(date_tup):
    timezone = pytz.timezone('PST8PDT')
    timeUTC = datetime(date_tup[0], date_tup[1], date_tup[2],
                       date_tup[3], date_tup[4], 0, 0, pytz.UTC)
    timeLocal = timeUTC.astimezone(timezone)
    return timeLocal


# gets the raw DateTime object of rise or set of a celestial object
def getRiseSet(year, month, day, celestial, status):
    constCel = swe.SUN
    if (celestial == 'MOON'):
        constCel = swe.MOON

    constStatus = swe.CALC_RISE
    if (status == 'SET'):
        constStatus = swe.CALC_SET

    tjd = swe.julday(year, month, day, 7, swe.GREG_CAL)  # julian day

    res, tret = swe.rise_trans(tjd, constCel, constStatus,
                               (-119.4960, 49.8880, 342.0), 0, 0, swe.FLG_SWIEPH)  # Coordinates are hardcoded for now

    # res: 0 = Event found, -2 Event not found because the object is circumpolar
    if (res != 0):
        return None

    utcTime = swe.jdut1_to_utc(tret[0], swe.GREG_CAL)

    return utcTime


def getDateOfNextFullMoon_UTC(year=None, month=None, day=None):
    """Return the date of the next full moon.
    input/output in UTC time.
    Checks for the first day meeting the requirement for a fullmoon illumination level (99%)
    Checks for brightest hour and minute as well to correct for UTC time conversion."""

    if (year == None) & (month == None) & (day == None):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    # Converts UTC time into julian day number
    tjd = swe.julday(year, month, day, 0, swe.GREG_CAL)
    # Get the illumination of the moon (variable: illum) of the starting day to check if it is a full moon
    res = swe.pheno_ut(tjd, swe.MOON)
    illum = res[1]

    # Compare the illumintation of the moon to a threshold (0.990) and get the first day
    # since the starting day where the threshold is met, this indicates full moon
    daysCount = 0
    # Find the first day that meets the illumination requirement.
    while (round(illum, 3) < 0.990):
        daysCount += 1
        tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
        res = swe.pheno_ut(tjd, swe.MOON)
        illum = res[1]

    # Full moon happens at a speciifc hour and minute during the day
    # We get this specific to make sure the timezone conversions will be accurate
    # Note: the mintues seem to be a little off when caompared to online sources

    # Get the hour with the brightest illumination
    tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
    max = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = max
    hour = 0.0
    # Find the brightest hour in that day
    while (temp > max and hour < 23):
        hour += 1.0
        tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if (temp > max):
            max = temp

    # Get the minute with the brightest illumination
    tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
    max = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = max
    minute = 0.0
    # Find the brightest minute
    while (temp >= max):
        minute += 0.017
        tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if (temp > max):
            max = temp

    tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
    utc_time = swe.jdut1_to_utc(tjd, swe.GREG_CAL)
    return (utc_time[0], utc_time[1], utc_time[2])


def getDaysTillFullMoon(year, month, day, timezone):
    """Gets days till next full moon based on entered date and timezone offset """
    year_utc, month_utc, day_utc, _, _, _ = swe.utc_time_zone(
        year, month, day, 0, 0, 0, timezone)
    # Returns the UTC time and date of the next full moon as a tuple
    fmoon_year_utc, fmoon_month_utc, fmoon_day_utc, fmoon_hours_utc, fmoon_minutes_utc, _ = getDateOfNextFullMoon_UTC(
        year_utc, month_utc, day_utc)
    # Converts the full moon UTC date to the local timezone
    local_time = swe.utc_time_zone(fmoon_year_utc, fmoon_month_utc,
                                   fmoon_day_utc, fmoon_hours_utc, fmoon_minutes_utc, 0, -timezone)
    # Subtract the next full moon date from the current day to retrieve the days till.

    startDate = datetime(year, month, day)
    endDate = datetime(local_time[0], local_time[1], local_time[2])
    diff = abs(endDate-startDate).days
    # Returns daysuntil next full moon
    return diff


# Gets string of data relating to time of solar eclipse
# Returns tuple (start of eclipse, peak of eclipse, end of eclipse, duration of eclipse)
def getWhenSolEclipseLoc(year=None, month=None, day=None):
    if (year == None) & (month == None) & (day == None):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    tjdut = swe.julday(year, month, day, 7, swe.GREG_CAL)
    geopos = [-119.4960, 49.8880, 342.0]
    retflags, tret, attr = swe.sol_eclipse_when_loc(
        tjdut, geopos, swe.FLG_SWIEPH, False)

    timeEclipseStart = swe.jdut1_to_utc(tret[1], swe.GREG_CAL)
    timeEclipseEnd = swe.jdut1_to_utc(tret[4], swe.GREG_CAL)
    timeEclipseMax = swe.jdut1_to_utc(tret[0], swe.GREG_CAL)

    # convert swisseph time to local time object
    time_formatted_start = utc_hack(timeEclipseStart)
    time_formatted_end = utc_hack(timeEclipseEnd)
    time_formatted_max = utc_hack(timeEclipseMax)

    # calculate duration of eclipse
    timeEclipseDuration = time_formatted_end - time_formatted_start

    return (time_formatted_start, time_formatted_max, time_formatted_end, timeEclipseDuration)


# Gets string of data relating to time of Lunar eclipse
# Returns tuple (start of eclipse, peak of eclipse, end of eclipse, duration of eclipse)
def getWhenLunEclipseLoc(year=None, month=None, day=None):
    if (year == None) & (month == None) & (day == None):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    tjdut = swe.julday(year, month, day, 7, swe.GREG_CAL)
    geopos = [-119.4960, 49.8880, 342.0]
    retflags, tret, attr = swe.lun_eclipse_when_loc(
        tjdut, geopos, swe.FLG_SWIEPH, False)

    timeEclipseStart = swe.jdut1_to_utc(tret[6], swe.GREG_CAL)
    timeEclipseEnd = swe.jdut1_to_utc(tret[7], swe.GREG_CAL)
    timeEclipseMax = swe.jdut1_to_utc(tret[0], swe.GREG_CAL)

    # convert swisseph time to local time object
    time_formatted_start = utc_hack(timeEclipseStart)
    time_formatted_end = utc_hack(timeEclipseEnd)
    time_formatted_max = utc_hack(timeEclipseMax)

    # calculate duration of eclipse
    timeEclipseDuration = time_formatted_end - time_formatted_start

    return (time_formatted_start, time_formatted_max, time_formatted_end, timeEclipseDuration)


# calculates the moons current illumination
def getMoonStatusHelper(year, month, day):
    jd = swe.julday(year, month, day)
    se_moon = 1
    attr = swe.pheno_ut(jd, se_moon, 1)
    moon_percent = (attr[1] * 100)
    return moon_percent


# uses getMoonStatusHelper to display current phases of the moon
def getMoonStatus():
    now = datetime.now()
    moon_percent = getMoonStatusHelper(now.year, now.month, now.day)
    next_day_percent = getMoonStatusHelper(now.year, now.month, now.day+1)
    moon_status = ""
    if round(moon_percent) < 49:
        moon_status = " Crescent"
    elif round(moon_percent) > 51:
        moon_status = " Gibbous"

    if moon_percent < next_day_percent:
        result = "Waxing" + moon_status
    elif moon_percent > next_day_percent:
        result = "Wanning" + moon_status
    elif round(moon_percent) == 100:
        result = "Full Moon"
    elif round(moon_percent) == 49 or 50 or 51:
        result = "Half Moon"
    elif round(moon_percent) == 0:
        result = "New Moon"

    moon_percent_rounded = round(moon_percent)
    return result, "Illumination " + str(moon_percent_rounded) + "%"


def getVariableDayLength(year, month, day, amountOfDays):
    """Return 2d array with amount of hours and minutes per day from current day to specified amount of days
    """
    amountOfDayLight = []

    for i in range(0, amountOfDays):
        daySunRise = getRiseSet(year, month, day + i, 'SUN', 'RISE')
        daySunSet = getRiseSet(year, month, day + i, 'SUN', 'SET')
        # convert to datetime object to perfrom difference
        dayRiseTime = datetime(
            daySunRise[0], daySunRise[1], daySunRise[2], daySunRise[3], daySunRise[4], int(daySunRise[5]))
        daySetTime = datetime(
            daySunSet[0], daySunSet[1], daySunSet[2], daySunSet[3], daySunSet[4], int(daySunSet[5]))

        # get difference between sunrise and and sunset
        timeDiff = abs(daySetTime-dayRiseTime)
        # convert time difference into seconds
        seconds = timeDiff.seconds
        # convert seconds into total hours
        dayLightHours = (seconds / 60) / 60
        # extract remainder of minutes
        dayLightHoursRemainder = dayLightHours % 1
        outputHours = int(dayLightHours // 1)
        outputMinutes = round(dayLightHoursRemainder * 60)
        # Adds 0 and if hour or minute is single digit, and convert to string
        if outputHours < 10:
            outputHours = "0" + str(outputHours)
        else:
            outputHours = str(outputHours)
        if outputMinutes < 10:
            outputMinutes = "0" + str(outputMinutes)
        else:
            outputMinutes = str(outputMinutes)
        # append hours and minutes to 2d array
        amountOfDayLight.append([outputHours, outputMinutes])

    return amountOfDayLight


def getDateOfNextNewMoon(year=None, month=None, day=None):
    """Return the date of the next new moon.
    input/output in UTC time.
    Checks for the first day meeting the requirement for a new moon illumination level (~0%)
    Checks for dimmest hour and minute as well to correct for UTC time conversion."""
    if (year == None) & (month == None) & (day == None):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    # Converts UTC time into julian day number
    tjd = swe.julday(year, month, day, 0, swe.GREG_CAL)
    # Get the illumination of the moon (variable: illum) of the starting day to check if it is a new moon
    res = swe.pheno_ut(tjd, swe.MOON)
    illum = res[1]

    # Compare the illumintation of the moon to a threshold (0.005) and get the first day
    # since the starting day where the threshold is met, this indicates new moon
    daysCount = 0
    # Find the first day that meets the illumination requirement.
    while (round(illum, 3) > 0.005):
        daysCount += 1
        tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
        res = swe.pheno_ut(tjd, swe.MOON)
        illum = res[1]

    # New moon happens at a speciifc hour and minute during the day
    # We get this specific to make sure the timezone conversions will be accurate
    # Note: the mintues seem to be a little off when c0mpared to online sources

    # Get the hour with the dimmest illumination
    tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
    min = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = min
    hour = 0.0
    # Find the dimmest hour in that day
    while (temp < min and hour < 23):
        hour += 1.0
        tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if (temp < min):
            min = temp

    # Get the minute with the dimmest illumination
    tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
    min = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = min
    minute = 0.0
    # Find the dimmest minute
    while (temp < min):
        minute += 0.017
        tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if (temp < min):
            min = temp

    tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
    utc = swe.jdut1_to_utc(tjd, swe.GREG_CAL)
    newMoon_year, newMoon_month, newMoon_day = utc[0], utc[1], utc[2]
    return (newMoon_year, newMoon_month, newMoon_day)


def getLocation(city, country):
    """
    Connects to the database 'locations.db' in the folder 'resources' and queries the
    database to get the corresponding row and then assign it to the global variable 'location'
    before returning a row of the database in the form of a tuple.

    Table Columns:
    1: 'City' as a string
    2: 'Country' as a string
    3: 'Elevation' (in meters) as an int
    4: 'Timezone' as a string
    5: 'Latitude' as a float
    6: 'Longitude' as a float
    """
    # Assigns database path/name to the variable
    database = "../AstroCal/resources/locations.db"
    # Checks if the user has inputed England, Wales or Scotland, as the database saves them all as UK
    # Ireland is a seperate entry from the other three countries
    if country == "England" or country == "Wales" or country == "Scotland":
        country = "United Kingdom"

    # Declares a connection to the database, None and the try and except are to minimize faulty calls
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    # Checks that the connection is properly established, creates a cursor and then uses it to run a query on the database
    with conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM geonamesLocations WHERE city=? AND country=?", (city, country,))
    # Gets the first row of the query and assigns it to 'row' and global variable 'location' before it is returned
    row = cur.fetchone()
    global LOCATION
    LOCATION = row
    return row


def getLocationTest():
    """
    'Unit' tests as Fred, Mitchell and I discovered that trying to access a database from unit tests needs more work than it would be worth.
    For in house testing, this will work and can be deleted before the product is delivered.

    Function below commented out until needed. All tests pass at time of writing.
    """
    # Prints a full row from the table
    print((f"A full row of the locations table looks like: %s" %
          (getLocation("Madrid", "Spain"),)))
    # Checks that the first item (City) returned is accurate
    if getLocation("Riyadh", "Saudi Arabia")[0] == "Riyadh":
        print("City test for Riyadh, Saudi Arabia passed. City is " +
              getLocation("Riyadh", "Saudi Arabia")[0] + ".")
    # Checks that the second item (Country) returned is accurate
    if getLocation("Sydney", "Australia")[1] == "Australia":
        print("Country test for Sydney, Australia passed. Country is " +
              getLocation("Sydney", "Australia")[1] + ".")
    # Checks that the third item (Elevation) returned is accurate
    if getLocation("Vancouver", "Canada")[2] == 70:
        print("Elevation test for Vancouver, Canada passed. Elevation is " +
              str(getLocation("Vancouver", "Canada")[2]) + "m.")
    # Checks that the fourth item (Timezone) returned is accurate
    if getLocation("Rio de Janeiro", "Brazil")[3] == "America/Sao_Paulo":
        print("Timezone test for Rio de Janeiro, Brazil passed. Timezone is " +
              getLocation("Rio de Janeiro", "Brazil")[3] + ".")
    # Checks that the fifth item (Latitude) returned accurate
    if getLocation("Paris", "France")[4] == 48.8534:
        print("Latitude test for Paris, France passed. Latitude is " +
              str(getLocation("Paris", "France")[4]) + ".")
    # Checks that the fifth item (Longitude) returned accurate
    if getLocation("Tokyo", "Japan")[5] == 139.6917:
        print("Latitude test for Tokyo, Japan passed. Longitude is " +
              str(getLocation("Tokyo", "Japan")[5]) + ".")
    # Checks that the global variable is being updated upon getLocation() call
    if getLocation("New York", "United States") == LOCATION:
        print("Global variable test passed.")

# getLocationTest() #Uncomment function to run test for the getLocation function
