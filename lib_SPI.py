import spidev, time

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 0b00

def bat_route():
    res = spi.xfer([0x01])
    time.sleep(0.2)
    res = spi.xfer([0x01])
    while res[0] == 1:
        time.sleep(0.2)
        res = spi.xfer([0x01])
    print("bat_route = " + str(int(res[0])*4*0.0146))
    return(int(res[0])*4*0.0146)

def bat_aux():
    res = spi.xfer([0x02])
    time.sleep(0.2)
    res = spi.xfer([0x02])
    while res[0] == 2:
        time.sleep(0.2)
        res = spi.xfer([0x02])
    print("bat_aux = " + str(int(res[0])*4*0.0146))
    return(int(res[0])*4*0.0146)

def hum_int():
    res = spi.xfer([0x03])
    time.sleep(0.2)
    res = spi.xfer([0x03])
    while res[0] == 3:
        time.sleep(0.2)
        res = spi.xfer([0x03])
    print("hum_int = " + str(res))
    return(res[0])

def hum_ext():
    res = spi.xfer([0x04])
    time.sleep(0.2)
    res = spi.xfer([0x04])
    while res[0] == 4 :
        time.sleep(0.2)
        res = spi.xfer([0x04])
    print("hum_ext = " + str(res))
    return(res[0])


def temp_int():
    res = spi.xfer([0x05])
    time.sleep(0.2)
    res = spi.xfer([0x05])
    while res[0] == 5:
        time.sleep(0.2)
        res = spi.xfer([0x05])

    #spi.writebytes([0x07])
    #time.sleep(0.2)
    #res = spi.readbytes(2)
    #print("first : "+str(res))

    #time.sleep(2)
    #res = spi.xfer([0x05])
    #res = spi.xfer([0x05])
    print("temp_int = " + str(res))
    return(res[0])

def temp_ext():
    res = spi.xfer([0x06])
    time.sleep(0.2)
    res = spi.xfer([0x06])
    while res[0] == 6:
        time.sleep(0.2)
        res = spi.xfer([0x06])
    print("temp_ext = " + str(res))
    return(res[0])

def temp_frigo():
    res = spi.xfer([0x07])
    time.sleep(0.2)
    res = spi.xfer([0x07])
    while res[0] == 7:
        time.sleep(0.2)
        res = spi.xfer([0x07])
    print("temp_frigo = " + str(res))
    return(res[0])

def temp():

    temp_int()
    temp_ext()
    temp_frigo()
    return(1)

if __name__ == '__main__':
    temp()
    #hum_ext()
    # hum_int()
    #temp_int()
    bat_route()
    # bat_aux()
