from lockinternet import *
from lockscreen import *
import time
from datetime import datetime

while True:
    datetf=open('data2','r')
    datet=datetf.read()
    datetf.close()
    if datetime.today().strftime('%Y-%m-%d') != datet:
        datetf=open('data2','w')
        datetf.write(datetime.today().strftime('%Y-%m-%d'))
        datetf.close()
        screentimef=open('data','w')
        screentimef.write('0')
        screentimef.close()
        root.destroy()
        turn_on_wifi()
    screentimef=open('data','r')
    screentime=float(screentimef.read())
    screentimef.close()
    time.sleep(.1)
    screentime+=.1
    screentimef=open('data','w')
    screentimef.write(str(screentime))
    screentimef.close()
    if screentime>=7200:
        turn_off_wifi()
        root.mainloop()
