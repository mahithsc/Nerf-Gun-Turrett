#include <Servo.h>

int incomingByte = 0;
Servo myservo;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  myservo.attach(9);
  myservo.write(0);
}

void loop() {
  delay(40);
  digitalWrite(13, LOW);
  if(Serial.available() > 0) {
    if(Serial.read() != NULL) {
      digitalWrite(13, HIGH);
      myservo.write(90);
    }
    else{
      digitalWrite(13, LOW);
      myservo.write(0);
    }
  } else {
    digitalWrite(13, LOW);
    myservo.write(0);
  }
}
