import swisseph as swe
import pytz
from datetime import datetime


# returns either rise or set of a specific celestial object in a formatted 24 hour string
# celestial: SUN, MOON
# event: RISE, SET
# year, month, day of when the event will happen, can be left out of parameters to get current day
def celestial_rise_or_set(celestial, event, year=0, month=0, day=0):
    if year == 0 & month == 0 & day == 0:
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    event_result = getRiseSet(year, month, day, celestial, event)
    time_unformatted = utc_hack(event_result)
    return format_24hour_time_output(time_unformatted)


# Not sure what this does, but I think it turns UTC to PST
def utc_hack(date_tup):
    timezone = pytz.timezone('PST8PDT')
    timeUTC = datetime(date_tup[0], date_tup[1], date_tup[2],
                       date_tup[3], date_tup[4], 0, 0, pytz.UTC)
    timeLocal = timeUTC.astimezone(timezone)
    return timeLocal


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


def getDateOfNextFullMoon_UTC(year, month, day):
    """Return the date of the next full moon.
    input/output in UTC time.
    Checks for the first day meeting the requirement for a fullmoon illumination level (99%)
    Checks for brightest hour and minute as well to correct for UTC time conversion."""

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
    return swe.jdut1_to_utc(tjd, swe.GREG_CAL)


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


def getWhenSolEclipseLoc(year, month, day):
    tjdut = swe.julday(year, month, day, 7, swe.GREG_CAL)
    geopos = [-119.4960, 49.8880, 342.0]
    retflags, tret, attr = swe.sol_eclipse_when_loc(
        tjdut, geopos, swe.FLG_SWIEPH, False)

    time = swe.jdet_to_utc(tret[1], swe.GREG_CAL)

    return time


# calculates the moons current illumination
def getMoonStatusHelper(year, month, day):
    jd = swe.julday(year, month, day)
    se_moon = 1
    attr = swe.pheno_ut(jd, se_moon, 1)
    moon_percent = (attr[1] * 100)
    #output = str(output) + "%"
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
        moon_status = " Cibbous"

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
