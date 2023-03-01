int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  digitalWrite(13, LOW);
  if(Serial.available() > 0) {
    if(Serial.read() != NULL) {
      digitalWrite(13, HIGH);
      delay(30);
    }
    else{
      digitalWrite(13, LOW);
    }
  } else {
    digitalWrite(13, LOW);
  }
}
