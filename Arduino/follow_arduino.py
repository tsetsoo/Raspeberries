import serial
import FacilRecognitionTrigger

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
while True:
    read_serial=ser.readline()
    s[0] = str(int (ser.readline(),16))
    print 's0 e: ' + s[0]
    if s[0] == '1':
        if FacilRecognitionTrigger.trigger() == 'simo':
            print "da stana"
            ser.write('Welcome Simo')
        else:
            print 'ne e simo'
            ser.write('chezni bunak')

    print read_serial
