'''Librairie de lecture capteur'''
import random

ALERT_PROPRE = 20
ALERT_GRISE = 60
ALERT_BATTERY = 12

def get_temperature():
    '''read temp'''
    value1 = round(random.uniform(-20, 40), 2)
    value2 = round(random.uniform(-20, 40), 2)
    value3 = round(random.uniform(-20, 40), 2)
    # value1 = 10
    # value2 = 20
    # value3 = 30
    return value1, value2, value3

def get_humidity():
    '''read humidity'''
    value1 = random.randint(0, 100)
    value2 = random.randint(0, 100)
    # value1 = 40
    # value2 = 50
    return value1, value2

def get_water():
    '''read water'''
    value1 = random.randint(0, 100)
    value2 = random.randint(0, 100)
    # value1 = 60
    # value2 = 70
    return value1, value2

def get_battery():
    '''read battery'''
    value = round(random.uniform(9, 15), 2)
    # value = 15
    return value

def get_all():
    '''read all value'''
    temperature = get_temperature()
    humidity = get_humidity()
    water = get_water()
    battery = get_battery()
    return temperature, humidity, water, battery

def get_alert():
    '''return alert on water and battery '''
    water = get_water()
    battery = get_battery()
    res = []
    if water[0] <= ALERT_PROPRE:
        res.append("<h4>Alerte niveau eau propre</h4>")
    if water[1] >= ALERT_GRISE:
        res.append("<h4>Alerte niveau eau grise</h4>")
    if battery <= ALERT_BATTERY:
        res.append("<h4>Alerte niveau batterie</h4>")
    if res == []:
        res.append("<h4>Aucune alerte</h4>")
    return res

if __name__ == '__main__':
    # value = get_all()
    # print(value[0][0])
    # print(value[1])
    # print(value[2])
    # print(value[3])
    print(get_alert())
