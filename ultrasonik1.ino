#define trigPin 9
#define echoPin 10
#define led 12
#define led2 13

void setup() {
Serial.begin (9600);
pinMode(trigPin,OUTPUT);
pinMode(echoPin,INPUT);
pinMode (led,OUTPUT);
pinMode (led2,OUTPUT);
}

void loop() {
  long duration,distance;
digitalWrite(trigPin,LOW);
delayMicroseconds(2);
digitalWrite(trigPin,HIGH);
delayMicroseconds(10);
digitalWrite(trigPin,LOW);
duration = pulseIn(echoPin,HIGH);
distance = (duration/2)/29.1;
if(distance<4){
  digitalWrite(led,HIGH);
  digitalWrite(led2,LOW);
  
  }

  else{
    digitalWrite(led,LOW);
  digitalWrite(led2,HIGH);
  }

  if(distance>=200||distance<=0){
    Serial.println("Out of range");
  }

else{
      Serial.print(distance);
          Serial.println(" cm");
}
delay(500);
}
