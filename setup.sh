sudo apt-get update && sudo apt-get upgrade
sudo apt-get install vim
# setting aliases
echo -e "alias lab='cd ~/Desktop/EMGRec'\n" >> ~/.bash_aliases
source ~/.bashrc

# adc
pip install adafruit-circuitpython-ads1x15
cd ~/Desktop
git clone https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15.git
cp Adafruit_CircuitPython_ADS1x15/examples/ads1x15_simpletest.py ~/Desktop/gestureRec/adc.py

# matplotlib
apt-get install libatlas-base-dev
pip install matplotlib
