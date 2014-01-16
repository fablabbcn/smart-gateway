Smart Citizen Gateway
=====================

**Smart Citizen Kit USB to Internet Gateway.**

#### Requirements

* *pySerial* module `pip install pyserial
` or `easy_install -U pyserial`

* *Requests* module `pip install requests` or `easy_install requests`

#### Setup

* Load using the Arduino IDE SmartCitizen firmware  0.8.5.1 with `#define USBLogEnabled   true` from /firmware. For **SCK version 1.1** select `Tools/Boards/Lylipad Arduino USB` on the Arduino IDE *(ATmega 23U4 at 8Mhz)*

* Edit `smart-gtw-service.sh` with the user and location want to run the service.

* Link the file as a system service `ln -s ./smart-gtw-service.sh /etc/init.d/smart-gtw`

* List all the USB Serial devices using `ls /dev | grep -e usb -e USB -e ACM` and get the SmartCitizen port.

* Edit the port path in the `config.ini` file.

* You can run a test by `python smart-gateway.py`.

* Start the service as `/etc/init.d/smart-gtw start`






