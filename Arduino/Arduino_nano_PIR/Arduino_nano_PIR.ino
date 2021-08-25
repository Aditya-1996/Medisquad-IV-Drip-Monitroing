int pirPin = 9;  //the digital pin connected to the PIR sensor's output  
 
void setup() {  
  Serial.begin(9600);  
  pinMode(pirPin, INPUT);   
  digitalWrite(pirPin, LOW);  
 }  
   
 void loop() {  
  if(digitalRead(pirPin) == HIGH)  
  {  
    Serial.println("1");  
    delay(500);
  }  
  if(digitalRead(pirPin) == LOW)  
  {    
    Serial.println("0");  
    delay(200);
  }
} 
