import swisseph as swe
from datetime import datetime

def test_swe():
    print("Hello World!")
    #jd = swe.julday(2007, 3, 3)
    #res = swe.lun_eclipse_when(jd)
    #ecltime = swe.revjul(res[1][0])
    # print(ecltime)
    #print(getDaysTillFullMoon(2022, 10, 12))
    #Test for days till full moon
    for i in range(1,13):
        #print(getDateOfNextFullMoon_UTC(2022, i, 1))
        print(str(getDaysTillFullMoon(2022, i, 1, -7)))


def getRiseSet(year, month, day, celestial, status):
    constCel = swe.SUN
    if(celestial == 'MOON'):
        constCel = swe.MOON

    constStatus = swe.CALC_RISE
    if(status == 'SET'):
        constStatus = swe.CALC_SET

    tjd = swe.julday(year, month, day, 7, swe.GREG_CAL)  # julian day

    res, tret = swe.rise_trans(tjd, constCel, constStatus,
                               (-119.4960, 49.8880, 342.0), 0, 0, swe.FLG_SWIEPH)  # Coordiantes are hardcoded for now

    if (res != 0):
        return None

    utcTime = swe.jdut1_to_utc(tret[0], swe.GREG_CAL)

    return utcTime

    # print('moonrise: %d/%02d/%02d %d:%d UTC' %
    #       (y, m, d, h, mi))

    # timezone = pytz.timezone('PST8PDT')
    # timeUTC = datetime.datetime(y, m, d, h, mi, 0, 0, pytz.UTC)
    # print(timeUTC)

    # timeLocal = timeUTC.astimezone(timezone)
    # print(timeLocal)

def getDateOfNextFullMoon_UTC(year, month, day):
    """Return the date of the next full moon.
    input/output in UTC time.
    Checks for the first day meeting the requirement for a fullmoon illumination level (99%)
    Checks for brightest hour and minute as well to correct for UTC time conversion."""
    
    #Converts UTC time into julian day number
    tjd = swe.julday(year, month, day, 0, swe.GREG_CAL)
    #Get the illumination of the moon (variable: illum) of the starting day to check if it is a full moon
    res = swe.pheno_ut(tjd, swe.MOON)
    illum = res[1]

    #Compare the illumintation of the moon to a threshold (0.990) and get the first day
    #since the starting day where the threshold is met, this indicates full moon
    daysCount = 0
    #Find the first day that meets the illumination requirement.
    while(round(illum,3) < 0.990):
        daysCount += 1
        tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
        res = swe.pheno_ut(tjd, swe.MOON)
        illum = res[1]
    
    #Full moon happens at a speciifc hour and minute during the day
    #We get this specific to make sure the timezone conversions will be accurate
    #Note: the mintues seem to be a little off when caompared to online sources

    #Get the hour with the brightest illumination
    tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
    max = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = max
    hour = 0.0
    #Find the brightest hour in that day
    while(temp > max and hour < 23):
        hour += 1.0
        tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if(temp > max):
            max = temp

    #Get the minute with the brightest illumination
    tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
    max = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = max
    minute = 0.0
    #Find the brightest minute
    while(temp >= max):
        minute += 0.017
        tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if(temp > max):
            max = temp

    tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
    return swe.jdut1_to_utc(tjd, swe.GREG_CAL)



def getDaysTillFullMoon(year, month, day, timezone):
    """Gets days till next full moon based on entered date and timezone offset """
    year_utc, month_utc, day_utc, _, _, _ = swe.utc_time_zone(year, month, day, 0, 0, 0, timezone)
    #Returns the UTC time and date of the next full moon as a tuple
    fmoon_year_utc,fmoon_month_utc,fmoon_day_utc,fmoon_hours_utc,fmoon_minutes_utc,_ = getDateOfNextFullMoon_UTC(year_utc, month_utc, day_utc)
    #Converts the full moon UTC date to the local timezone
    local_time = swe.utc_time_zone(fmoon_year_utc, fmoon_month_utc, fmoon_day_utc, fmoon_hours_utc, fmoon_minutes_utc, 0, -timezone)
    #Subtract the next full moon date from the current day to retrieve the days till.

    startDate = datetime(year, month, day)
    endDate = datetime(local_time[0], local_time[1], local_time[2])
    diff = abs(endDate-startDate).days
    #Returns daysuntil next full moon
    return diff
    
def getWhenSolEclipseLoc(year, month, day):
    tjdut = swe.julday(year, month, day, 7, swe.GREG_CAL)
    geopos = [-119.4960,49.8880, 342.0] 
    retflags,tret,attr = swe.sol_eclipse_when_loc(tjdut,geopos,swe.FLG_SWIEPH,False)
    
    time = swe.jdet_to_utc(tret[1],swe.GREG_CAL)
    #print("The eclipse occured on" + str(time) + "\n year,month,date,hour,minute,seconds")
    
    return time


def getWhenLunEclipseLoc(year, month, day):
    tjdut = swe.julday(year, month, day, 7, swe.GREG_CAL)
    geopos = [-119.4960,49.8880, 342.0] 
    retflags,tret,attr = swe.lun_eclipse_when_loc(tjdut,geopos,swe.FLG_SWIEPH,False)
    
    time = swe.jdet_to_utc(tret[1],swe.GREG_CAL)
    #print("The eclipse occured on" + str(time) + "\n year,month,date,hour,minute,seconds")
    
    return time


#calculates the moons current illumination
def getMoonStatusHelper(year, month, day):
	jd = swe.julday(year, month, day)
	se_moon = 1
	attr = 	swe.pheno_ut(jd, se_moon, 1)
	moon_percent = (attr[1] * 100)
	#output = str(output) + "%"
	return moon_percent

#uses getMoonStatusHelper to display current phases of the moon
def getMoonStatus():
    now = datetime.now()
    attr = getMoonStatusHelper(now.year, now.month, now.day)
    next_day_percent = getMoonStatusHelper(now.year, now.month, now.day+1)
    moon_status = ""
    if round(attr) < 49:
        moon_status = " Crescent"
    elif round(attr) > 51:
        moon_status = " Cibbous"

    if attr < next_day_percent:
        print("Waxing" + moon_status)
    elif attr > next_day_percent:
        print("Wanning" + moon_status)
    elif round(attr) == 100:
        print("Full Moon")
    elif round(attr) == 0:
        print("New Moon")

    moon_percent = round(attr)
    print("Illumination " + str(moon_percent) + "%")

def getDateOfNextNewMoon(year, month, day):
    """Return the date of the next new moon.
    input/output in UTC time.
    Checks for the first day meeting the requirement for a new moon illumination level (~0%)
    Checks for dimmest hour and minute as well to correct for UTC time conversion."""
    
    #Converts UTC time into julian day number
    tjd = swe.julday(year, month, day, 0, swe.GREG_CAL)
    #Get the illumination of the moon (variable: illum) of the starting day to check if it is a new moon
    res = swe.pheno_ut(tjd, swe.MOON)
    illum = res[1]

    #Compare the illumintation of the moon to a threshold (0.005) and get the first day
    #since the starting day where the threshold is met, this indicates new moon
    daysCount = 0
    #Find the first day that meets the illumination requirement.
    while(round(illum,3) > 0.005):
        daysCount += 1
        tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
        res = swe.pheno_ut(tjd, swe.MOON)
        illum = res[1]
        
    
    #New moon happens at a speciifc hour and minute during the day
    #We get this specific to make sure the timezone conversions will be accurate
    #Note: the mintues seem to be a little off when c0mpared to online sources

    #Get the hour with the dimmest illumination
    tjd = swe.julday(year, month, day+daysCount, 0, swe.GREG_CAL)
    min = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = min
    hour = 0.0
    #Find the dimmest hour in that day
    while(temp < min and hour < 23):
        hour += 1.0
        tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if(temp < min):
            min = temp

    #Get the minute with the dimmest illumination
    tjd = swe.julday(year, month, day+daysCount, hour, swe.GREG_CAL)
    min = swe.pheno_ut(tjd, swe.MOON)[1]
    temp = min
    minute = 0.0
    #Find the dimmest minute
    while(temp < min):
        minute += 0.017
        tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
        temp = swe.pheno_ut(tjd, swe.MOON)[1]
        if(temp < min):
            min = temp

    tjd = swe.julday(year, month, day+daysCount, hour+minute, swe.GREG_CAL)
    utc = swe.jdut1_to_utc(tjd, swe.GREG_CAL)
    newMoon_year, newMoon_month, newMoon_day = utc[0], utc[1], utc[2]
    return (newMoon_year, newMoon_month, newMoon_day)