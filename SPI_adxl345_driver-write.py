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
    addr_buff[0] = DATA_FORMAT_R
    adxl_write(addr_buff,FOUR_G)
    
    #Reset all power control bits
    addr_buff[0] = POWER_CTL_R
    adxl_write(addr_buff,RESET)
    
    #Set power control measure bit
    addr_buff[0] = POWER_CTL_R
    adxl_write(addr_buff,SET_MEASURE_B)    


