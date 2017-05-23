import time

temperatureLevels = []
counter = 0
while counter <= 12:
    print(counter)
    currentTemp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
    temperatureLevels.append(currentTemp)
    print 'Current temp: ' + str(currentTemp)
    time.sleep(5)
    counter += 1
    minuteMaximums = max(temperatureLevels)
    print "Maximum temperature was: ", minuteMaximums 
    print 'Weekly maximum radiation: ' + str(minuteMaximums)

#First comment line here
# Checking maximum value



# This line prints the value of weeklyMaximum.
# Since we combine a text string with a numerical value
# we use str() to convert the number to a string so print
# can display both together.

#print 'Weekly maximum radiation: ' + str(minuteMaximums)
