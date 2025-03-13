import requests

url = 'http://<STRAPILocalIP>:<PORT>/api/aqua-sreading-tests'

myobj = {"data":{
  "Temperature": 25.5,
  "device_id": 1512313531,
  "timestamp": "2025-02-26T12:34:56.789Z"
}
}

x = requests.post(url,headers={"Content-Type": "application/json"},json=myobj)
print(x.content)



"""
# Code on the raspberry pi to read the arduino
# combine eventually
import serial
import datetime
import pytz

def nowtime():
    dtime = datetime.datetime.now()
    timezone = pytz.timezone("America/New_York")
    dtzone = timezone.localize(dtime)
    tstamp = dtzone.timestamp()
    epoch_time_secs = int(round(tstamp))
    return epoch_time_secs

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) #ttyACM0 is the lsusb for arduino connected
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            tstamp = nowtime()
            line += ";"+str(tstamp)
            print(line)

"""