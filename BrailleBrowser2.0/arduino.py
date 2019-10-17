import serial
import time

i =0
ser = serial.Serial('COM4', 9600)
#ser.flush()


while (True):  
    # Serial write section
    setTempCar1 = 1
    setTempCar2 = 37
    setTemp1 = str(setTempCar1)
    setTemp2 = str(setTempCar2)
    print ("Python value sent: ")
    print (str.encode(setTemp1))
    temp = b'11111111'
    ser.write(chr(5).encode())
    time.sleep(2) # with the port open, the response will be buffered 
                  # so wait a bit longer for response here
    ser.write(chr(1).encode())
    # Serial read section
    msg = ser.read(ser.inWaiting()) # read everything in the input buffer
    print ("Message from arduino: ")
    print (msg)
    