int Vib[4] = {12, 11, 10, 9};
int mode = 0; // 0: non-directional, 1: directional
int amplitude = 1;
int modeIsSet = 0;
//char *vibrations[16];
char vibrations[79];
int section = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(Vib[0], OUTPUT);
  pinMode(Vib[1], OUTPUT);
  pinMode(Vib[2], OUTPUT);
  pinMode(Vib[3], OUTPUT);

  memset(vibrations, 0, 79);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    // Handshake
    String tmp = Serial.readString();
    Serial.println("Start new time block.");
    // Data
    tmp = Serial.readString();
    Serial.println("recv: " + tmp);

    tmp.toCharArray(vibrations, 79);
  }
  else {
    if (strlen(vibrations) != 0) {
      int now_section = section % 16;
      for(int i = 0; i < 4; i ++) {
        if(vibrations[now_section * 4 + i] - '0') {
          digitalWrite(Vib[i], HIGH);
        }  
        else {
          digitalWrite(Vib[i], LOW);  
        }
      }
      section ++;
      delay(500);
    }
    else {
      for(int i = 0; i < 4; i ++) {
        digitalWrite(Vib[i], LOW);  
      }  
    }
  }
}
