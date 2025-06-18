float vout; 
float vRead; 
int dt = 100; 
float analogVal; 
void setup() { 
// put your setup code here, to run once: 
pinMode (vRead, INPUT); 
Serial.begin(9600); 
} 
void loop() { 
// put your main code here, to run repeatedly: 
analogVal = analogRead(vRead); 
vout = (5.*analogVal)/1023.; 
Serial.println(vout); 
delay(dt); 
}
