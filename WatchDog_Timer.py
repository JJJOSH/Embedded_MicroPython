import pyb
import machine



green_led =  pyb.Pin('PA5', mode = pyb.Pin.OUT_PP)

#Enabl watchdog timer with a timeout of 5 seconds
wdt =  machine.WDT(timeout = 5000)

sema = 0

def timer_thread(timer):
    global sema
    
    if sema == 0:
        green_led.value(not green_led.value())
        
        print("System in normal operation...")
        
        #Feed the watchdog timer to prevent it from resetting the system
        wdt.feed()

def pc13_callback(pin):
    global sema
    sema = 1
    
def main():
    global sema
    
    pyb.ExtInt('PC13', mode = pyb.ExtInt.IRQ_RISING, pull = pyb.Pin.PULL_NONE, callback = pc13_callback)
    timer1 =  pyb.Timer(1, freq = 10, mode = pyb.Timer.UP)
    timer1.callback(timer_thread)



main()
    
    
    
