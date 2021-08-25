#this python program reads serial data form arduino and posts it to oracle event hub with a rest proxy
import serial
import requests
import json
#ser = serial.Serial('/dev/ttyUSB0',9600)
url = 'https://129.213.54.5:1080/restproxy/topics/testagain'
#while 1:
	#x=ser.readline()
	#if x[0] == 'a':
		#x1=x[1:]
		#print(x1)
	#else:
		#x2=x[1:]
		#print(x2)

#y= '{"schema": {"type": "struct","fields": [{"type": "string","optional": true,"field": "ID1"}, { "type": "string", "optional": true, "field": "ID2" }], "optional": false, "name": "testagain" }, "payload": {"ID1": "10000", "ID2": "bar"}}'
data = { "records" : [{ "value" : "22" }]}
headers = {'Content-Type':'application/vnd.kafka.json.v2+json'}
response = requests.post(url, data=json.dumps(data), headers=headers, auth=('admin','Oracle#1234567'), verify=False)
print response.text
