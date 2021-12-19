#!/bin/bash

sudo apt update
sudo apt full-upgrade -y
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install vim -y

# adc
pip install adafruit-circuitpython-ads1x15
cd ~/Desktop
git clone https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15.git
cp Adafruit_CircuitPython_ADS1x15/examples/ads1x15_simpletest.py ~/Desktop/EMGRec/adc.py

# matplotlib
sudo apt-get install libatlas-base-dev -y
pip install matplotlib
pip install -U numpy

# setting aliases
echo -e "alias lab='cd ~/Desktop/EMGRec'\n" >> ~/.bash_aliases
source ~/.bashrc
