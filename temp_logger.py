#!/usr/bin/python
# -*- coding: utf-8 -*-

# Die Sensoren m�ssen mit "modprobe w1-gpio" und "modprobe w1-therm" aktiviert werden!


# Import der Module
import sys
import os
import urllib
from time import *

# Zeitvariable definieren
lt = localtime()

# Apikey und URL für emoncms angeben
s_apikey="acba7aa62bda32bb15261998c1a6fa13"
s_emonurl="http://emon.sklammer.at/input/post.json?node=1&json={"
s_apikey="your_api_key"
s_emonurl="http://youremonurl.com/input/post.json?node=1&json={"

# 1-Wire Slave-Liste oeffnen
file = open('/sys/devices/w1_bus_master1/w1_master_slaves') #Verzeichniss evtl. anpassen

# 1-Wire Slaves auslesen
w1_slaves = file.readlines()

# 1-Wire Slave-Liste schliessen
file.close()

temperature = []
senorids = []

# Header fuer Bildschirmausgabe
#print('Sensor ID       | Temperatur')
#print('----------------------------')
# Fuer jeden 1-Wire Slave eine Ausgabe
while(1):
 for line in w1_slaves:

  # 1-wire Slave extrahieren
  w1_slave = line.split("\n")[0]

  # 1-wire Slave Datei oeffnen
  file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')

  # Inhalt des 1-wire Slave File auslesen
  filecontent = file.read()

  # 1-wire Slave File schliessen
  file.close()

  # Temperatur Daten auslesen
  stringvalue = filecontent.split("\n")[1].split(" ")[9]

  # Temperatur konvertieren
  #temperature = float(stringvalue[2:]) / 1000

  # Temperatur in array legen
  senorids.append(w1_slave)
  temperature.append(stringvalue[2:])

  # Temperatur ausgeben
  #print(str(w1_slave) + ' | %5.3f �C' % temperature)

  # Werte in Datei schreiben
  # Zeit und Datum erfassen
  #Datum = strftime("%d.%m.%Y")
  #Uhrzeit = strftime("%H:%M:%S")

  # Textdatei oeffnen
  #fobj_out = open("temp-daten.txt","a")
  # Daten in Textdatei schreiben
  #fobj_out.write(Datum + ", " + Uhrzeit +", " + '%5.3f �C' % temperature + "\n")
  # Textdatei schliessen
  #fobj_out.close()


 # Python script beenden und GNUPLOT Grafik erstellen
 for i in range(0, 7):
  #print("Senornr: " + str(i) +"ID" + senorids[i] +", Temp: " + str(temperature[i]) + "\n")
  url_d=s_emonurl
  url_d+=senorids[i]+ ":" + str(temperature[i]) +";}&apikey="
  url_d+=s_apikey
  f=urllib.urlopen(url_d)
  #print(f.read())
 print("Loop OK")
 sleep(60)

sys.exit(0)
