import pyb

green_led =  pyb.Pin('PA5',mode = pyb.Pin.OUT_PP)


def btn_callback(id):
    
    if id == 13:
        green_led.value(not green_led.value())
        print("Line 13 triggered")
    if id == 0:
        print("Line 0 triggered")

def main():
    pc13_btn =  pyb.ExtInt('PC13',pyb.ExtInt.IRQ_RISING,pyb.Pin.PULL_DOWN,btn_callback)
    pa0_btn =  pyb.ExtInt('PA0',pyb.ExtInt.IRQ_RISING,pyb.Pin.PULL_DOWN,btn_callback)
    

main()



