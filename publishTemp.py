import os
import glob
import time
import paho.mqtt.client as paho
import math
import ssl
import sys
from time import strftime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

mqttClient = paho.Client();
mqttClient.will_set("/event/dropped", "Connection died")
mqttClient.tls_set("./certs/ca.cert", "./certs/client.cert", "./certs/client.key", ssl.CERT_REQUIRED, ssl.PROTOCOL_TLSv1, None)
mqttClient.tls_insecure_set(True);
mqttClient.connect(sys.argv[1], sys.argv[2], 60, "")

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        # return temp_c, temp_f
        return temp_c

while True:
        temp = read_temp()
        mqttClient.publish("house/temp2", str(math.trunc(time.time())) + ", temp:" + str(temp))
        mqttClient.publish("house/time", str(math.trunc(time.time())) + ", time:" + str(strftime('%H %M %S')))
        time.sleep(10)


