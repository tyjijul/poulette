import gpxpy
import gpxpy.gpx


def is_holyday(n):
    file = open("holiday.txt","w")
    if n == 1:
        file.write("1")
    elif n == 0:
        file.write("0")
    file.close()


def txt_to_gpx():
    # Creating a new file:
    # --------------------

    gpx = gpxpy.gpx.GPX()

    # Create first track in our GPX:
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    # Create first segment in our GPX track:
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # Create points:
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234, 5.1234, elevation=1234))
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235, 5.1235, elevation=1235))
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236, 5.1236, elevation=1236))

    # You can add routes and waypoints, too...

    print('Created GPX:', gpx.to_xml())

    file = open("testfile.gpx","w")
    # for lines in gpx.to_xml():
    #     #print(lines)
    #     file.write(lines)

    file.write(gpx.to_xml())

def gps_base():
    holiday = open("holiday.txt", "r")
    H = holiday.read()
    holiday.close()
    if H == "1":
        with open("gps-holiday.txt", "w") as holiday:
            holiday.write("gpsData['fix_date']" + "," + "gpsData['fix_time']" + "," + "str(gpsData['decimal_latitude'])" + "," + "str(gpsData['decimal_longitude'])"+",endLine")



is_holyday(1)

gps_base()








