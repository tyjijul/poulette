'''Librairie de lecture capteur'''
import random

def get_temperature():
    '''read temp'''
    value1 = round(random.uniform(-20, 40), 2)
    value2 = round(random.uniform(-20, 40), 2)
    value3 = round(random.uniform(-20, 40), 2)
    return value1, value2, value3

def get_humidity():
    '''read humidity'''
    value1 = random.randint(0, 100)
    value2 = random.randint(0, 100)
    return value1, value2

def get_water():
    '''read water'''
    value1 = random.randint(0, 100)
    value2 = random.randint(0, 100)
    return value1, value2

def get_battery():
    '''read battery'''
    value = round(random.uniform(9, 15), 2)
    return value

if __name__ == '__main__':
    print(get_temperature())
