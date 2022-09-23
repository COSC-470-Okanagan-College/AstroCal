import swisseph as swe
import sys
import datetime
import pytz


def run():
    moonrise()
    moonset()

def moonrise():
    tjd = swe.julday(2022, 9, 11, 0, swe.GREG_CAL)  # julian day

    res, tret = swe.rise_trans(tjd, swe.MOON, swe.CALC_RISE,
                               (-119.4960, 49.8880, 342.0), 0, 0, swe.FLG_SWIEPH)

    if (res != 0):
        print('moonrise not found')
        sys.exit(1)

    tset = tret[0]

    y, m, d, h, mi, s = swe.jdut1_to_utc(tset, swe.GREG_CAL)

    print('moonrise: %d/%02d/%02d %d:%d UTC' %
          (y, m, d, h, mi))

    timezone = pytz.timezone('PST8PDT')
    timeUTC = datetime.datetime(y, m, d, h, mi, 0, 0, pytz.UTC)
    print(timeUTC)

    timeLocal = timeUTC.astimezone(timezone)
    print(timeLocal)

def moonset():
    tjd = swe.julday(2022, 9, 11, 0, swe.GREG_CAL)  # julian day

    res, tret = swe.rise_trans(tjd, swe.MOON, swe.CALC_SET,
                               (-119.4960, 49.8880, 342.0), 0, 0, swe.FLG_SWIEPH)
    if (res != 0):
        print('moonset not found')
        sys.exit(1)

    tset = tret[0]

    y, m, d, h, mi, s = swe.jdut1_to_utc(tset, swe.GREG_CAL)

    print('moonset: %d/%02d/%02d %d:%d UTC' %
          (y, m, d, h, mi))

    timezone = pytz.timezone('PST8PDT')
    timeUTC = datetime.datetime(y, m, d, h, mi, 0, 0, pytz.UTC)
    print(timeUTC)

    timeLocal = timeUTC.astimezone(timezone)
    print(timeLocal)