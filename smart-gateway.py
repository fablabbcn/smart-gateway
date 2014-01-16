#!/usr/bin/env python

import requests
import serial
import json
import ConfigParser
import logging

from time import sleep
from datetime import datetime

config = ConfigParser.ConfigParser()

config.read('config.ini')

sck = serial.Serial(config.get('SMARTCITIZEN-KIT','port'), config.getint('SMARTCITIZEN-KIT','speed'))

try:
	sck.flush()
	while 1:
	    if sck.inWaiting():
	        line = sck.readline().strip(' \t\n\r')
	        sck.flush()
	       	data = json.loads(line)

	    	sensors = data['sensors']

	    	for sensor in sensors:
	    		sensor['timestamp'] = datetime.utcnow().isoformat()

			payload = {}
			headers = {'X-SmartCitizenMacADDR': data['params']['mac-address'], 'X-SmartCitizenVersion': data['params']['kit-version'], 'User-Agent': 'SmartCitizen Gateway', 'X-SmartCitizenData': json.dumps(sensors)}


			r = requests.put(config.get('SMARTCITIZEN-SERVER','collectorURL'), data=json.dumps(payload), headers=headers)
	   	    
	    	print json.dumps(sensors)
	    	print r

except KeyboardInterrupt:
	print "\nQuit	"


