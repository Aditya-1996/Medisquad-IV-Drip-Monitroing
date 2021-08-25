import requests
import json
import datetime

now = datetime.datetime.now() 	#getting the datetime object and passing it to a variable 
currentdate=str(now) 		#using str method of datetime object 

url='https://129.213.54.5:1080/restproxy/topics/test'

#y= {"Country": "Canada", "Name": "Luke"}
#y= {"schema": {"type": "struct","fields": [{"type": "string","optional": "true","field": "ID1"}, { "type": "string", "optional": "true", "field": "ID2" }], "optional": "false", "name": "testagain" }, "payload": {"ID1": "90010", "ID2": "bar1"}}
#data={"records":[{ "value": 5 }]}, sort_keys=True


y={"schema": {"type": "struct","fields": [{"type": "string","optional": "true","field": "IOT_ID"}, { "type": "string", "optional": "true", "field": "VALUE" },{"type": "string","optional": "true","field": "STATUS"},{"type": "string","optional": "true","field": "DEVICE_STATUS"},{"type": "string","optional": "true","field": "CREATED_DATE"},{"type": "string","optional": "true","field": "PATIENT_ID"},{"type": "string","optional": "true","field": "CREATED_BY"}],"optional": "false", "name": "IOT_DRIP_STATUS" },"payload": {"IOT_ID": "IOT11", "VALUE": "1000","STATUS": "LOW", "DEVICE_STATUS": "A", "CREATED_DATE" : "25-JAN-2019 22:00:00","PATIENT_ID": "P011", "CREATED_BY": "IOT11"}}
data= {"records" : [{ "value" : y}]}


print("kunaltest")



url = "https://129.213.54.5:1080/restproxy/topics/IOT_DRIP_STATUS"
#data = "{"records":[{"value": "{"\schema": {\"type\": \"struct\",\"fields\": [{\"type\": \"string\",\"optional\": true,\"field\": \"ID1\"}, { \"type\": \"string\", \"optional\": true, \"field\": \"ID2\" }], \"optional\": false, \"name\": \"testagain\" }, \"payload\": {\"ID1\": \"10000\", \"ID2\": \"bar\"}}"
headers = {'Content-type': 'application/vnd.kafka.json.v1+json'}
r = requests.post(url, headers=headers,data=json.dumps(data),auth=('admin','Oracle#1234567'),verify=False)
print (r)