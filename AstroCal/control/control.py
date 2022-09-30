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
<<<<<<< HEAD
    """Return the date of the next full moon.
    input/output in UTC time.
    Checks for the first day meeting the requirement for a fullmoon illumination level (99%)
    Checks for brightest hour and minute as well to correct for UTC time conversion."""
=======
    #Converts UTC time into julian day number
>>>>>>> 270e5e4f07d2759ea70b8f70a6b09dbaf03fbf2e
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
<<<<<<< HEAD
    """Gets days till next full moon based on entered date and timezone offset """
    year_utc, month_utc, day_utc, _, _, _ = swe.utc_time_zone(year, month, day, 0, 0, 0, timezone)
    #Returns the UTC time and date of the next full moon as a tuple
    fmoon_year_utc,fmoon_month_utc,fmoon_day_utc,fmoon_hours_utc,fmoon_minutes_utc,_ = getDateOfNextFullMoon_UTC(year_utc, month_utc, day_utc)
    #Converts the full moon UTC date to the local timezone
    local_time = swe.utc_time_zone(fmoon_year_utc, fmoon_month_utc, fmoon_day_utc, fmoon_hours_utc, fmoon_minutes_utc, 0, -timezone)
    #Subtract the next full moon date from the current day to retrieve the days till.
=======
    #Convert Local time into UTC
    utc_time = swe.utc_time_zone(year, month, day, 0, 0, 0, timezone)
    year_utc = utc_time[0]
    month_utc = utc_time[1]
    day_utc = utc_time[2]
    #Pass UTC Time into the which return the date of the next full moon down to the minute
    date_utc = getDateOfNextFullMoon_UTC(year_utc, month_utc, day_utc)
    year_utc = date_utc[0]
    month_utc = date_utc[1]
    day_utc = date_utc[2]
    hours_utc = date_utc[3]
    minutes_utc = date_utc[4]
    #Convert UTC time back into local time
    local_time = swe.utc_time_zone(year_utc, month_utc, day_utc, hours_utc, minutes_utc, 0, -timezone)
    #Convert local start and local time of next full moon into datetime objects. Subtract time to get the difference in days
>>>>>>> 270e5e4f07d2759ea70b8f70a6b09dbaf03fbf2e
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
test_swe()
     
