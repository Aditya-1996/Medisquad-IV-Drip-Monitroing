import requests
import json
import serial
import datetime

#url='https://129.213.54.5:1080/restproxy/topics/test'
#y= {"Country": "Canada", "Name": "Luke"}
#y= {"schema": {"type": "struct","fields": [{"type": "string","optional": "true","field": "ID1"}, { "type": "string", "optional": "true", "field": "ID2" }], "optional": "false", "name": "testagain" }, "payload": {"ID1": "90010", "ID2": "bar1"}}
#data={"records":[{ "value": 5 }]}, sort_keys=True

ser = serial.Serial('/dev/ttyUSB0',9600)
#url = "https://129.213.54.5:1080/restproxy/topics/IOT_DRIP_STATUS"
#url = "https://129.213.164.184:1080/restproxy/topics/MEDISQUADEventHub" 
url =  "https://129.213.164.184:1080/restproxy/topics/IOT_DRIP_STATUS"
headers = {'Content-type': 'application/vnd.kafka.json.v1+json'}
val1=0
val2=0
limit=1010
now = datetime.datetime.now() 	#getting the datetime object and passing it to a variable 
current_date=str(now) 		#using str method of datetime object 
flag=0
oicurl = "https://MEDISQUADOIC-orasenatdhubsblue02.integration.ocp.oraclecloud.com:443/ic/api/integration/v1/flows/rest/M_NOTIFY/1.0/notify"
previous_status="LOW"
while 1:
	x=ser.readline()
	if x[0] == 'a':
		val1=int(x[1:])
	elif x[0] == 'b':
		val2=int(x[1:])
	
	if val1 and val2:
		print(val1)
		print(val2)
		if val1 >= limit and val2 >= limit:               #If drip level is high (pings both as > limit)
      			current_status="HIGH"
			current_value="500"

		elif val2 >= limit and val1 < limit:       
      			current_status="MEDIUM"
			current_value="300"
  		
		elif val1 < limit and val2 < limit: 
     			current_status="LOW"
			current_value="100"
		
		if(current_status=="LOW" and previous_status=="MEDIUM"):
			flag=1
		
		previous_status=current_status
		
		print(current_status)

		y={"schema": {"type": "struct","fields": [{"type": "string","optional": "true","field": "IOT_ID"}, { "type": "string", "optional": "true", "field": "VALUE" },{"type": "string","optional": "true","field": "STATUS"},{"type": "string","optional": "true","field": "DEVICE_STATUS"},{"type": "string","optional": "true","field": "CREATED_DATE"},{"type": "string","optional": "true","field": "PATIENT_ID"},{"type": "string","optional": "true","field": "CREATED_BY"}],"optional": "false", "name": "IOT_DRIP_STATUS" },"payload": {"IOT_ID": "IOT1", "VALUE": current_value,"STATUS": current_status, "DEVICE_STATUS": "B", "CREATED_DATE" : current_date, "PATIENT_ID": "NA", "CREATED_BY": "IOT1"}}

		data= {"records" : [{ "value" : y}]}
		print("kunaltest")
		r = requests.post(url, headers=headers,data=json.dumps(data),auth=('admin','Oracle#1234567'),verify=False)
		print (r)

		if(flag>0):	
			data_oic={ "row": {"IOT_ID": "P001","STATUS": "LOW","D_MSG": "M", "TIMESTAMP" : current_date}}
			response= requests.post(oicurl, json=data_oic, auth=('api.user','Qwerty123456@'))
			print(response)
			flag=0

	
