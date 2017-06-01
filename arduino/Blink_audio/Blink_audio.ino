
void setup() {
  
  pinMode (13, OUTPUT);
  pinMode (11, OUTPUT);
  Serial.begin(9600);
}


int cnt = 0;

void loop() {

  // read POTI voltage in range 0...1023
  int val = analogRead(A0);

  // map analog input voltage to correct output range
  int outVal = map (val, 0, 1023, 0, 255);
  
  // write POTI voltage to output 11 0...255
  analogWrite(11, outVal);


  // write outval to pc with USB
  Serial.println(outVal);

  delay(40);


  // TURN MOTOR PIN on and off
  if (cnt==0) {
    digitalWrite(13, HIGH);
  }
  if (cnt==30) {
    digitalWrite(13, LOW);
  }


  // count to 100 and start with 0 again
  cnt = (cnt+1)%100;
  
  delay(50);
}
