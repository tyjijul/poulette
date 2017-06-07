import time


def bat_route():
    res = [200]
    
    return(int(res[0])*4*0.0146)

def bat_aux():
    res = [200]
    return(int(res[0])*4*0.0146)

def hum_int():
    res = [20]
    return(res[0])

def hum_ext():
    res = [20]
    return(res[0])


def temp_int():
    res = [20]
    return(res[0])

def temp_ext():
    res = [20]
    return(res[0])

def temp_frigo():
    res = [20]
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
