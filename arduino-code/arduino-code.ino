#include <Servo.h>
#include <ArduinoJson.h>

int incomingByte = 0;
Servo servo;

void setup() {
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  servo.attach(9);
  servo.write(0);
}

void loop() {
  while(Serial.available() == 0){}

  // getting the command
  // String command = Serial.readStringUntil('\r');

  StaticJsonDocument<256> doc;  // JSON document buffer
  DeserializationError error = deserializeJson(doc, Serial);  // Parse JSON data

  if(error) {
    digitalWrite(13, HIGH);
  } else {
    String command = doc["command"];
    // // checking commad output
   if(command == "FIRE") {
    //  digitalWrite(13, HIGH);
     servo.write(120);
     servo.write(90);
   }
    if(command == "DONTFIRE") {
    //  digitalWrite(13, LOW);
     servo.write(0);
   }
  }
}


