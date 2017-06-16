import gpxpy, time
import gpxpy.gpx


def is_holyday(VACANCE_BOOL):
    """ Write in holiday.txt 1 if holiday mode activate """
    file = open("holiday.txt", "w")
    if VACANCE_BOOL == 1:
        dateDebut = time.strftime("%Y-%m-%d_%H-%M-%S")
        file.write("1;"+dateDebut)
        print("C'est les vacances !!!!!")
    elif VACANCE_BOOL == 0:
        file.write("0")
        print("Au boulot !")
    file.close()


def txt_to_gpx():
    """ Convert txt gps-holiday.txt in GPX trace TO DO ADD NAME AND DESCRIPTION"""
    gpx = gpxpy.gpx.GPX()

    # Create first track in our GPX:
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    # Create first segment in our GPX track:
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    with open("gps-holiday.txt", "r") as holiday:
        lines = holiday.readlines()
        print(lines)
        for line in lines:
            if line != "\n":
                parsePath = line.split(",")
                date = parsePath[0]
                hour = parsePath[1]
                longitude = parsePath[2]
                latitude = parsePath[3]
                # Create points:
                gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(float(longitude), float(latitude), elevation=0))
    print('Created GPX:', gpx.to_xml())
    file = open("testfile.gpx", "w")
    file.write(gpx.to_xml())

def gps_base():
    holiday = open("holiday.txt", "r")
    H = holiday.read()
    holiday.close()
    if H == "1":
        with open("gps-holiday.txt", "w") as holiday:
            holiday.write("gpsData['fix_date']" + "," + "gpsData['fix_time']" + "," + "str(gpsData['decimal_latitude'])" + "," + "str(gpsData['decimal_longitude'])"+",endLine")



is_holyday(1)
#txt_to_gpx()









