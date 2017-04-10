#!/usr/bin/python
# -*- coding: utf-8 -*-

# Das Modul ADE7758 muss mit sudo modprobe ade7758 geladen werden

# Import der Module
import sys
import os
import urllib
from time import *

# Zeitvariable definieren
lt = localtime()

# Apikey und URL für emoncms angeben
s_apikey="your_api_key"
s_emonurl="http://youremonurl.com/input/post.json?node=1&json={"

# Argumente auswerten
if(len(sys.argv)>1):
 action=sys.argv[1]
 if(len(sys.argv)>2):
  delay=int(sys.argv[2])
else:
 action="meas"
 delay=5

if(action=="meas"):
 i=0
 while(i<60):
  print("Measure" +str(i) +"sec")
   # URL Anfang erstellen
   url_d=s_emonurl
  # ADE7758 Datei oeffnen & Spannungen lesen
  # Spannung L1
  file = open('/sys/bus/iio/devices/iio:device0/avrms')
  filecontent = file.read()
  file.close()
  url_d+="{SpannungL1:" + str(filecontent) +"},"
  # Spannung L2
  file = open('/sys/bus/iio/devices/iio:device0/bvrms')
  filecontent = file.read()
  file.close()
  url_d+="{SpannungL2:" + str(filecontent) +"},"
  # Spannung L3
  file = open('/sys/bus/iio/devices/iio:device0/cvrms')
  filecontent = file.read()
  file.close()
  url_d+="{SpannungL3:" + str(filecontent) +"},"

  # Strom L1
  file = open('/sys/bus/iio/devices/iio:device0/airms')
  filecontent = file.read()
  file.close()
  url_d+="{Strom1:" + str(filecontent) +"},"
  # Strom L2
  file = open('/sys/bus/iio/devices/iio:device0/birms')
  filecontent = file.read()
  file.close()
  url_d+="{StromL2:" + str(filecontent) +"},"
  # Strom L3
  file = open('/sys/bus/iio/devices/iio:device0/cirms')
  filecontent = file.read()
  file.close()
  url_d+="{Strom3:" + str(filecontent) +"},"

  # Scheinleistung L1
  file = open('/sys/bus/iio/devices/iio:device0/a')
  filecontent = file.read()
  file.close()
  url_d+="{VA_L1:" + str(filecontent) +"},"
  # Scheinleistung L2
  file = open('/sys/bus/iio/devices/iio:device0/b')
  filecontent = file.read()
  file.close()
  url_d+="{VA_L2:" + str(filecontent) +"},"
  # Scheinleistung L3
  file = open('/sys/bus/iio/devices/iio:device0/c')
  filecontent = file.read()
  file.close()
  url_d+="{VA_L3:" + str(filecontent) +"},"

  # Blindleistung L1
  file = open('/sys/bus/iio/devices/iio:device0/a')
  filecontent = file.read()
  file.close()
  url_d+="{VAr_L1:" + str(filecontent) +"},"
  # Blindleistung L2
  file = open('/sys/bus/iio/devices/iio:device0/b')
  filecontent = file.read()
  file.close()
  url_d+="{VAr_L2:" + str(filecontent) +"},"
  # Blindleistung L3
  file = open('/sys/bus/iio/devices/iio:device0/c')
  filecontent = file.read()
  file.close()
  url_d+="{VAr_L3:" + str(filecontent) +"},"

  # URL abschliessen und aufrufen
  url_d+="}&apikey="
  url_d+=s_apikey
  f=urllib.urlopen(url_d)
  i=i+delay
  if(i==60):
   break
  sleep(delay)

elif(action=="cal"):
 print("Calibrate ADE7758")
 print("Read Calibration Data")
 file = open('/sys/bus/iio/devices/iio:device0/avrmsos')
 filecontent = int(file.read())
 print(filecontent)
 file.close()
 if(filecontent!=0):
  print("ADE7758 has set Calibration Data")
  print("Do you want to recalibrate? (Y/N/C)")
  calibrate=raw_input()
 else:
  calibrate="Y"

 if(calibrate=="Y"):
  print("ADE7758 not yet calibrated")
  print("Start calibration")
  print("Shorten the Voltage Inputs, Press Enter when finished")
  raw_input()
  file = open('/sys/bus/iio/devices/iio:device0/avrms')
  filecontent = int(file.read())
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/avrmsos','rw')
  file.write(str(-filecontent/64))
  filecontent = int(file.read())
  file.close()
  print("Channel A Voltage Offset set to: " + str(filecontent))
  file = open('/sys/bus/iio/devices/iio:device0/bvrms')
  filecontent = int(file.read())
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/bvrmsos','rw')
  file.write(str(-filecontent/64))
  filecontent = int(file.read())
  file.close()
  print("Channel B Voltage Offset set to: " + str(filecontent))
  file = open('/sys/bus/iio/devices/iio:device0/cvrms')
  filecontent = int(file.read())
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/cvrmsos','rw')
  file.write(str(-filecontent/64))
  filecontent = int(file.read())
  file.close()
  print("Channel C Voltage Offset set to: " + str(filecontent))

  print("Close the Current Clips with no wire, Press Enter when finished")
  raw_input()
  file = open('/sys/bus/iio/devices/iio:device0/airms')
  filecontent = int(file.read())
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/airmsos','rw')
  file.write(str(-filecontent/64))
  filecontent = int(file.read())
  file.close()
  print("Channel A Current Offset set to: " + str(filecontent))
  file = open('/sys/bus/iio/devices/iio:device0/birms')
  filecontent = int(file.read())
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/birmsos','rw')
  file.write(str(-filecontent/64))
  filecontent = int(file.read())
  file.close()
  print("Channel B Current Offset set to: " + str(filecontent))
  file = open('/sys/bus/iio/devices/iio:device0/cirms')
  filecontent = int(file.read())
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/cirmsos','rw')
  file.write(str(-filecontent/64))
  filecontent = int(file.read())
  file.close()
  print("Channel C Offset set to: " + str(filecontent))

 elif(calibrate=="C"):
  file = open('/sys/bus/iio/devices/iio:device0/avrmsos','w')
  file.write("0")
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/bvrmsos','w')
  file.write("0")
  file.close()
  file = open('/sys/bus/iio/devices/iio:device0/cvrmsos','w')
  file.write("0")
  file.close()
  print("All Calibration Data cleared")
 else:
  print("Leave calibration as is")

sys.exit(0)

print("Alles OK")
