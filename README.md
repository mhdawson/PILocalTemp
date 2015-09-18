# PI Local temperature

This project reads the temperature from a local sensor and publishes
to an mqtt broker 

## Circuit

TODO (standard DS18B20 connection to 1 wire)


## To install/run:
+ git clone https://github.com/mhdawson/PILocalTemp.git

+ cd PILocalTemp

+ update start.sh to reflect your path and config

+ add certs directory or comment out line in publishTemp.py that sets the certs

+ download get-pip.py from https://bootstrap.pypa.io/get-pip.py

+ python get-pip.py

+ pip install paho-mqtt

+ add:

    dtoverlay=w1-gpio
    
+ to the end of

   /boot/config.txt
   
+ reboot

+ start by running start.sh

Temperature will be published to house/temp2

Time will be published to house/time


## TODOs
- more info  

