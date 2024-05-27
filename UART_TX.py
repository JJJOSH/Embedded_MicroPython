import pyb

tx_data = "Hello World\n\r"
def main():
    green_led =  pyb.Pin('PA5', mode =pyb.Pin.OUT_PP)
    uart2 =  pyb.UART(2)
    uart2.init(115200,timeout = 100)
    
    while True:
        uart2.write(tx_data)
        green_led.value(not green_led.value())
        pyb.delay(1000)
        


main()
        