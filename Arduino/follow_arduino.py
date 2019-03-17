import serial
import FacilRecognitionTrigger

ser = serial.Serial('/dev/ttyUSB0',9600, timeout=None)
s = [0,1]
while True:
    if ser.read() == '1':
        if FacilRecognitionTrigger.trigger() == 'tsetso':
            print "da stana"
            ser.write('1')
        else:
            print 'ne e simo'
            ser.write('0')
