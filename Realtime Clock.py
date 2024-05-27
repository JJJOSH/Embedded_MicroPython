import pyb
import machine
from pyb import RTC



track  = 0

def pc13_callback(pin):
    global track
    track = 1
    
def main():
    
    global track
    
    rtc =  RTC()
    #(year,month,day,weekday,hour,minute,seconds,subseconds)
    #Set date and time to 20 Feb 2024, 15:25: 10: 000
    rtc.datetime((2024,2,20,6,15,35,10,0))
    
    pyb.ExtInt('PC13',mode =pyb.ExtInt.IRQ_RISING, pull =pyb.Pin.PULL_NONE, callback = pc13_callback)
    
    
    while True:
        #Test2
        #print(rtc.datetime())
        
        if track ==  1:
            print(rtc.datetime()) #Get date and time
            track = 0


main()
    
    
    
