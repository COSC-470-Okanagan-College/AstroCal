import swisseph as swe

def test_swe():
	jd = swe.julday(2007, 3, 3)
	res = swe.lun_eclipse_when(jd)
	ecltime = swe.revjul(res[1][0])
	print(ecltime)