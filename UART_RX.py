import pyb

def main():
    green_led =  pyb.Pin('PA5', mode =pyb.Pin.OUT_PP)
    uart2 =  pyb.UART(2)
    uart2.init(115200,timeout = 100)
    
    while True:

        rx_data =  uart2.readchar()
        
        if rx_data == 0x67: #g
            
            green_led.value(not green_led.value())
        


main()
        