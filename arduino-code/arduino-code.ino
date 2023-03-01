void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  delay(1000);
  if (Serial.available() > 0) {
    String value = Serial.readStringUntil("\n");

    if (value == "FOUND") {
      digitalWrite(13, HIGH);
    }
  }
}
