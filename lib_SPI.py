import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 0b00

def bat_route():
    res = spi.xfer([0x04, 0x00])
    print("bat_route = " + str(res[0]))
    return(res[0])

def bat_aux():
    res = spi.xfer([0x04, 0x00])
    print("bat_aux = " + str(res[0]))
    return(res[0])

def hum_int():
    res = spi.xfer([0x05, 0x00])
    print("hum_int = " + str(res[0]))
    return(res[0])

def hum_ext():
    res = spi.xfer([0x06, 0x00])
    print("hum_ext = " + str(res[0]))
    return(res[0])

def temp_int():
    res = spi.xfer([0x07, 0x00, 0x00, 0x00, 0x00])
    print("temp_int = " + str(res[0]))
    return(res[0])

def temp_ext():
    res = spi.xfer([0x08, 0x00])
    print("temp_ext = " + str(res[0]))
    return(res[0])

def temp_frigo():
    res = spi.xfer([0x09, 0x00])
    print("temp_ext = " + str(res[0]))
    return(res[0])
