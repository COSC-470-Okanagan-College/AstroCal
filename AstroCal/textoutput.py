from datetime import datetime

def run():
    getCurrentMonth()
    
def getCurrentMonth():  
    #Get Current Month & Year
    currentdate = datetime.now()
    month_str = currentdate.strftime("%B")
    month = currentdate.month 
    year = currentdate.year   

    #Get number of days in the month       
    if month > 11: #If month is December
        daysinmonth = (datetime(year+1, 1, 1) - datetime(year, month, 1)).days
    else:
        daysinmonth = (datetime(year, month + 1, 1) - datetime(year, month, 1)).days
    
    #Store calculations here || Move into for loop when calculations are put in
    sunrise_start = currentdate.strftime("%I:%M %p")
    sunrise_end = currentdate.strftime("%I:%M %p")
    sunset_start = currentdate.strftime("%I:%M %p")
    sunset_end = currentdate.strftime("%I:%M %p")
    moonrise_start = currentdate.strftime("%I:%M %p")
    moonrise_end = currentdate.strftime("%I:%M %p")
    moonset_start = currentdate.strftime("%I:%M %p")
    moonset_end = currentdate.strftime("%I:%M %p")
    
    #Print out info for each day in the month
    for day in range(daysinmonth):
        print("".ljust(45, '='))
        print("{} {}, {}".format(month_str, day+1, year))  
        print("".ljust(45, '='))
        print("{:<12} | {:<12} | {:<12}".format("Event", "Start Time", "End Time"))
        print("".ljust(45, '-'))
        print("{:<12} | {:<12} | {:<12}".format("Sunrise", sunrise_start, sunrise_end))
        print("{:<12} | {:<12} | {:<12}".format("Sunset", sunset_start, sunset_end))
        print("{:<12} | {:<12} | {:<12}".format("Moonrise", moonrise_start, moonrise_end))
        print("{:<12} | {:<12} | {:<12}".format("Moonset", moonset_start, moonset_end))
        print()

run()