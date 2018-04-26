# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:48:02 2018

@author: evin
"""

import re
import json

data = '{"tobiiEyeTracker":{"timeStamp":"25.09.2017 18:06:36.7452","leftPos":{"x":"-16,7315728269386","y":"3,89062108428363","z":"56,2198678361344"},"rightPos":{"x":"-10,0026425550767","y":"3,29426110476243","z":"56,0879127434864"},"leftGaze":{"x":"-3,49850843959982","y":"22,1567167927533","z":"6,37821179543316"},"rightGaze":{"x":"-7,89889571217705","y":"21,4349212191887","z":"6,11551553472114"},"leftPupilDiameter":"3,069977","rightPupilDiameter":"2,963455"}}'

omitBeginLen = len('{"tobiiEyeTracker":')

data = data[omitBeginLen:-1]

print data

print "##################################"

data = re.sub(r'\"(\-??\d+),(\d+)\"', r'\1.\2', data) # "-16,7315728269386" -> -16.7315728269386

print data
#print "##################################"
#
#jsonData = json.loads(data)
#print jsonData
#print "##################################"
#
#timeStampStr = jsonData["timeStamp"]
#
#jsonData["timeStamp"] = timeStampStr.strip('"')
#
#print jsonData

