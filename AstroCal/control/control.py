import swisseph as swe


def test_swe():
    jd = swe.julday(2007, 3, 3)
    res = swe.lun_eclipse_when(jd)
    ecltime = swe.revjul(res[1][0])
    print(ecltime)


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

    
def getWhenSolEclipseLoc(year, month, day):
    tjdut = swe.julday(year, month, day, 7, swe.GREG_CAL)
    geopos = [-119.4960,49.8880, 342.0] 
    retflags,tret,attr = swe.sol_eclipse_when_loc(tjdut,geopos,swe.FLG_SWIEPH,False)
    
    time = swe.jdet_to_utc(tret[1],swe.GREG_CAL)
    #print("The eclipse occured on" + str(time) + "\n year,month,date,hour,minute,seconds")
    
    return time
#TODO complete the unit test for peer review
     

print(getWhenSolEclipseLoc(2022,9,27))

