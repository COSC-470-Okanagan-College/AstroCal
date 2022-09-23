#Astro Calender Console Menu

#Imports
from datetime import datetime

#sun options
def sun():
    print('Sun Events')
    print('1. View Today')
    print('2. View Full Month')
    print('3. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        getCurrentdate()
        print('Sun will Rise: ' ) #call function name for moon rise
        print('Sun will Set : ') #call function name for moon set
    elif option == 2:
        print() #call month function
    elif option == 3:
        createMenu()
    else:
        print('error not an option')
        sun()
        

#moon options
def moon():
    print('Moon Events')
    print('1. View Today')
    print('2. View Full Month')
    print('3. Back \n')
    option = int(input('Enter selection: '))
    if option == 1:
        getCurrentdate()
        print('Moon will Rise: ' ) #call function name for moon rise
        print('Moon will Set : ') #call function name for moon set
    elif option == 2:
        moon() 
        #call month function
    elif option == 3:
        createMenu()
    else:
        print('error not an option')
        sun()

#get current date
def getCurrentdate():
    currentdate = datetime.now()
    today = currentdate.strftime("%B-%d-%Y  %H:%M \n")
    print(today)


#create menu
def createMenu():
    print('✧ ･ﾟ * ✧  ASTRO CALANDER  ✧ ･ﾟ * ✧ ･ﾟ \n')
    getCurrentdate()
    print('1. Sun Events')
    print('2. Moon Events')
    print('3. exit \n')
    option = int(input('Enter selection: '))
    if option == 1:
        sun()
    elif option == 2:
        moon()
    elif option == 3:
        print('Bye')
    else:
        print('error not an option')
        createMenu()

createMenu()