void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(57600);
}

uint8_t cnt = 0;
uint8_t cmp = 20;

void loop() {
 
  cnt = (cnt+1);
  if (cnt==0) {
    digitalWrite(2, HIGH);
    cmp = (cmp+1);
    Serial.print(cmp);
  }
  if (cnt==cmp)
    digitalWrite(2, LOW);
  
}
