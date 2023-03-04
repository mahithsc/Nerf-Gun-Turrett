#include <Servo.h>
#include <ArduinoJson.h>

int incomingByte = 0;
Servo servo;
int servoPin = 9;

int getAngle(int actualAngle) {
  return actualAngle * 130 / 180;
}

void setup() {
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  servo.attach(servoPin);
  servo.write(getAngle(0));
}

void loop() {
  while(Serial.available() == 0){}

  // getting and parsing JSON
  StaticJsonDocument<256> doc;  // JSON document buffer
  DeserializationError error = deserializeJson(doc, Serial);  // Parse JSON data

  if(!error) {
    // setting the Serial data to local variables
    String command = doc["command"];


    if(command == "FIRE") {
      //  digitalWrite(13, HIGH);
      servo.write(120);
      servo.write(getAngle(90));
    }
      if(command == "DONTFIRE") {
      //  digitalWrite(13, LOW);
      servo.write(0);
    }
  }
}


