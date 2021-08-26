Follow the following steps to run a medisquad setup of raspi and website:

Pre-requisites:

1) Setup a mobile hotspot with the exact following details (because the raspberry pi is setup to run with it):
	Hotspot name : raspberryOracle
	Password : <shared on mail>

2) Connect to same hotspot using another phone and download and use fing from play store to find raspberry pi public IP address. 

For current setup, it is 129.168.43.140

3) SSH into the Pi with above public IP and following details :

username : pi
password : <shared on mail>

4) Connect the Arduino USB cable to the bottom right USB slot on raspi

5) Find and run the runpython2.py file in /home folder.
The file output should run and output details of connections and analog values of drip levels, and 200 OK.
Make sure that output is coming LOW and analog values far less than threshold value of 1000 (best if both values less than  850-900) 





Steps :

1) Open https://bangalorehubintegration-orasenatdpltintegration01.integration.ocp.oraclecloud.com/ic/builder/design/MEDISQUAD1_5_2_1_/1.0/preview/webApps/dripmanagment1/ > patient drip status > Bed 1 

(NOTE : This site can also be accessed from VBCS in 01 environment)

2) Make sure the Current status is set to "START" mode.

3) Enable live status using the sliding button.


This should do the trick as long as the python script in raspberry pi is up and running. Live status should now be getting updated in real time. 

4) IV drip can be drained and gets updated in real time



Troubleshooting : 

1) No public IP shows up in Fing : Make sure you're on same WiFi as the pi and try to reconnect.

2) If your raspi is on and you cannot to it: Make sure you're on same WiFi network as the Pi when trying to SSH into it.

3) Python script on the Pi gives error: Just rerun it. Its an initial configuration problem.

4) Both output values are at not in correct threshold/Output NOT showing LOW (when no IV drip): Adjust the sensors and wiring to fire directly at each other and try again. 

5) Script running fine and showing correct output but website not updating real time : Contact Kunal Kundan to help resolve this issue.  



