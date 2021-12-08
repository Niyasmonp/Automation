#include <ESP32Servo.h>
Servo servo;
  int trig=32;
  int echo=34;
  int d1,d2,d;
  float distance;
  void moveForward(){
  digitalWrite(25,LOW);
  digitalWrite(27,HIGH);
  digitalWrite(12,LOW);
  digitalWrite(13,HIGH);
} 
void moveReverse(){
  digitalWrite(25,HIGH);
  digitalWrite(27,LOW);
  digitalWrite(12,HIGH);
  digitalWrite(13,LOW);
  delay(1000);
}
void turnRight(){
//  digitalWrite(25,LOW);
//  digitalWrite(27,LOW);
//  digitalWrite(12,LOW);
  digitalWrite(13,HIGH);
}
void turnLeft(){
//  digitalWrite(25,LOW);
  digitalWrite(27,HIGH);
//  digitalWrite(12,LOW);
//  digitalWrite(13,LOW);
}
void Stop(){
  digitalWrite(25,LOW);
  digitalWrite(27,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,LOW);
  delay(1000);
}
void action(){
    Stop();
  servo.write(15);
  delay(500);
  d1=getDist();
  delay(300); 
  servo.write(90);
  delay(500);
  servo.write(180);
  delay(500);
  d2=getDist();
  delay(300);
  servo.write(90);
}
int getDist(){
    digitalWrite(trig,LOW);
    delayMicroseconds(2);
  
    digitalWrite(trig,HIGH);
    delayMicroseconds(10);
    
    digitalWrite(trig,LOW);
  
    float time=pulseIn(echo,HIGH);
  
    distance=time*0.034/2;
    return distance;
  }
void setup() {
  servo.attach(5);
  servo.write(90);
  pinMode(25,OUTPUT);
  pinMode(27,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);
  
}

void loop() {
    delay(500);
    d=getDist();
    if (d>36){moveForward();}
  else{
    action();
    Serial.println(d1);
    Serial.println(d2);
  if (d1>=d2){
    turnRight();
    }
  else if(d2>15) {turnLeft();
    }
//  else{moveReverse();}
    delay(330);}
}
