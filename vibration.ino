int Vib[4] = {12, 11, 10, 9};
int mode = 0; // 0: non-directional, 1: directional
int amplitude = 1;
int modeIsSet = 0;

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
    //String tmp = Serial.readString();
    //Serial.println("start new time block.");
    String tmp = Serial.readString();
    Serial.println("recv: " + tmp);
    int tmpLen = sizeof(tmp);
    char vibration[tmpLen];
    tmp.toCharArray(vibration, tmpLen);
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
}
