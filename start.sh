#!/bin/sh
cd /home/pi/433/PILocalTemp
python ./publishTemp.py <YOUR BROKER URL> "8883" &
