
void setup() {
  
  pinMode (13, OUTPUT);
  pinMode (11, OUTPUT);
}


int dT = 1;
int cnt = 0;
int T0 = 8;
int T1 = 8;
int ANALOG_OUT = 255;

int notes[8] = {
  8,
  12,
  11,
  13, 
  9,
  10,
  20,
  11
};


int i = 0;
void loop() {

  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(T0);
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(T0);

  
  cnt = cnt+1;
  
   if (cnt==10) {
    cnt = 0;
    T0 = notes[i];
    i = (i+1)%8;
  }
}
