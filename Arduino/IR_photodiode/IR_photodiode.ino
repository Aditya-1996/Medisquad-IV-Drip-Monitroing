 int pd=2;                      //Photodiode to digital pin 2
 //int buzz=13;                   //piezo buzzer to digital pin 13 
 int senRead1=0;                 //Readings from sensor to analog pin 0 
 int senRead2=2;                //Readings from sensor to analog pin 1
 int limit=970;                 //Threshold range of an obstacle 
 //int threshold1 =  ;
 //int threshold2 =  ;
 void setup()   
 { 
  pinMode(pd,OUTPUT); 
  digitalWrite(pd,HIGH);       //supply 5 volts to photodiode 
  Serial.begin(9600);          //setting serial monitor at a default baund rate of 9600 
 } 
 void loop() 
 { 
  int val1=analogRead(senRead1);  //variable to store values from the photodiode 
  int val2=analogRead(senRead2); //variable to store values from the photodiode2 
  Serial.print("a");
  Serial.println(val1);          // prints the values from the sensor in serial monitor 
  Serial.print("b");
  Serial.println(val2);
  //if(val1 >= limit && val2 >= limit)              //If obstacle is nearer than the Threshold range 
      //Serial.println("HIGH"); 
  //else if(val2 >= limit && val1 < limit)          //If obstacle is not in Threshold range 
      //Serial.println("MEDIUM");
  //else
      //Serial.println("LOW");
  delay(3000);
 }  
