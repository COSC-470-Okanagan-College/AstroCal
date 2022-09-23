# import the library
def run():
    import swisseph as swe
    # set the directory path of the ephemeris files
    swe.set_ephe_path("./swissEphem")
    # find time of next lunar eclipse
    jd = swe.julday(2027, 9, 9) # julian day
    res = swe.lun_eclipse_when(jd)
    ecltime = swe.revjul(res[1][0])
    print(ecltime)