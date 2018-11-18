int Vib[4] = {12, 11, 10, 9};
int mode = 0; // 0: non-directional, 1: directional
int amplitude = 1;
int modeIsSet = 0;
String vibration;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(Vib[0], OUTPUT);
  pinMode(Vib[1], OUTPUT);
  pinMode(Vib[2], OUTPUT);
  pinMode(Vib[3], OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()) {
    if (!modeIsSet) {
      mode = Serial.read() - '0';
      Serial.print("Set mode");
      modeIsSet = 1;
    } 
    if (mode) { // mode: 1
      vibration = Serial.readString();
      Serial.print(vibration);
      for(int i = 0; i < 4; i ++){
        if (vibration[i] - '0') {
          digitalWrite(Vib[i], HIGH);  
        }  
        else {
          digitalWrite(Vib[i], LOW);  
        }
      }
      delay(500);
    }
    else { // mode: 0
      amplitude = Serial.read() - '0';
      Serial.print("I received amplitude: " + amplitude);
      for (int i  = 0; i < 4; i ++) {
        if (i < amplitude) {
          digitalWrite(Vib[i], HIGH);
        }
        else {
          digitalWrite(Vib[i], LOW);  
        }
      }
      delay(500);
    }
  }
}