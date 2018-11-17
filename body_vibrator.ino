void setup() {
  Serial.begin (9600);
  
  // if use analogWrite to control vibrator, analog Pin do not need to set
}

void loop() {
  Serial.println("Test analog toggle");
  for(int i = 0; i < 4; ++i) {
    Serial.print("Toggle with light: ");
    Serial.println(i*84);
    
    analogWrite(A0, i*84);
    delay(1500) ;
  }
}
