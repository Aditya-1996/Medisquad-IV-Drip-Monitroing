import serial
import requests
import json
ser = serial.Serial('/dev/ttyUSB0',9600)
limit = 970
val1=0
val2=0
while 1:
	x=ser.readline()
	if x[0] == 'a':
		val1=int(x[1:])
		#print(val1)
	else:
		val2=int(x[1:])
		#print(val2)
	
	if val1 and val2:
		if val1 >= limit and val2 >= limit:               #If drip level is high (pings both as > limit)
      			print("HIGH")
		elif val2 >= limit and val1 < limit:       
      			print("MEDIUM")
  		else:
     			print("LOW")