import pyb

MULTI_BYTE_EN   = 0x40  # 0b 0100 0000
READ_OPERATION  = 0x80  # 0b 1000 0000

DEVICE_ID_ADDR  = 0x00
POWER_CTL_R     = 0x2D
DATA_FORMAT_R   = 0x31
FOUR_G          = 0x01
DATA_START_ADDR = 0x32
RESET           = 0x00
SET_MEASURE_B   = 0x08

#Create chip select pin at PA9
cs_pin = pyb.Pin('PA9',mode=pyb.Pin.OUT_PP)
spi_master =  pyb.SPI(1)
spi_master.init(pyb.SPI.MASTER,baudrate = 2000000,polarity=1,phase =1)


def adxl345_write(address,value):
    
    #Create buff to hold addr and data
    data_buff = bytearray(2)
    
    #Enable multi-byte and place addr in buffer
    data_buff[0] = address | MULTI_BYTE_EN
    
    #Place data into buff
    data_buff[1] = value

    #Pull cs_line low enable the slave
    cs_pin(0)
    
    #Send data and addr
    spi_master.write(data_buff)
    
    #Pull cs_line high disable the slave
    cs_pin(1)


def adxl345_read(address):
    
    
    #Set read operation
    address[0] |= MULTI_BYTE_EN
    
    #Enable multibyte read
    address[0] |= READ_OPERATION
    
    #Pull cs_line low enable the slave
    cs_pin(0)
    
    #Send address
    spi_master.write(address)
    
    #read data
    rxdata = bytearray(6)
    
    #read 6 bytes
    spi_master.readinto(rxdata)
    
    #Pull cs_line high disable the slave
    cs_pin(1)
    
    #return read data
    return rxdata 
    


def adxl345_init():
    
    #Create addr buff
    addr_buff = bytearray(1)
    
    #Set data format to +-4g
    adxl345_write(DATA_FORMAT_R,FOUR_G)
    
    #Reset all power control bits
    adxl345_write(POWER_CTL_R,RESET)
    
    #Set power control measure bit
    adxl345_write(POWER_CTL_R,SET_MEASURE_B)    



def main1():
    
    addr_buff = bytearray(1)
    addr_buff[0] = DATA_START_ADDR
    
    data_rec =  bytearray(6)
    
    adxl345_init()
    
    while True:
        
        data_rec = adxl345_read(addr_buff)
        
        x = ((data_rec[1] <<8)|data_rec[0])
        y = ((data_rec[3] <<8)|data_rec[2])
        z = ((data_rec[5] <<8)|data_rec[4])
        
        xg = (x * 0.0078)
        yg = (y * 0.0078)
        zg = (z * 0.0078)
        
#         print("X :",str(x))
#         print("Y :",str(y))
#         print("Z :",str(z))

        print("XG :",str(xg))
        print("YG :",str(yg))
        print("ZG :",str(zg))
        


def main():
    i2c_master =  pyb.I2C(1)
    i2c_master.init(pyb.I2C.MASTER)
    print(i2c_master.scan())
    


main()
