import pyb

MULTI_BYTE_EN   = 0x40  # 0b 0100 0000
READ_OPERATION  = 0x80  # 0b 1000 0000

DEVICE_ID_ADDR = 0x00

#Create chip select pin at PA9
cs_pin = pyb.Pin('PA9',mode=pyb.Pin.OUT_PP)
spi_master =  pyb.SPI(1)
spi_master.init(pyb.SPI.MASTER,baudrate = 2000000,polarity=1,phase =1)



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
    

addr_buff =  bytearray(1)
addr_buff[0] = DEVICE_ID_ADDR

print(adxl345_read(addr_buff))

