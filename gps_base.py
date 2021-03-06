""" Librairie de lecture de la balise GPS puis d'ecriture en fichier texte """

import serial
import os, time



firstFixFlag = False # this will go true after the first GPS fix.
firstFixDate = ""

# Set up serial:
ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=4800,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)

# Helper function to take HHMM.SS, Hemisphere and make it decimal:
def degrees_to_decimal(data, hemisphere):
    try:
        decimalPointPosition = data.index('.')
        degrees = float(data[:decimalPointPosition-2])
        minutes = float(data[decimalPointPosition-2:])/60
        output = degrees + minutes
        if hemisphere is 'N' or hemisphere is 'E':
            return output
        if hemisphere is 'S' or hemisphere is 'W':
            return -output
    except:
        return ""

# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
# This also calls degrees_to_decimal and stores the decimal values as well.
def parse_GPRMC(data):
    data = data.split(',')
    dict = {
            'fix_time': data[1],
            'validity': data[2],
            'latitude': data[3],
            'latitude_hemisphere' : data[4],
            'longitude' : data[5],
            'longitude_hemisphere' : data[6],
            'speed': data[7],
            'true_course': data[8],
            'fix_date': data[9],
            'variation': data[10],
            'variation_e_w' : data[11],
            'checksum' : data[12]
    }
    dict['decimal_latitude'] = degrees_to_decimal(dict['latitude'], dict['latitude_hemisphere'])
    dict['decimal_longitude'] = degrees_to_decimal(dict['longitude'], dict['longitude_hemisphere'])
    return dict

# Main program loop:
while True:
    line = ser.readline()
    print(line)
    if "$GPRMC" in line: # This will exclude other NMEA sentences the GPS unit provides.
        gpsData = parse_GPRMC(line) # Turn a GPRMC sentence into a Python dictionary called gpsData
        print(gpsData)
        #if gpsData['validity'] == "A": # If the sentence shows that there's a fix, then we can log the line
        if gpsData['decimal_latitude'] == '' :
                print("NO SIGNAL")
        else :
                with open("/home/pi/poulette/GPS-log.txt", "w") as myfile:
                    myfile.write(gpsData['fix_date'] + "," + gpsData['fix_time'] + "," + str(gpsData['decimal_latitude']) + "," + str(gpsData['decimal_longitude'])+",endLine")
                with open("/home/pi/poulette/GPS-raw-log.txt", "w") as myfile:
                    myfile.write(line)
                myfile.close()
                holiday = open("holiday.txt", "r")
                H = holiday.read()
                holiday.close()
		print(H)
                if "1" in H:
		    print("detect holiday mode")
                    with open("/home/pi/poulette/gps-holiday.txt", "a") as holiday:
                        if gpsData['fix_date'] > "1":
				print("None mouvement detect - position don't save")
                        	holiday.write(gpsData['fix_date'] + "," + gpsData['fix_time'] + "," + str(gpsData['decimal_latitude']) + "," + str(gpsData['decimal_longitude'])+",endLine\n")
                    holiday.close()

        time.sleep(5)

