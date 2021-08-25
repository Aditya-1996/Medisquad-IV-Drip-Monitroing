curl -k -X POST https://129.213.157.132:1080/restproxy/topics/MEDISQUADEVENTHUB \
-H 'Authorization: <token>'  \
-H 'Content-Type: application/vnd.kafka.json.v2+json' \
-d '{
 "records" : [{ "value" : "A Sample Message" }]
 }' 

