#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execut python script, then back to home

cd /
cd home/pi/emon_scripts
sudo python temp_logger.py
cd /
