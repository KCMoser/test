import time

interval=5                              #Set time interval @ 5 seconds

while interval >0:                      #Start countdown
    mins, secs = divmod(interval, 60)   #Setting time formatting
    timeformat = '{:02d}:{:02d}'.format(mins, secs) #Setting time formatting
    print(timeformat, end='\r')         #Output current status, " end='\r' " puts output on same line
    time.sleep(1)                       #Pause for 1 second
    interval -=1                        #Decrement the countdown by 1
print('Done !')
