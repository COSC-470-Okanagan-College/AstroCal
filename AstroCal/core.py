import swisseph as swe
import sys
import datetime
import pytz


def run():
    print("Hi")


def getRiseSet(year, month, day, celestial, status):
    constCel = swe.SUN
    if(celestial == 'MOON'):
        constCel = swe.MOON

    constStatus = swe.CALC_RISE
    if(status == "SET"):
        constStatus = swe.CALC_SET

    tjd = swe.julday(year, month, day, 0, swe.GREG_CAL)  # julian day

    res, tret = swe.rise_trans(tjd, constCel, constStatus,
                               (-119.4960, 49.8880, 342.0), 0, 0, swe.FLG_SWIEPH)  # Coordiantes are hardcoded for now

    if (res != 0):
        return None

    tset = tret[0]

    utcTime = swe.jdut1_to_utc(trise, swe.GREG_CAL)

    return utcTime

    # print('moonrise: %d/%02d/%02d %d:%d UTC' %
    #       (y, m, d, h, mi))

    # timezone = pytz.timezone('PST8PDT')
    # timeUTC = datetime.datetime(y, m, d, h, mi, 0, 0, pytz.UTC)
    # print(timeUTC)

    # timeLocal = timeUTC.astimezone(timezone)
    # print(timeLocal)
